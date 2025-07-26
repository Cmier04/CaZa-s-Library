# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 20, 2025
# Project Name: CaZa's Library
# File Purpose: Define and implement classes used in driver program

#--------------------------List of TODO's-------------------------------
  # TODO: complete definition of Member class and check if "user" class is necessary to handle guest interaction
  # TODO: complete definition of Staff class; make any changes necessary
  # TODO: define functions for member class
  # TODO: revise and edit docstrings to accurately describe classes

#--------------------------Changes Made---------------------------------
 # Comment changes made to this file here, keeps track of changes if commit contains multiple files.
  #..

from backend.functions import *

from datetime import date, timedelta

class Book:
  # Handles all book information and retrieves title, author, isbn from book.json
  def __init__(self, title, author, isbn, rent_status, overdue_status):
    self.__title = title
    self.author = author
    self.isbn = isbn
    self.rent_status = rent_status
    self.overdue_status = overdue_status

  def getTitle(self):
    return self.__title

  def setTitle(self, title):
    self.__title = title

class Member:
  # Defines what attributes are associated with being a member
  def __init__(self, name, member_id, email):
    self._name = name
    self._member_id = member_id
    self._email = email
    self.favorites = []
    self.rented = {} # Dictionary has book:rent_due_date key:value pairs

  def _editAccount(self, name, email):
    self._name = name
    self._email = email

  def search(self, title, author, ISBN): # Returns string message, if search fails, and a list of dictionaries, if it succeeds
    # Searches the book database via title, author, ISBN
    books_load = load_books() # Returns a list of dictionaries
    list_of_books = []
    for item in books_load:
      if ((title != "") and (title == item["title"]) and (author == "") and (ISBN == "")):
        list_of_books.append(item) # Dictionary containing info on book found
      elif ((author != "") and (author == item["author"]) and (title == "") and (ISBN == "")):
        list_of_books.append(item)
      elif ((ISBN != "") and (ISBN == item["isbn"]) and (author == "") and (title == "")):
        list_of_books.append(item)

    if (len(list_of_books) == 0):
      return "No books found."
    else:
      return list_of_books

  def viewListing(self):
    # Displays info on all available books
    books_load = load_books()
    return books_load

  def _viewFavorites(self):
    # Displays info on all favorited books
    return self.favorites
    
  def rentBook(self, title, author, isbn, rent_status, overdue_status, date): # date is a string of "YYYY-MM-DD"
    # Changes rent status of book, assigns rent period to Member
    # Limit of rented books at a time is 2 books
    # Check how many rented books Member has, and if they have 2 books currently, reject their request
    if (len(self.rented == 2)):
      return "Rent book request rejected. Member is currently renting 2 books, which is the limit at one point in time."
    elif (rent_status == "closed"):
      return "Rent book request rejected. Book is currently being rented and unavailable to other Members."
    else:
      books_load = load_books()
      copy_load = books_load
      rent_status = "closed"
      new_book = Book(title, author, isbn, rent_status, overdue_status)

      # Reference for finding the rent_date with first_date and date and timedelta objects: https://www.dataquest.io/blog/python-datetime/
      first_date = date.fromisoformat(date)
      time_period = 14
      rent_date = first_date + timedelta(days=time_period)
      self.rented[isbn] = rent_date.isoformat()
      
      index = 0
      for item in copy_load:
        if ((title == item["title"]) and (author == item["author"]) and (isbn == item["isbn"])):
          books_load[index]["rent_status"] = "closed"
        else:
          index += 1
      save_books(books_load)
      return "Book has been successfully rented. Please return it in 14 days."

  def returnBook(self, title, author, isbn):
    # Change status of book, delete book reference from attribute
    books_load = load_books()
    copy_load = books_load
    rented_books = self.rented.keys() # Returns a list of keys/Book()'s
    for book in rented_books:
      if ((title == book.getTitle()) and (author == book.author) and (isbn == book.isbn)):
        del self.rented[book]
    index = 0
    for item in copy_load:
      if ((title == item["title"]) and (author == item["author"]) and (isbn == item["isbn"])):
        books_load[index]["rent_status"] = "open"
        books_load[index]["overdue_status"] = "on time"
      else:
        index += 1
    save_books(books_load)

  def addFavorite(self, title, author, isbn, rent_status, overdue_status):
    # Add book to favorites attribute
    fav_book = Book(title, author, isbn, rent_status, overdue_status)
    self.favorites.append(fav_book)
  
  def removeFavorite(self, title, author, isbn):
    # Remove book from favorites
    fav_list = self.favorites
    for item in fav_list:
      if ((item.getTitle() == title) and (item.author == author) (item.isbn == isbn)):
        self.favorites.remove(item)
  
  def changeBookStatus(self):
    # Check rented books and change their status accordingly
    # call Manager's function sendOverdueNotice, if there are any overdue books
    # Reference for date object and functions: https://www.dataquest.io/blog/python-datetime/
    pass

class Staff:
  # Attributes information to staff
  def __init__(self, username, id):
    self._username = username
    self._id = id
  
  def _editListing(self, new_title, author, isbn):
    # Edit books listing
    books_listing = load_books()
    copy_listing = books_listing
    index = 0
    for item in copy_listing:
      if ((author == item["author"]) and (isbn == item["isbn"])):
        books_listing[index]["title"] = new_title
      else:
        index += 1
    save_books(books_listing)
    
  def _addBook(self, title, author, isbn, genre, description):
    # Add a Book to the books.json
    book1 = {"title":title, 
             "author": author, 
             "isbn": isbn, 
             "rent_status": "open", 
             "overdue_status": "on time",
             "genre": genre,
             "description": description}
    listing = load_books()
    listing.append(book1)
    save_books(listing)
    
  def _removeBook(self, title, author, isbn): # Returns a boolean that confirms whether the process succeeded or not
    # Remove a Book from the books.json
    listing = load_books()
    copy = listing
    did_succeed = False
    for item in copy:
      if ((title != "") and (title == item["title"]) and (author == item["author"]) and (isbn == item["isbn"])):
        listing.remove(item)
        save_books(listing)
        did_succeed = True
    return did_succeed
    
  def _addMember(self, name, member_id, email):
    # Add a member to "users" list in the dictionary found in users.json
    users_listing = load_users() # Returns a dictionary with two keys
    member1 = {"name": name, 
               "member_id": member_id, 
               "email": email}
    users_listing["users"].append(member1)
    save_users(users_listing)
    
  def _removeMember(self, member_id): # Returns a boolean that confirms whether the process succeeded or not
    # Remove a member from the "users" list in users.json
    users_listing = load_users()
    copy = users_listing["users"] # Returns a list of dictionaries
    did_succeed = False
    for item in copy:
      if (member_id == item["member_id"]):
        users_listing["users"].remove(item)
        save_users(users_listing)
        did_succeed = True
    return did_succeed
    
  def search(self, title, author, ISBN):
    # Search for a book in the books.json via title, author, or ISBN
    books_load = load_books() # Returns a list of dictionaries
    list_of_books = []
    for item in books_load:
      if ((title != "") and (title == item["title"]) and (author == "") and (ISBN == "")):
        list_of_books.append(item) # Dictionary containing info on book found
      elif ((author != "") and (author == item["author"]) and (title == "") and (ISBN == "")):
        list_of_books.append(item)
      elif ((ISBN != "") and (ISBN == item["isbn"]) and (author == "") and (title == "")):
        list_of_books.append(item)

    if (len(list_of_books) == 0):
      return "No books found."
    else:
      return list_of_books
    
  def editBookTitle(self, new_title, current_isbn): # Returns string message indicating whether the function succeeded
    # First, search for book via ISBN, and then edit title of the book
    books_listing = load_books()
    copy_listing = books_listing
    index = 0
    is_true = False
    for item in copy_listing:
      if ((ISBN != "") and (ISBN == item["isbn"])):
        books_listing.remove(item)
        item["title"] = new_title
        books_listing.insert(index, item)
        save_books(books_listing)
        is_true = True
      else:
        index += 1

    if (is_true):
      return "Book title edited."
    else:
      return "Book title editing failed."

# combined the Staff/Member manager class into Manager, rename if necessary
class Manager:
  # Manages all staff and member information while managing book returns and overdue notices
  def __init__(self):
    pass

  def getOverdueBooks(self, member): # Checks the overdue status of books and adds them to dict
    overdue = []
    today = datetime.today().date()
    for book, due_date_str in member.rented.items():
      due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
      if due_date < today:
        overdue.append(book)
    return overdue
    
  def _sendOverdueNotice(self, title, isbn):
    # Display overdue notice and which book is overdue to user, display title and isbn of book
    return f"Notice to Member: The book titled {title} and with the ISBN: {isbn} is now overdue."
  
  def loginUser(self, role, name, id):
    # Login user based on name and id, as well as role
    users_listing = load_users()
    staff_listing = load_staff() # Returns list of dictionaries with "name" and "staff_id" keys
    if ((role == "staff") and self._checkStaffId(id)):
      is_true = False
      for item in staff_listing:
        if ((name == item["name"]) and id == item["staff_id"]):
          is_true = True
      if (is_true):
        return "Staff Login succeeded."
      else:
        return "Login denied."
    elif ((role == "member") and self._checkMemberId(id)):
      users = users_listing["users"]
      is_member = False
      for item in users:
        if ((name == item["name"]) and (id == item["member_id"])):
          is_member = True
      if (is_member):
        return "Member Login succeeded."
      else:
        return "Login denied."
    else:
      return "Login denied."

      
   def add_new_member(self, name, email): # Add a new member to user.json file
      users_listing = load_users()
      member_id = self._assignMemberId(users_listing)
      if not member_id == -1:
        return "Failed to add new member: Library is at capacity."
      for user in users_listing["users"]:
        if user["name"] == name and user["email"] == email:
          return "Failed to add new member: User already exists."
      new_member = {
        "name": name,
        "member_id": member_id,
        "email": email,
        "favorites": [],
        "rented": {}
      }
      users_listing["users"].append(new_member)
      save_users(users_listing)
      return f"New member added successfully. Member ID: {member_id}"
    
  def _assignMemberId(self): # Return member id, if available, and return -1 when not available
    # Assign a member id listed from "unused_ids" in the users.json
    # then delete the currently being used id from the list
    users_listing = load_users()
    unused_list = users_listing["unused_ids"]
    if (len(unused_list) > 0):
      member_id = unused_list[0]
      unused_list.remove(member_id)
      users_listing["unused_ids"] = unused_list
      save_users(users_listing)
      return member_id
    else:
      return -1

  def _checkMemberId(self, member_id): # Return/display whether member id is valid (bool value)
    users_listing = load_users()
    users = users_listing["users"]
    for item in users:
      if (member_id == item["member_id"]):
        return True
    return False
    
  def _checkStaffId(self, id): # Return/display whether staff id is valid (bool value)
    staff = load_staff()
    for item in staff:
      if (id == item["staff_id"]):
        return True
    return False