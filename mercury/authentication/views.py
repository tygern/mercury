from flask import request, g, session, redirect, render_template, flash
from mercury import app, oid, db
from mercury.authentication import authentication_service
from mercury.user import user_service


@app.before_request
def lookup_current_user():
    authentication_service.set_current_user()


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if authentication_service.logged_in():
        return redirect(oid.get_next_url())
    if request.method == 'POST':
        return authentication_service.external_login()
    return render_template('login.html', next=oid.get_next_url(),
                           error=oid.fetch_error())


@oid.after_login
def create_or_login(resp):
    user = user_service.find_by(openid=resp.identity_url)
    if user is None:
        user_service.create(name=resp.fullname or resp.nickname, email=resp.email, openid=resp.identity_url)

    authentication_service.login(user)

    flash(u'Successfully signed in')
    return redirect(oid.get_next_url())


@app.route('/logout')
def logout():
    authentication_service.logout()
    flash(u'You were signed out')
    return redirect(oid.get_next_url())

