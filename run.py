import tornado.ioloop
from tornado.web import Application
from base.urls import get_api_urls
from auth.urls import get_auth_urls


def init_app():
    return Application(
        get_api_urls() +
        get_auth_urls()
    )


if __name__ == "__main__":
    app = init_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()