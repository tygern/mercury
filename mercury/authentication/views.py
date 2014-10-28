from flask import request, jsonify
from mercury import app
from mercury.services import authentication_service


@app.route('/login', methods=['POST'])
def login():
    login_result = authentication_service.login(request.form['username'], request.form['password'])


    print login_result

    return jsonify(login_result)


@app.route('/logout')
def logout():
    return jsonify(authentication_service.logout())