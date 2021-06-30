from .views import RegisterHandler, LoginHandler, LogoutHandler


def get_auth_urls() -> list:
    return [
        ('/register', RegisterHandler),
        ('/login', LoginHandler),
        ('/logout', LogoutHandler)
    ]