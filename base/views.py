from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write({'message': 'hello'})