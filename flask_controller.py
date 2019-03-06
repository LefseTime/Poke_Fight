from flask import Flask, render_template, url_for, jsonify, request
app = Flask(__name__)
import flask_ui as ui

@app.route("/")
def main():
    return render_template('main.html')


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
    print(request.form)
    return jsonify({
        'status': 'success',
        'texts': ui.prompt_name(json_data['type'])
    })




if __name__ == '__main__':
    app.run(debug=True)