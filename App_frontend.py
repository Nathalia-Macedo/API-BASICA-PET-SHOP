import requests
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

API_BASE_URL = "http://127.0.0.1:5000"  # Endereço da API local

# Rota para exibir a lista de pets
@app.route('/')
def index():
    # Consome a API para obter os pets
    response = requests.get(f"{API_BASE_URL}/pets")  
    pets = response.json()
    # Renderiza o template com os pets
    return render_template("index.html", pets=pets) 

# Rota para marcar/desmarcar um pet como favorito
@app.route('/favorite/<int:pet_id>', methods=['POST'])
def favorite_pet(pet_id):
    # Enviando o id do pet que será favoritado
    requests.post(f"{API_BASE_URL}/favorite/{pet_id}")
    # Redirecionando para a função index
    return redirect(url_for('index'))

@app.route('/adopt/<int:pet_id>', methods=['POST'])
def adopt_pet(pet_id):
    requests.post(f"{API_BASE_URL}/pets/{pet_id}/adopt")
    return redirect(url_for('index'))

# Executa o servidor Flask
if __name__ == "__main__":
    app.run(port=5001, debug=True)
