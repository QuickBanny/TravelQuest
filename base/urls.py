from .views import MainHandler


def get_api_urls() -> list:
    return [
        ('/', MainHandler)
    ]