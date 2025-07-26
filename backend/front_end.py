# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 18, 2025
# Project Name: CaZa's Library
# File Purpose: This file helps connecting the different pages together through routing.

# --------------------------List of TODO's-------------------------------
  # TODO: implement signup(): prompts user for username and email then redirects to home page
  # TODO: implement login(): prompts the user for username and member_id or staff_id, redirects to home page (for staff, to their account to check library)
  # TODO: implement member_application(): holds user information which is given when the user creates a new account, for staff they can check overdue status and modify user accounts/books
  # TODO: implement logout(): logs users out of their accounts and redirects them to the home page under guest view
  # TODO: implement home_members(): home page for members which allows them to log out from the nav bar (call log out f)
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

bp = Blueprint('frontend', __name__, template_folder='../frontend/templates', static_folder='../frontend/static', static_url_path='/frontend_static')

user_data = load_users()
#manager = Manager(user_data)

#---------------------------------User Home Pages---------------------------------
@bp.route('/')
def home():
   return render_template('home.html')

@bp.route('/home_members')
def home_members():
    'members home page which gets rid of log in and sign up feature, replacing them with logout'
    session['user_type'] = 'member'
    return render_template('home_members.html', user_type = 'member')

@bp.route('/home_staff')
def home_staff():
    'staff home page which gives them a summary of overdue books'
    session['user_type'] = 'staff'
    return render_template('home_staff.html', user_type = 'staff')

#---------------------------------User Log in and Sign up---------------------------------
@bp.route('/apply')
def apply():
    'implements the functionality of the member application page'
    return render_template('member_application.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    'implements functions of the member/staff login page'
    if request.method == 'POST':
        username = request.form.get('username')
        user_id = request.form.get('member')
        role = request.form.get('role')

        manager = Manager(user_data=None)

        result = manager.loginUser(role, username, user_id)

        if result == 'Member Login succeede.':
            session['user_type'] = 'member'
            session['username'] = username
            return redirect(url_for('frontend.home_members'))
        elif result == "Staff Login succeeded.":
            session['user_type'] = 'staff'
            session['username'] = username
            return redirect(url_for('frontend.home_staff'))
        else:
            error: "Invalid name or ID. Please try again."
            return render_template('login.html', error=error)
    return render_template('login.html')

@bp.route('/logout')
def logout():
    'logs out users and redirects them to the home page'
    session.clear()
    return redirect(url_for('frontend.home'))

@bp.route('/forgot_id')
def forgot_id():
    'allows user to ask for their id by inputting their email/username in order to verify their identity'
    return render_template('forgot_id.html')

#---------------------------------Member and Staff Profiles---------------------------------
@bp.route('/member_profile')
def member_profile():
    'defines and implements what can be seen in the staff/members account'
    return render_template('member_profile')

@bp.route('/staff_profile')
def staff_profile():
    'implements overdue books list and displays them on the staff profile, also displays list of members and allows for editing'
    return render_template('staff_profile.html')

#---------------------------------Book Listing Pages---------------------------------
@bp.route('/listing_member')
def listing_member():
    'displays book litings to members:checkout, rent status, description, etc'
    return render_template('listing_member.html')

@bp.route('/listing_staff')
def listing_staff():
    'allows staff to edit book information and view rent/overdue status'
    return render_template('listing_staff.html')

#---------------------------------Other Pages/UI---------------------------------
@bp.route('/about')
def about_us():
    'displays library information'
    return render_template('about_us.html')

@bp.route('/favorites')
def favorites():
    'displays users favorited books'
    return render_template('favorites.html')

@bp.route('/search')
def search():
    'search page with sort by features and displays shorter book listing with image, title, and brief description of book'
    return render_template('search.html')