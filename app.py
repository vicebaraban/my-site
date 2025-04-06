import json
import os
import sys

from flask import Flask, redirect, url_for, render_template, request, session, jsonify


app = Flask(__name__, static_url_path='',
            static_folder="static", template_folder="templates")
app.secret_key = "secret key"


@app.route("/vk_ok_auth", methods=["POST"])
def vk_ok_auth():
    user_data = request.json
    name = user_data.get('name', '')
    surname = user_data.get('surname', '')

    session['name'] = name
    session['surname'] = surname

    return jsonify({
        'status': 'ok',
    })


@app.route('/')
def main_page():
    name = session.get('name', None)
    surname = session.get('surname', None)
    return render_template("index.html", is_auth=bool(name), name=name, surname=surname)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
