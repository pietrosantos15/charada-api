from flask import Flask, jsonify, request
import random  # Biblioteca para escolher charadas aleatoriamente
from flask_cors import CORS  # Permite requisições de diferentes origens (Cross-Origin Resource Sharing)
import firebase_admin
from firebase_admin import credentials, firestore
import os, json

# Inicializa o aplicativo Flask
app = Flask(__name__)
CORS(app)  # Habilita o CORS para permitir requisições de outras origens
FBKey = json.loads(os.getenv('CONFIG_FIREBASE'))


# Conecta ao Firestore usando um arquivo de credenciais JSON
cred = credentials.Certificate(FBKey)
firebase_admin.initialize_app(cred)

db = firestore.client()  # Obtém a referência ao banco de dados Firestore

# Rota principal para verificar se a API está funcionando
@app.route('/', methods=['GET'])
def index():
    return 'api on fire 🔥'  # Mensagem indicativa de que a API está online

# Rota para obter uma charada aleatória (parece estar incompleta no código original)  # Aqui falta a definição da variável "charadas"

# Rota para buscar uma charada aleatória do Firestore
@app.route('/charadas', methods=['GET'])
def charada_aleatoria():
    charadas = []
    lista = db.collection('charadas').stream()  # Busca todas as charadas no Firestore
    for item in lista:
        charadas.append(item.to_dict())  # Converte os documentos em dicionários

    if charadas:
        return jsonify(random.choice(charadas)), 200  # Retorna uma charada aleatória
    else:
        return jsonify({'Erro': 'Nenhuma charada encontrada'}), 404  # Retorna erro se não houver charadas

# Rota para buscar uma charada específica pelo ID
@app.route('/charadas/<id>', methods=['GET'])
def busca(id):
    doc_ref = db.collection('charadas').document(id)  # Obtém a referência do documento pelo ID
    doc = doc_ref.get().to_dict()  # Converte o documento em um dicionário

    if doc:
        return jsonify(doc), 200  # Retorna a charada encontrada
    else:
        return jsonify({'Mensagem': 'Charada não encontrada'}), 404  # Retorna erro se não existir

# Rota para adicionar uma nova charada
@app.route('/charadas', methods=['POST'])
def adicionar_charada():
    dados = request.json  # Obtém os dados enviados no corpo da requisição

    # Verifica se os campos obrigatórios estão presentes
    if "pergunta" not in dados or "resposta" not in dados:
        return jsonify({'Mensagem': 'Campo pergunta e resposta são obrigatórios'}), 400
    
    # Gerenciamento do contador de ID
    contador_ref = db.collection('controle_id').document('contador')
    contador_doc = contador_ref.get().to_dict()
    ultimo_id = contador_doc.get('id')  # Obtém o último ID salvo
    novo_id = int(ultimo_id) + 1  # Incrementa o ID
    contador_ref.update({'id': novo_id})  # Atualiza o contador no Firestore

    # Grava a nova charada no Firestore
    db.collection('charadas').document(str(novo_id)).set({
        "id": novo_id,
        "pergunta": dados['pergunta'],
        "resposta": dados['resposta']
    })

    return jsonify({'Mensagem': 'Charada cadastrada com sucesso'}), 201  # Retorna mensagem de sucesso

# Rota para alterar uma charada existente pelo ID
@app.route('/charadas/<id>', methods=['PUT'])
def alterar_charada(id):
    dados = request.json  # Obtém os dados enviados na requisição

    # Verifica se os campos obrigatórios estão presentes
    if "pergunta" not in dados or "resposta" not in dados:
        return jsonify({'Mensagem': 'Campo pergunta e resposta são obrigatórios'}), 400

    doc_ref = db.collection('charadas').document(id)  # Obtém a referência do documento
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            'pergunta': dados['pergunta'],
            'resposta': dados['resposta']
        })
        return jsonify({'Mensagem': 'Charada alterada com sucesso'}), 200  # Retorna sucesso
    else:
        return jsonify({'Mensagem': 'Erro. Charada não encontrada'}), 404  # Retorna erro se não existir

# Rota para excluir uma charada pelo ID
@app.route('/charadas/<id>', methods=['DELETE'])
def excluir_charada(id):
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()
    
    if not doc.exists:
        return jsonify({'mensagem': 'Erro - Charada não encontrada!'}), 404  # Retorna erro se não existir
    
    doc_ref.delete()  # Exclui a charada do Firestore
    return jsonify({'mensagem': 'Charada excluída com sucesso!'}), 200  # Retorna sucesso

# Inicia o servidor Flask no modo de depuração
if __name__ == '__main__':
    app.run(debug=True)