import sqlite3


def create_connection():
    connection = sqlite3.connect("library.db")
    return connection


def get_books_by_author(author):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, author, publication_year, genre, number_of_pages, number_of_copies
        FROM books
        WHERE author = ?
        ORDER BY name ASC
    """, (author,))

    books = cursor.fetchall()
    connection.close()

    if books:
        print(f"\n Книги автора: {author}")
        for book in books:
            print(f"- {book[0]} ({book[2]}), жанр: {book[3]}, страниц: {book[4]}, копий: {book[5]}")
    else:
        print(f"\nАвтор '{author}' не найден в базе данных.")


if __name__ == "__main__":
    author_name = input("Введите имя автора: ")
    get_books_by_author(author_name)
