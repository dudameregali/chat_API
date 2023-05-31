from flask import Flask
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
sockets = Sockets(app)

if __name__ == '__main__':
    from routes import mensagem_route
    app.register_blueprint(mensagem_route)
    
    http_server = WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
