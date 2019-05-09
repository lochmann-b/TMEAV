from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from . import auth
from ..models import User
from .. import db
from ..decorators import admin_required

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.activated and user.verify_password(form.password.data):            
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)                        
        flash('Invalid username / password or inactive account')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created. You can log in a soon as your account has been activated by an admin.")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/activate/<userid>/<token>')
@login_required
@admin_required()
def activate(userid, token):
    user = User.query.filter_by(id=userid).first()
    if user == None:
        flash("User not found")
    elif user.activated:
        flash("User already activated")
    elif user.set_activated(token, True):
        db.session.commit()
        flash('User {} activated'.format(user.username))
    else:
        flash('Something went wrong')
    return redirect(url_for('auth.users'))

@auth.route('/deactivate/<userid>/<token>')
@login_required
@admin_required()
def deactivate(userid, token):
    user = User.query.filter_by(id=userid).first()
    if user == None:
        flash("User not found")
    elif not user.activated:
        flash("User already deactivated")
    elif user.set_activated(token, False):
        db.session.commit()
        flash('User {} deactivated'.format(user.username))
    else:
        flash('Something went wrong')
    return redirect(url_for('auth.users'))



@auth.route('/deletuser/<userid>/<token>')
@login_required
@admin_required()
def delet_user(userid, token):
    user = User.query.filter_by(id=userid).first()
    if user == None:
        flash("User not found")   
    elif user.check_token(token):
        db.session().delete(user)
        db.session().commit()
        flash("User {} deleted".format(user.username))
    else:
        flash('Something went wrong')
    return redirect(url_for('auth.users'))

@auth.route('/users')
@admin_required()
def users():
    return render_template('auth/users.html', users=User.query.order_by(User.id).all())