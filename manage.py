from flask_script import Manager, Server
from app import create_app

app = create_app('develop')
manager = Manager(app)
server = Server(host='0.0.0.0', port=7777)
manager.add_command('runserver', server)


@app.route('/')
def index():
    return ''


if __name__ == '__main__':
    manager.run()
