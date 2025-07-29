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
from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from backend.functions import load_users, save_users, load_staff, load_books, save_books
from backend.classes import Book, Member, Staff, Manager
from datetime import datetime, date, timedelta

bp = Blueprint('frontend', __name__, template_folder='../frontend/templates', static_folder='../frontend/static', static_url_path='/frontend_static')

user_data = load_users()
staff_data = load_staff()
manager = Manager(user_data)

#---------------------------------User Home Pages---------------------------------
@bp.route('/')
def home():
   return render_template('home.html')

@bp.route('/home_members')
def home_members():
    'members home page which gets rid of log in and sign up feature, replacing them with logout'
    if session.get('user_type') != 'member':
        return redirect(url_for('frontend.login'))
    
    username = session.get('username')
    users = load_users().get('users', [])
    user_data = next((u for u in users if u['name'] == username), None)
    if not user_data:
        return redirect(url_for('frontend.login'))

    member = Member(user_data['name'], user_data['member_id'], user_data['email'])
    member.rented = user_data.get('rented', {})
    
    manager = Manager(user_data=None)
    overdue_books = manager.getOverdueBooks(member)

    #TODO: Fix message popup, members are not displayed their id's after creating their account
    member_id_popup = session.pop('member_id_popup', None)
    return render_template('home_members.html', member_id_popup=member_id_popup)

@bp.route('/home_staff')
def home_staff():
    'staff home page which gives them a summary of overdue books'
    if session.get('user_type') != 'staff':
        return redirect(url_for('frontend.login'))
    
    username = session.get('username')
    staff_user = load_staff().get('staff_users', [])
    staff_data = next((u for u in staff_user if u['name'] == username), None)
    if not staff_data:
        return redirect(url_for('frontend.login'))

    staff = Staff(staff_data['name'], staff_data['staff_id'])

    users = load_users().get('users', [])
    total_overdue = 0
    manager = Manager(user_data=None)

    for user in users:
        if 'name' in user and 'member_id' in user:
            member = Member(user['name'], user['member_id'], user['email'])
            member.rented = user.get('rented', {})
            overdue_books = manager.getOverdueBooks(member)
            total_overdue += len(overdue_books)
        else:
            print("Skipping malformed entry:", user)

    return render_template('home_staff.html', username=username, total_overdue=total_overdue)

#---------------------------------User Log in and Sign up---------------------------------
@bp.route('/apply', methods=['GET', 'POST'])
def apply():
    'implements the functionality of the member application page'
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        global user_data
        manager = Manager(user_data)
        result = manager.add_new_member(name, email)

        if result.startswith("New member added"):
            member_id = result.split(":")[-1].strip()
            session['user_type'] = 'member'
            session['username'] = name
            session['member_id'] = member_id
            session['email'] = email
            session['member_id_popup'] = member_id

            user_data = manager.user_data

            flash(f"Welcome {name.strip()}! You are now being redirected to your home page...", 'success')
            return render_template('member_application.html', redirect_to_homepage=True)

        elif result == "Failed to add new member: User already exists.":
            flash(f"{result} Redirecting to login..", 'error')
            return render_template('member_application.html', redirect_to_login=True)

        flash(result, 'error')
        return redirect(url_for('frontend.apply'))

    return render_template('member_application.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    'implements functions of the member/staff login page'
    if request.method == 'POST':
        username = request.form.get('username')
        user_id = request.form.get('memberid')
        staff_id = request.form.get('memberid')
        role = request.form.get('role')

        if not role or not username or (role == 'member' and not user_id) or (role == 'staff' and not staff_id):
            error = "All fields are required."
            return render_template('login.html', error=error)
        
        manager = Manager(load_users())
        user_role = user_id if role == 'member' else staff_id
        result = manager.loginUser(role, username, user_role)

        if result == 'Member Login succeeded.':
            session['user_type'] = 'member'
            session['username'] = username
            session['member_id'] = user_id
            return redirect(url_for('frontend.home_members'))

        elif result == "Staff Login succeeded.":
            print(result)
            session['user_type'] = 'staff'
            session['username'] = username
            session['staff_id'] = staff_id
            print("redirecting to:", url_for('frontend.home_staff'))
            return redirect(url_for('frontend.home_staff'))

        else:
            error = "Invalid username or ID. Please try again or choose Forgot Member ID."
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
@bp.route('/member_profile', methods=['GET', 'POST'])
def member_profile():
    'defines and implements what can be seen in the staff/members account'
    if not session.get('user_type') or session['user_type'] != 'member':
        return redirect(url_for('frontend.login'))

    username = session.get('username')
    member_id = session.get('member_id')

    manager = Manager()
    users = manager.user_data.get('users', [])

    user_data = next((u for u in users if u['name'] == username and u['member_id'] == member_id), None)

    if not user_data:
        return redirect(url_for('frontend.login'))

    member = Member(user_data['name'], user_data['member_id'], user_data['email'])

    #TODO: Fix Error and Success Messages not displaying !!!!!
    if request.method == 'POST':
        new_name = request.form.get('edit_name')
        new_email = request.form.get('edit_email')

        member._editAccount(new_name=new_name, new_email=new_email)
        success = manager.update_member_info(member)
        if success:
            session['username'] = member._name
            session['email'] = member._email
            flash("Profile updated successfully.", "success")
            return redirect(url_for('frontend.member_profile'))
        else:
            flash("Error updating profile", 'error')
        return redirect(url_for('frontend.member_profile'))

    member.favorites = [
        Book (
        fav['title'],
        fav['author'],
        fav['isbn'],
        fav.get('rent_status', 'open'),
        fav.get('overdue_status', 'on time')
    ) for fav in user_data.get('favorites', [])
    ]
    rented_raw = user_data.get('rented', {})
    member.rented = rented_raw

    manager = Manager(user_data=None)
    overdue_books = manager.getOverdueBooks(member)

    return render_template(
        'member_profile.html',
        name=member._name,
        member_id=member._member_id,
        email=member._email,
        favorites=member.favorites,
        rented_books=member.rented,
        overdue_books=overdue_books
    )

@bp.route('/staff_profile', methods=['GET', 'POST'])
def staff_profile():
    'implements overdue books list and displays them on the staff profile, also displays list of members and allows for editing'
    if not session.get('user_type') or session['user_type'] != 'staff':
        return redirect(url_for('frontend.login'))
    
    username = session.get('username')
    staff_id = session.get('staff_id')

    staff_data = next((s for s in load_staff().get('staff_users', []) if s['staff_id'] == staff_id), None)

    if not staff_data:
        flash("Staff not found", "error")
        return redirect(url_for('frontend.login'))

    staff = Staff(staff_data['name'], staff_data['staff_id'])
    manager = Manager()

    if request.method == 'POST':
        member_id = request.form.get('member_id')
        new_name = request.form.get('edit_name')
        new_email = request.form.get('edit_email')

        user_data = load_users()
        members_list = user_data.get('users', [])

        print("member_id form from ", member_id)
        print("all member_ids", [u['member_id'] for u in members_list])
        member_data = next((u for u in members_list if u['member_id'] == member_id), None)

        if not member_data:
            flash("Member not found.", "error")
            print("user is not in user_data")
        else:
            print('enters else statement')
            member = Member(member_data['name'], member_data['member_id'], member_data['email'])
            member.rented = member_data.get('rented', [])

            member._editAccount(new_name, new_email)

            success = manager.update_member_info(member)
            if success:
                flash("Profile updated successfully.", "success")
            else:
                flash("Error updating profile", 'error')
        return redirect(url_for('frontend.staff_profile'))

    members_list = load_users().get('users', [])
    overdue_books = []
    for user in members_list:
        member = Member(user['name'], user['member_id'], user['email'])
        member.rented = user.get('rented', {})
        overdue_books.extend(manager.getOverdueBooks(member))

    return render_template(
        'staff_profile.html',
        members_list=members_list,
        name=staff._username,
        staff_id=staff._staff_id,
        overdue_books = overdue_books
    )

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

@bp.route('/search', methods=['GET', 'POST'])
def search():
    'search page with sort by features and displays shorter book listing with image, title, and brief description of book'
    if session.get('user_type') not in ('member', 'staff'):
        return redirect(url_for('frontend.login'))

    username = session.get('username')
    user_type = session.get('user_type')

    if not username or not user_type:
        return redirect(url_for('frontend.login'))

    #load user and staff data
    user = None
    if user_type == 'member':
        users = load_users().get('users', [])
        user_data = next((u for u in users if u['name'] == username), None)
        if not user_data:
            return redirect(url_for('frontend.login'))
        user = Member(user_data['name'], user_data['member_id'], user_data['email'])
    elif user_type == 'staff':
        staff_list = load_staff().get('staff', [])
        staff_data = next((s for s in staff_list if s['name'] == username), None)
        if not staff_data:
            return redirect(url_for('frontend.login'))
        user = Staff(staff_data['name'], staff_data['staff_id'])
    else:
        return redirect(url_for('frontend.login'))

    title = author = isbn = ""
    books = []
    message = None
    sort_key = request.args.get('sort')

    books_data = load_books()
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        isbn = request.form.get('isbn', '').strip()

        result = user.search(title=title, author=author, isbn=isbn)

        if isinstance(result, str):
            message = result
            books = []
        else:
            books = result
        
        exact_match = None
        if isbn:
            exact_match = next((b for b in books if b['isbn'].lower() == isbn.lower()), None)
        if not exact_match and title:
            exact_match = next((b for b in books if b['title'].lower() == title.lower()), None)
        if sort_key in ('title', 'author', 'genre'):
            books.sort(key=lambda b: b.get(sort_key, '').lower())
      
    else:
        books = load_books()
        exact_match = None
      
    return render_template(
        'search.html',
        books=books,
        exact_match=exact_match,
        message=message,
        title=title,
        author=author,
        isbn=isbn,
        sort_key=sort_key
        )
