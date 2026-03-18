"""Personal Library Manager
Goal:
Build a Python program to manage a small personal library, practicing:

String manipulation

Lists, tuples, sets, dictionaries

Conditionals (if/elif/else)

Loops (while, for, nested loops)

Functions (with parameters, return values, and optional arguments)

Exit confirmation

📊 Learning Objectives
Grouping code into functions for better readability.

Passing and returning data from functions.

Practicing parameters and arguments.

Working with multiple data structures in one program.

Using loops and nested loops inside functions.

Exit confirmation logic.

📌 Features to Implement
Add a Book – Store title, author, year, and genres.

View All Books – Display every book in the library.

Search Books by Title – Case-insensitive match.

Show Statistics – Number of books, unique authors, genres count.

Exit – Ask for confirmation before quitting.

📂 Data Structures
Book stored as a dictionary:        {

                  "title": "The Hobbit",

                  "author": "J.R.R. Tolkien",

 
                  "year": 1937,

                 "genres": ("fantasy", "adventure")

      }
List → stores all books.

Set → stores all unique authors.

Set → stores all unique genres.

📜 Menu System
The program should output 5 options to the user:

               1. Add a Book
               2. View All Books
               3. Search Books by Title
               4. Show Statistics
               5. Exit
Then, it has to:

Ask the user to enter the number of the action it wishes to carry out.

If the number is not in the range 1 to 5, send and error message and ask for a correct option and keep looping this action until the user chooses an option in the list.

If the number is in the range 1 to 5 redirect them to the correct block of code.

🛠 Functions to Create
add_book(library, authors, genres)

Ask for book details.

Format title & author using .title().

Validate year as a number.

Split genres by commas and store as a tuple.

Add to library list.

Update authors and genres sets.

view_books(library)

Loop and print all books in a formatted style.

search_books(library, search_title)

Convert search query to lowercase.

Check all books for a match.

Print details if found; otherwise, "No book found."

show_statistics(library, authors, genres)

Print total number of books.

Print all unique authors.

Nested loop to count how many books per genre.

confirm_exit()

Ask "Are you sure you want to exit? (yes/no)".

Return True if yes, otherwise False.
"""

library = []
authors = set()
genres = set()

def add_book(library,authors,genres):
    print(f"\n----- Adding Book -----")
    title = input("Enter book title: ").strip().title()
    author = input("Enter book author: ").strip().title()

    while True:
        year_input = input("Enter publication year: ").strip()
        if not year_input.isdigit():
            print("Invalid input. Please enter number only.")
            continue
        year = int(year_input)
        break
    genres_input = input("Enter book genres : ").strip().title()
    cleaned_genres_list = [g.strip() for g in genres_input.lower().split(',') if g.strip()]
    genres_tuple = tuple(cleaned_genres_list)
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genres': genres_tuple
    }
    library.append(book)
    authors.add(author)
    for g in genres_tuple:
        genres.add(g) # It can be more then one genre for a book, so we need to add all genres to the set
    print(f"\nBook '{title}' by '{author}' added successfully!")

def view_books(library):
    print(f"\n----- Library Books -----")
    if not library:
        print("No books in the library.")
        return
    for i,book in enumerate(library): # Here First I used .items() method, but it is not working
        # because library is a list of dictionaries, not a dictionary. So I changed it to enumerate() method to get the index and the book dictionary.
        print(f"{i+1}. '{book['title']}' by {book['author']} ({book['year']}) - Genres: {', '.join(book['genres'])}")

def search_books(library, search_title):
    print(f"\n----- Search Results -----")
    search_query = search_title.lower()
    found = False
    for book in library:
        if search_query in book['title'].lower():
            print(f"'{book['title']}' by {book['author']} ({book['year']}) - Genres: {', '.join(book['genres'])}")
            found = True
    if not found:
        print(f"No books found with title '{search_title}'.")

def show_statistics(library, authors, genres):
    print(f"\n----- Library Statistics -----")
    total_books = len(library)
    unique_authors = len(authors)
    unique_genres = len(genres)
    print(f"Total books: {total_books}")
    print(f"Unique genres: {unique_genres}")
    print(f"Unique authors ({len(authors)}):")
    for author in sorted(authors):
        print(f"  - {author}")


    for genre in sorted(genres):
        count = 0
        for book in library:
            if genre in book['genres']:
                count += 1
        print(f"Genre '{genre}': {count} book(s)")

def confirm_exit():
    answer = input("Are you sure you want to exit? (y/n): ").strip().lower()
    if answer in ('y', 'yes'):
        print("Exiting the program. Goodbye!")
        return True
    else:
        print("Exit cancelled. Returning to the menu.")
        return False

while True:
    print("\n=============================")
    print("   Personal Library Manager")
    print("=============================")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Books by Title")
    print("4. Show Statistics")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip()
    if choice == '1':
        add_book(library, authors, genres)
    elif choice == '2':
        view_books(library)
    elif choice == '3':
        search_title = input("Enter book title to search: ").strip()
        search_books(library, search_title)
    elif choice == '4':
        show_statistics(library, authors, genres)
    elif choice == '5':
        if confirm_exit():
            break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")