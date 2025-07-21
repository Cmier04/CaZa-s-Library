# Names: Alexia Macias, Christine Mier, Allen Le, Zhi Xuan Chong
# Date Started: July 20, 2025
# Project Name: CaZa's Library
# File Purpose: Define and implement classes used in driver program

class Book:
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
  def __init__(self, name, member_id, email):
    self._name = name,

class Staff:
  def __init__(self, username, id):
    self._username = username,

# combined the Staff/Member manager class into Manager
class Manager:
  #TODO: define functions for member class
