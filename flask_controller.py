from flask import Flask, render_template, url_for, jsonify, request
from fight import Fight, Round
from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap
app = Flask(__name__)
import flask_ui as ui
import flask_logic as logic

@app.route("/")
def main():
    return render_template('main.html')


def pokeFight(user_poke, wild_poke):
    logic.fight(user_poke, wild_poke)


@app.route("/api/intro", methods=['GET'])
def intro():
    return jsonify({
        'status': 'success',
        'texts': ui.intro_texts()
    })

@app.route("/api/type-list", methods=['GET'])
def type_list():
    return jsonify({
        'status': 'success',
        'types': ui.types()
    })

@app.route("/api/prompt-name", methods=['POST'])
def prompt_name():
    json_data = request.get_json()
    return jsonify({
        'status': 'success',
        'texts': ui.prompt_name(json_data['type'])
    })

@app.route("/api/prompt-sad", methods=['POST'])
def prompt_sad():
    json_data = request.get_json()
    return jsonify({
        'status': 'success',
        'texts': ui.prompt_sad(json_data['name'])
    })

@app.route("/api/prompt-happy", methods=['POST'])
def prompt_happy():
    json_data = request.get_json()
    return jsonify({
        'status': 'success',
        'texts': ui.prompt_happy(json_data['name'])
    })

@app.route("/api/initialize-user", methods=['POST'])
def initialize_user():
    json_data = request.get_json()
    user_poke = logic.initializeUserPoke(json_data['type'], json_data['name'], json_data['happy'], json_data['sad'])
    wild_poke = logic.createWildPoke()
    fight = logic.initializeFight(user_poke, wild_poke)
    return jsonify({
        'status': 'success',
        'texts': ui.encounterWildPoke(wild_poke),
        'user': {'name': user_poke.name.title(), 'hp': user_poke.hp},
        'wild': {'name': wild_poke.name, 'hp': wild_poke.hp}
    })

@app.route("/api/round", methods=['POST'])
def initialize_round():
    json_data = request.get_json()
    move = json_data['move']
    return jsonify({
        'status': 'success',
        'move': move
    })



if __name__ == '__main__':
    app.run(debug=True)