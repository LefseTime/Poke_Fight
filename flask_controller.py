from flask import Flask, render_template, url_for
app = Flask(__name__)
import flask_ui as ui

@app.route("/")
def intro():
    return render_template('intro.html', texts = ui.texts)

def run():
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)