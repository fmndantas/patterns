import sqlite3
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os

BASEDIR = os.path.dirname(__file__)
TEMPLATES = os.path.join(BASEDIR, 'templates')


# Just for caution
class DatabaseSingleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, 'db'):
            cls.db = super(DatabaseSingleton, cls).__call__(*args, **kwargs)
        return cls.db


# Model
class DatabaseConnection(metaclass=DatabaseSingleton):
    def __init__(self):
        self._status = None
        self._connection = None
        self._cursor = None

    def set_status(self, new_status):
        self._status = new_status

    def get_status(self):
        return self._status

    def connect(self, name):
        self._connection = sqlite3.connect(name)
        self.get_cursor()

    def get_cursor(self):
        self._cursor = self._connection.cursor()

    def execute(self, query):
        return self._cursor.execute(query)

    def commit_and_close(self):
        self._connection.commit()
        self._connection.commit()


# Controllers
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = "select * from task"
        todos = db_execute(query)
        self.render('index.html', todos=todos)


class NewHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task (id INTEGER \
            PRIMARY KEY, name TEXT, status NUMERIC)"
        db_execute(query)
        query = f"insert into task (name, status) values {name, 1}"
        db_execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')


class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = f"update task set status={int(status)} where id={id}"
        db_execute(query)
        self.redirect('/')


class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
        query = f"delete from task where id={id}"
        db_execute(query)
        self.redirect('/')


class RunApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/todo/new', NewHandler),
            (r'/todo/update/(\d+)/(\d+)', UpdateHandler),
            (r'/todo/delete/(\d+)', DeleteHandler)
        ]
        settings = {
            'debug': True,
            'template_path': TEMPLATES,
            'static_path': 'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def db_execute(query):
    return db.execute(query)


if __name__ == '__main__':
    db = DatabaseConnection()
    db.connect(os.path.join(BASEDIR, "task.db"))
    # FIXME: works but is ugly
    try:
        http_server = tornado.httpserver.HTTPServer(RunApp())
        http_server.listen(5000)
        tornado.ioloop.IOLoop.instance().start()
    finally:
        db.commit_and_close()
