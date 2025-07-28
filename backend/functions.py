# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 20, 2025
# Project Name: CaZa's Library
# File Purpose: Defines functions needed for program

import json
import os

user_file = 'users.json'
book_file = 'books.json'
staff_file = 'staff.json'

def load_users():
    # load users from users.json
    if not os.path.exists(user_file):
        return {"error": "There are no users"}
    with open(user_file, 'r') as f:
        return json.load(f)

def save_users(user_data):
    # saves the user_data to users.json
    with open(user_file, 'w') as f:
        json.dump(user_data, f, indent=4)

def load_books():
    # loads books from books.json
    if not os.path.exists(book_file):
        return{}
    with open (book_file, 'r') as f:
        return json.load(f)

def save_books(book_data):
    with open(book_file, 'w') as f:
        json.dump(book_data, f, indent=4)

def load_staff():
    #loads staff from staff.json
    if not os.path.exists(staff_file):
        return{"error": "There are no staff"}
    with open (staff_file, 'r') as f:
        return json.load(f)
