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

  def search(self): # Returns string message, if search fails, and a list of dictionaries, if it succeeds
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
    
  def rentBook(self):
    # Changes rent status of book, assigns rent period to Member
    # Limit of rented books at a time is 2 books
    # Check how many rented books Member has, and if they have 2 books currently, reject their request
    pass

  def returnBook(self):
    # Change status of book, delete book reference from attribute
    pass

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
    pass

class Staff:
  # Attributes information to staff
  def __init__(self, username, id):
    self._username = username
    self._id = id
  
  def _editListing(self):
    # Edit books listing
    # books_listing = load_books()
    pass
    
  def _addBook(self, title, author, isbn, rent_status, overdue_status):
    # Add a Book to the books.json
    # book1 = Book(title, author, isbn, rent_status, overdue_status)
    # listing = load_books()
    pass
    
  def _removeBook(self, title, author, isbn):
    # Remove a Book from the books.json
    # listing = load_books()
    pass
    
  def _addMember(self, name, member_id, email):
    # Add a member to "users" list in the dictionary found in users.json
    # users_listing = load_users()
    # member1 = Member(name, member_id, email)
    pass
    
  def _removeMember(self):
    # Remove a member from the "users" list in users.json
    # users_listing = load_users()
    pass
    
  def search(self):
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
  def __init__(self, user_data):
    pass

  def _sendOverdueNotice(self, title, isbn):
    # Display overdue notice and which books are overdue to user, display title and isbn of book(s)
    pass
  
  def loginUser(self, role, name, id):
    # Login user based on name and id, as well as role
    # users_listing = load_users()
    pass
    
  def _assignMemberId(self, name, email): # Return/display member id
    # Assign a member id listed from "unused_ids" in the users.json
    # then delete the currently being used id from the list
    # users_listing = load_users()
    pass

  def _checkMemberId(self, member_id): # Return/display whether member id is valid (bool value)
    # users_listing = load_users()
    pass
    
  def _checkStaffId(self, id): # Return/display whether staff id is valid (bool value)
    #if not os.path.exists('staff.json'):
        #return False
    #with open ('staff.json', 'r') as f:
        #staff_listing = json.load(f)
    pass
