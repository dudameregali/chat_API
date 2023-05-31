import json

def serializar_mensagem(mensagem):
    mensagem_serializada = json.dumps({'mensagem': mensagem})
    return mensagem_serializada
