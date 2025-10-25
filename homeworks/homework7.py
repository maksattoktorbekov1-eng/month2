import sqlite3


def create_connection():
    connection = sqlite3.connect("library.db")
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    connection.commit()
    connection.close()
    print("Таблица 'books' успешно создана.")


def insert_books():
    connection = create_connection()
    cursor = connection.cursor()

    books = [
        ("Джамиля", "Чингиз Айтматов", 1958, "Повесть", 96, 8),
        ("Прощай, Гульсары!", "Чингиз Айтматов", 1966, "Роман", 210, 5),
        ("И дольше века длится день", "Чингиз Айтматов", 1980, "Роман", 450, 4),
        ("Плаха", "Чингиз Айтматов", 1986, "Роман", 512, 3),
        ("Белый пароход", "Чингиз Айтматов", 1970, "Повесть", 160, 6),
        ("Первый учитель", "Чингиз Айтматов", 1962, "Повесть", 120, 7),
        ("Тополёк мой в красной косынке", "Чингиз Айтматов", 1961, "Повесть", 80, 10),
        ("Материнское поле", "Чингиз Айтматов", 1963, "Рассказ", 75, 9),
        ("Когда падают горы ", "Чингиз Айтматов", 2006, "Роман", 470, 2),
        ("Тавро Кассандры", "Чингиз Айтматов", 1995, "Фантастика", 430, 3)
    ]

    cursor.executemany("""
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()
    connection.close()
    print("10 книг Чингиза Айтматова успешно добавлены в таблицу.")


def delete_book(book_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()
    print(f"Книга с id={book_id} удалена.")


def add_deleted_column_and_archive_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("PRAGMA table_info(books)")
    columns = [col[1] for col in cursor.fetchall()]
    if "deleted" not in columns:
        cursor.execute("ALTER TABLE books ADD COLUMN deleted INTEGER DEFAULT 0")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books_archive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    connection.commit()
    connection.close()
    print("Добавлена колонка 'deleted' и создана таблица 'books_archive'.")


def soft_delete(book_id):
    connection = create_connection()
    cursor = connection.cursor()

    result = cursor.execute(
        "SELECT name, author, publication_year, genre, number_of_pages, number_of_copies FROM books WHERE id = ?",
        (book_id,))
    book = result.fetchone()

    if book:

        cursor.execute("UPDATE books SET deleted = 1 WHERE id = ?", (book_id,))

        cursor.execute("""
            INSERT INTO books_archive (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        """, book)
        print(f"Книга с id={book_id} мягко удалена и перенесена в архив.")
    else:
        print(f"Книга с id={book_id} не найдена.")

    connection.commit()
    connection.close()


def hard_delete(book_id):
    connection = create_connection()
    cursor = connection.cursor()

    result = cursor.execute("SELECT deleted FROM books WHERE id = ?", (book_id,))
    book = result.fetchone()

    if book and book[0] == 1:
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        print(f"Книга с id={book_id} полностью удалена из базы.")
    else:
        print(f"Книга с id={book_id} не помечена как удалённая или не существует.")

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_table()
    insert_books()
    delete_book(2)

    add_deleted_column_and_archive_table()
    soft_delete(4)
    hard_delete(4)
