# %% [markdown]
# # Library Management System
# 
# This notebook implements a Library Management System that allows users to:
# - Add books to the library
# - Search for books
# - Borrow books
# - Return books
# 
# The system uses Python lists and dictionaries to store and manage book and user information.

# %%
# Import necessary libraries
import datetime

# %% [markdown]
# ## Data Structures
# 
# We'll use the following data structures to store library information:

# %%
# List of books in the library
library_books = []

# Dictionary to store borrowed books
borrowed_books = {}

# List of users
users = []

# %% [markdown]
# ## Core Functions

# %%
# Function to add a new book to the library
def add_book(book_id, title, author):
    """
    Adds a new book to the library.
    
    Parameters:
    - book_id (str): Unique identifier for the book
    - title (str): Title of the book
    - author (str): Author of the book
    """
    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    library_books.append(book)  # Add the book to the library_books list
    print(f"Book '{title}' by {author} added to the library.")

# %%
# Function to search for a book
def search_book(title):
    """
    Searches for books in the library that match the given title (case-insensitive).
    
    Parameters:
    - title (str): Title or part of title to search for
    """
    # Search for books in the library that match the given title (case-insensitive)
    found_books = [
        book for book in library_books
        if title.lower() in book["title"].lower()
    ]
    
    if found_books:
        # Iterate through the found books and print their details
        for book in found_books:
            status = "Available" if book["available"] else "Borrowed"
            print(
                f"ID: {book['book_id']}, Title: {book['title']}, "
                f"Author: {book['author']}, Status: {status}"
            )
    else:
        print("No books found with that title.")

# %%
# Function to borrow a book
def borrow_book(user, book_id):
    """
    Allows a user to borrow a book if it's available.
    
    Parameters:
    - user (str): Name of the user borrowing the book
    - book_id (str): ID of the book to borrow
    """
    # Check if the specified book is available and mark it as borrowed
    for book in library_books:
        if book["book_id"] == book_id and book["available"]:
            book["available"] = False  # Mark the book as unavailable
            borrowed_books[book_id] = {
                "user": user,
                "borrow_date": datetime.date.today()  # Record the borrow date
            }
            print(f"Book '{book['title']}' borrowed by {user}.")
            return
    
    print("Book not available or does not exist.")

# %%
# Function to return a book
def return_book(book_id):
    """
    Returns a borrowed book to the library.
    
    Parameters:
    - book_id (str): ID of the book being returned
    """
    # Check if the book is in borrowed_books and mark it as available
    if book_id in borrowed_books:
        for book in library_books:
            if book["book_id"] == book_id:
                book["available"] = True  # Mark the book as available
                borrowed_books.pop(book_id)  # Remove the book from borrowed_books
                print(f"Book '{book['title']}' returned.")
                return
    print("Book not found in borrowed books.")

# %% [markdown]
# ## Main Program Loop

# %%
def main():
    """
    Main function that runs the library management system interface.
    """
    # Start an infinite loop for the library management system
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        # Handle user choices for library operations
        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(book_id, title, author)  # Call function to add a new book
            
        elif choice == '2':
            title = input("Enter book title to search: ")
            search_book(title)  # Call function to search for a book
            
        elif choice == '3':
            user = input("Enter your name: ")
            book_id = input("Enter book ID to borrow: ")
            borrow_book(user, book_id)  # Call function to borrow a book
            
        elif choice == '4':
            book_id = input("Enter book ID to return: ")
            return_book(book_id)  # Call function to return a borrowed book
            
        elif choice == '5':
            print("Exiting the system. Goodbye!")  # Exit message
            break  # Exit the loop and end the program
            
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# %% [markdown]
# ## Running the System
# 
# Execute the following cell to start the Library Management System:

# %%
# Start the Library Management System
if __name__ == "__main__":
    main()