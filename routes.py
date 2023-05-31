from flask import Blueprint, jsonify, request
import threading
from app import sockets

mensagem_route = Blueprint('mensagem', __name__)

@mensagem_route.route('/mensagens/', methods=['POST'])
def receber_mensagem():
    mensagem = request.json['mensagem']
    # Criar uma nova thread para processar a mensagem
    thread = threading.Thread(target=processar_mensagem, args=(mensagem,))
    thread.start()
    return jsonify({'status': 'Mensagem recebida com sucesso'})

def processar_mensagem(mensagem):
    # Faça o processamento necessário com a mensagem
    # Envie a mensagem para o front-end React
    # ...

    # Envie a mensagem para todos os clientes conectados
    for ws in sockets:
        ws.send(mensagem)
