from flask import request, session, flash, jsonify
from mercury import app


@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.form['username'] != app.config['USERNAME']:
        error = 'Invalid username'
    elif request.form['password'] != app.config['PASSWORD']:
        error = 'Invalid password'
    else:
        session['logged_in'] = True

    return jsonify({
        "success": error is None,
        "message": error
    })


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return {"success": True}