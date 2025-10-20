# homework_4_1.py

class Vehicle:
    def start(self):
        print("Vehicle starting")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")


class ElectricCar(Vehicle):
    def start(self):
        super().start()


class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print("Tesla ready")


class BaseView:
    def render(self):
        print("Template render")


class LoggingMixin:
    def render(self):
        print("Log: start")
        super().render()
        print("Log: end")


class AuthRequiredMixin:

    def __init__(self, authed=True, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.authed = authed

    def render(self):
        if self.authed:
            print("Auth OK")
            super().render()
        else:
            print("Access denied")


class AdminPageView(LoggingMixin, AuthRequiredMixin, BaseView):
    def __init__(self, authed=True):
        super().__init__(authed=authed)

    def render(self):
        print("Admin page render start")
        super().render()
        print("Admin page render end")


if __name__ == "__main__":
    print("=== Тест: Tesla.start() ===")
    t = Tesla()
    t.start()

    print("\n=== Тест: AdminPageView (authed=True) ===")
    admin_auth = AdminPageView(authed=True)
    admin_auth.render()

    print("\n=== Тест: AdminPageView (authed=False) ===")
    admin_noauth = AdminPageView(authed=False)
    admin_noauth.render()
