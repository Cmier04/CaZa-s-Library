# Names: Alexia Macias, Christine Mier, Zhi Xuan Chong, Allen Le
# Start Date: July 18, 2025
# Project Name: CaZa's Library
# File Purpose: This is the main python file that manages all backend and frontend development


"--------------------------NOTE-------------------------------"
  # if crash, redefine create_app to not use blueprints

"--------------------------Changes Made---------------------------------"
  # Comment changes made to this file here, keeps track of changes if commit contains multiple files.
  #..

from backend._init_ import create_app

app = create_app

if __name__ == '__main__':
    app.run(debug=True)