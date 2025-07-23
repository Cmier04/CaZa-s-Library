# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 18, 2025
# Project Name: CaZa's Library
# File Purpose: This file helps connecting the different pages together through routing.

# --------------------------List of TODO's-------------------------------
  # TODO: implement signup(): prompts user for username and email then redirects to home page
  # TODO: implement login(): prompts the user for username and member_id or staff_id, redirects to home page (for staff, to their account to check library)
  # TODO: implement user_account(): holds user information which is given when the user creates a new account, for staff they can check overdue status and modify user accounts/books
  # TODO: implement logout(): logs users out of their accounts and redirects them to the home page under guest view
  # TODO: test and ensure all routes lead to a defined page

# --------------------------Changes Made---------------------------------
    # Comment changes made to this file here, keeps track of changes if commit contains multiple files.'
    # Added different page routes and specified todo's

# ------------------------NOTE-----------------------
    # if the way this was implemented does not work, look into manually writing out the routes between pages
    # make sure to use render_template in order to load the HTML file 

import sys
import os
from flask import Blueprint, render_template, request, redirect, session
from backend.functions import load_users, save_users
from backend.classes import Manager

bp = Blueprint('main', __name__)

user_data = load_users()
manager = Manager(user_data)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    'implements the functionality of the member application page'

@bp.route('/login', methods=['GET', 'POST'])
def login():
    'implements functions of the member/staff login page'

@bp.route('/account')
def user_account():
    'defines and implements what can be seen in the staff/members account'

@bp.route('/logout')
def logout():
    'logs out the user and ends the session by redirecting the user to the guest home page'
