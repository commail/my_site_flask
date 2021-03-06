from flask_script import Manager, Server
from app import create_app
from gevent.pywsgi import WSGIServer
from flask_migrate import MigrateCommand
# from comm.set_response import MyResponse

env = 'develop'
app = create_app(env)
# app.response_class = MyResponse


if __name__ == '__main__':
    if env == 'develop':
        manager = Manager(app)
        manager.add_command('db', MigrateCommand)
        server = Server(host='0.0.0.0', port=7777)
        manager.add_command('runserver', server)
        manager.run()
    else:
        http_server = WSGIServer(('0.0.0.0', 7777), app)
        http_server.serve_forever()
