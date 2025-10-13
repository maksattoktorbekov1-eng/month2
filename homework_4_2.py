class BaseView:
    def render(self):
        print("Template render")


class LoggingMixin:
    def render(self):
        print("Log: start")
        super().render()
        print("Log: end")


class AuthRequiredMixin:
    def __init__(self, authorized=False):

        super().__init__()
        self.authorized = authorized

    def render(self):
        if self.authorized:
            print("Auth OK")
            super().render()
        else:
            print("Access denied")


class AdminPageView(AuthRequiredMixin, LoggingMixin, BaseView):
    def render(self):
        print("Admin page render start")
        super().render()
        print("Admin page render end")


print("\n=== Авторизованный пользователь ===")
admin_page = AdminPageView(authorized=True)
admin_page.render()

print("\n=== Неавторизованный пользователь ===")
admin_page2 = AdminPageView(authorized=False)
admin_page2.render()
