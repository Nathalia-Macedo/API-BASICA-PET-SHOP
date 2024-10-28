
from flask import Flask, jsonify, request
from flask_cors import CORS  # Importe a biblioteca CORS

# Inicia a aplicação Flask
app = Flask(__name__)  
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5001"}})


# Simulação de "banco de dados" com uma lista de pets
pets_db = [
    {"id": 1, "name": "Bolt", "species": "dog", "age": 2, "is_favorite": False, "is_adopted": False},
    {"id": 2, "name": "Mittens", "species": "cat", "age": 3, "is_favorite": False, "is_adopted": False},
    {"id": 3, "name": "Charlie", "species": "dog", "age": 4, "is_favorite": True, "is_adopted": False},
    {"id": 4, "name": "Whiskers", "species": "cat", "age": 1, "is_favorite": False, "is_adopted": True},
    {"id": 5, "name": "Goldie", "species": "fish", "age": 1, "is_favorite": False, "is_adopted": False}
]

# Rota básica para verificar se a API está funcionando
@app.route('/')
def home():
    return "API Funcionando!"  

@app.route('/pets', methods=['GET'])
def get_pets():
    return jsonify(pets_db)  

# @app.route('/pets', methods=['POST'])
# def add_pet():
#     new_pet = request.get_json() 
#     new_pet['id'] = len(pets_db) + 1  
#     pets_db.append(new_pet) 
#     return jsonify(new_pet), 201  


@app.route('/favorite/<int:pet_id>', methods=['POST'])
def favorite_pet(pet_id):
    for pet in pets_db:
        if pet["id"] == pet_id:
            pet["is_favorite"] = not pet["is_favorite"]  # Alterna o estado de favorito
            return jsonify({"success": True, "is_favorite": pet["is_favorite"]})
    return jsonify({"success": False, "message": "Pet not found"}), 404


@app.route('/pets/<int:pet_id>/adopt', methods=['POST'])
def adopt_pet(pet_id):
    for pet in pets_db:
        if pet["id"] == pet_id:
            pet["is_adopted"] = True  # Marca o pet como adotado
            return jsonify({"success": True})
    return jsonify({"success": False, "message": "Pet not found"}), 404

# Executa a aplicação
if __name__ == "__main__":
    app.run(debug=True)
