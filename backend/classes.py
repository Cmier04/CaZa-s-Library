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
  'Defines what attributes are associated with being a member'
  def __init__(self, name, member_id, email):
    self._name = name
    self._member_id = member_id
    self._email = email
    self.favorites = []
    self.rented = {} # Dictionary has book:rent_due_date key:value pairs

  def _editAccount(self, name, email):
    self._name = name
    self._email = email

  def search(self):
    # Searches the book database via title, author, ISBN
    pass

  def viewListing(self):
    # Displays info on all available books
    pass

  def _viewFavorites(self):
    # Displays info on all favorited books
    pass
    
  def rentBook(self):
    # Changes rent status of book, assigns rent period to Member
    # Limit of rented books at a time is 2 books
    # Check how many rented books Member has, and if they have 2 books currently, reject their request
    pass

  def returnBook(self):
    # Change status of book, delete book reference from attribute
    pass

  def addFavorite(self):
    # Add book to favorites attribute
    pass
  
  def removeFavorite(self):
    # Remove book from favorites
    pass
  
  def changeBookStatus(self):
    # Check rented books and change their status accordingly
    # call Manager's function sendOverdueNotice, if there are any overdue books
    pass

class Staff:
  'Attributes information to staff'
  def __init__(self, username, id):
    self._username = username
    self._id = id
  
  def _editListing(self):
    # Edit books listing
    pass
    
  def _addBook(self, title, author, isbn, rent_status, overdue_status):
    # Add a Book to the books.json
    pass
    
  def _removeBook(self, title, author, isbn):
    # Remove a Book from the books.json
    pass
    
  def _addMember(self):
    # Add a member to "users" list in the dictionary found in users.json
    pass
    
  def _removeMember(self):
    # Remove a member from the "users" list in users.json
    pass
    
  def search(self):
    # Search for a book in the books.json via title, author, or ISBN
    pass
    
  def editBookTitle(self, title, isbn):
    # First, search for book via ISBN, and then edit title of the book
    pass

# combined the Staff/Member manager class into Manager, rename if necessary
class Manager:
  # Manages all staff and member information while managing book returns and overdue notices
  def __init__(self):
    pass

  def _sendOverdueNotice(self, title, isbn):
    # Display overdue notice and which books are overdue to user, display title and isbn of book(s)
    pass
  
  def loginUser(self, name, id):
    # Login user based on name and id
    pass
    
  def _assignMemberId(self, name, email): # Return/display member id
    # Assign a member id listed from "unused_ids" in the users.json
    # then delete the currently being used id from the list
    pass

  def _checkMemberId(self, member_id): # Return/display whether member id is valid (bool value)
    pass
    
  def _checkStaffId(self, id): # Return/display whether staff id is valid (bool value)
    pass
    
  def logOut(self):
    # Logout the user
    pass
