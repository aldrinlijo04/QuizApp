from flask import Blueprint, request, render_template, redirect, url_for
from utils import admin_required, custom_jwt_required
from flask_jwt_extended import verify_jwt_in_request

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
@custom_jwt_required()
def index():
    return render_template('dashboard.html')

@frontend_bp.route('/login')
def loginpage():
    if verify_jwt_in_request(optional=True):
        return redirect('/')
    return render_template('login.html')


@frontend_bp.route('/register')
def registerpage():
    return render_template('register.html')

@frontend_bp.route('/attempt')
def attemptpage():
    return render_template('attempt.html')

@frontend_bp.route('/quiz_create')
def quizcreatepage():
    return render_template('quiz_create.html')

@frontend_bp.route('/result')
def resultpage():
    return render_template('result.html')

@frontend_bp.route('/logout')
def logout():
    return redirect(url_for('auth.logout'))