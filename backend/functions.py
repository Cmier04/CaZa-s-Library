# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 20, 2025
# Project Name: CaZa's Library
# File Purpose: Defines functions needed for program

# --------------------------List of TODO's-------------------------------
    # TODO: ensure file information is correct and json files have information to read from
    # TODO: test
# NOTE: might need to add more functions to verify login information (may also be defined within the manager class)

# --------------------------Changes Made---------------------------------
  # Comment changes made to this file here, keeps track of changes if commit contains multiple files.'
  #..

import json
import os

user_file = 'users.json'
book_file = 'books.json'

def load_users():
    # load users from users.json
    if not os.path.exists(user_file):
        return {"There are no users"}
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
