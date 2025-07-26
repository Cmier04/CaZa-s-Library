# Define and implement test cases for project here
import pytest
from main import LibrarySystem

@pytest.fixture
def library():
    return LibrarySystem("books.json")

# --- Functionality Test Case ---
def test_borrow_book_success(library):
    result = library.borrow_book("M001", "B001")
    assert result["success"] is True
    assert library.books["B001"]["status"] == "borrowed"

# --- Boundary Test Case ---
def test_borrow_book_unavailable(library):
    library.books["B001"]["status"] = "borrowed"
    result = library.borrow_book("M001", "B001")
    assert result["success"] is False
    assert result["message"] == "Book unavailable"

# --- Error Handling Test Case ---
def test_borrow_invalid_member(library):
    result = library.borrow_book("INVALID", "B001")
    assert result["success"] is False
    assert result["message"] == "Invalid member"
