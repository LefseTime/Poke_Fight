from flask import Flask, render_template, url_for, jsonify, request
app = Flask(__name__)
import flask_ui as ui
import logic

@app.route("/")
def main():
    return render_template('main.html')


def pokeFight(user_poke, wild_poke):
    logic.fight(user_poke, wild_poke)


if __name__ == '__main__':
    app.run(debug=True)