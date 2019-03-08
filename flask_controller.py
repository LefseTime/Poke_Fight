from flask import Flask, render_template, url_for, jsonify, request, session
# from flask_session import Session
from fight import Fight, Round
from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap
app = Flask(__name__)
import flask_ui as ui
import flask_logic as logic
import uuid

app.secret_key = 'abc123'
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

    session['user_poke_name'] = user_poke.name.title()
    session['user_poke_type'] = user_poke.type
    session['user_poke_sad'] = user_poke.sad_sound
    session['user_poke_happy'] = user_poke.happy_sound
    session['user_poke_base_hp'] = user_poke.hp
    session['user_poke_current_hp'] = user_poke.hp
    session['user_poke_attack'] = user_poke.attack
    session['user_poke_defense'] = user_poke.defense
    session['user_poke_speed'] = user_poke.speed

    session['wild_poke_name'] = wild_poke.name.title()
    session['wild_poke_type'] = wild_poke.type
    session['wild_poke_sad'] = wild_poke.sad_sound
    session['wild_poke_happy'] = wild_poke.happy_sound
    session['wild_poke_base_hp'] = wild_poke.hp
    session['wild_poke_current_hp'] = wild_poke.hp
    session['wild_poke_attack'] = wild_poke.attack
    session['wild_poke_defense'] = wild_poke.defense
    session['wild_poke_speed'] = wild_poke.speed
    
    return jsonify({
        'status': 'success',
        'texts': ui.encounterWildPoke(wild_poke),
        'user': {'name': user_poke.name.title(), 'hp': user_poke.hp},
        'wild': {'name': wild_poke.name, 'hp': wild_poke.hp},
    })

@app.route("/api/round", methods=['POST'])
def initialize_round():
    json_data = request.get_json()
    move = json_data['move']
    return jsonify({
        'status': 'success',
        'move': move,
        'pleasework': session['user_poke_name']
    })



if __name__ == '__main__':
    app.run(debug=True)