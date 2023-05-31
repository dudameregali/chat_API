from app import app, sockets
import threading
from flask_sockets import Sockets
from routes import mensagem_route

# Lista para armazenar os clientes conectados
clientes_conectados = []

@sockets.route('/chat/')
def chat_socket(ws):
    # Inicie uma nova thread para lidar com o cliente
    thread = threading.Thread(target=handle_client, args=(ws,))
    thread.start()

    # Lógica para lidar com cada conexão de usuário individualmente
    while not ws.closed:
        message = ws.receive()

        # Quando uma mensagem é recebida, envie-a para todos os clientes conectados
        broadcast_message(message)

    # Remova o cliente da lista de clientes conectados ao encerrar a conexão
    clientes_conectados.remove(ws)
    # Feche a conexão quando a thread terminar
    ws.close()

def handle_client(ws):
    # Adicione o cliente à lista de clientes conectados
    clientes_conectados.append(ws)

    # Resto da lógica para lidar com cada conexão de usuário individualmente

def broadcast_message(message):
    # Envie a mensagem para todos os clientes conectados
    for cliente in clientes_conectados:
        cliente.send(message)

if __name__ == '__main__':
    sockets.init_app(app)
    app.register_blueprint(mensagem_route)
    app.run()


# Certifique-se de instalar as bibliotecas necessárias, 
# como flask-sockets, gevent, gevent-websocket, 
# e flask-cors, usando o comando pip install flask-sockets 
# gevent gevent-websocket flask-cors no seu ambiente virtual 
# Python antes de executar o servidor.
