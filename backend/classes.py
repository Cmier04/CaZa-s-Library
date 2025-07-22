# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 20, 2025
# Project Name: CaZa's Library
# File Purpose: Define and implement classes used in driver program

"--------------------------List of TODO's-------------------------------"
  # TODO: complete definition of Member class and check if "user" class is necessary to handle guest interaction
  # TODO: complete definition of Staff class; make any changes necessary
  # TODO: define functions for member class
  # TODO: revise and edit docstrings to accurately describe classes

"--------------------------Changes Made---------------------------------"
 ' Comment changes made to this file here, keeps track of changes if commit contains multiple files.'
  #..

class Book:
  'Handles all book information and retrieves title, author, isbn from book.json'
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

  def editAccount(self, name, email):
    self._name = name
    self._email = email

  def search(self):
    # Searches the book database via title, author, ISBN
    pass

  def viewListing(self):
    # Displays info on all available books
    pass

class Staff:
  'Attributes information to staff'
  def __init__(self, username, id):
    self._username = username
    self._id = id

# combined the Staff/Member manager class into Manager, rename if necessary
class Manager:
  'Manages all staff and member information while managing book returns and overdue notices'
