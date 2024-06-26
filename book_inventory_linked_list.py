# Lesson 3: Assignment | Linked List

# Implementing a BookInventory Linked List in Python
# Objective: The aim of this assignment is to reinforce understanding of the linked list data structure and its implementation in Python.

# Problem Statement: You are tasked with building an inventory management system for a bookstore. The system should allow adding new books to the inventory and removing books based on their ISBN. You'll implement this system using a linked list data structure.

# Task 1
# Create a class named Book with attributes for title, author, genre, ISBN, and quantity.

class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.title} by {self.author}\nGenre: {self.genre}\nISBN: {self.isbn}\nQuantity: {self.quantity}"


# Task 2
# Create a class named Node to represent nodes in the linked list. Each node will store a book object.

class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

    def __str__(self):
        return str(self.book)
    

# Task 3
# Implement a class named InventoryManager to manage the inventory using a linked list.

class InventoryManager:
    def __init__(self, name):
        self.name = name
        self.head = None


# Task 4
# Implement the following methods in the **`InventoryManager`** class:

    # add_book(title, author, genre, isbn, quantity): Adds a new book to the inventory:

    def add_book(self, title, author, genre, isbn, quantity):
        # Create a new Book instance with the args
        new_book = Book(title, author, genre, isbn, quantity)
        # Create a node with the Book
        new_node = Node(new_book)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    # remove_book(isbn): Removes a book from the inventory based on its ISBN:
    def remove_book(self, isbn):
        if self.head is None:
            print(f"The inventory '{self.name}' is empty")
            return
        # If the first node is the node we are trying to remove
        if self.head.book.isbn == isbn:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            return
        # Start at the first node
        current_node = self.head
        # While the current_node has a next value
        while current_node.next is not None:
            # Check if the next node is the node we are trying to remove
            if current_node.next.book.isbn == isbn:
                # Set the current node's next to the next node's next
                current_node.next = current_node.next.next
                return
            # If not, move on to the next node
            current_node = current_node.next
        # If we get to the end of the Linked List without returning, the node was never there
        print(f"{isbn} is not in the '{self.name}' inventory.")


    # display_inventory(): Displays the current inventory:
    def display_inventory(self): # O(n) - Linear Time
        print('Current inventory:')
        # Start at the beginning of the list
        print('head\n | \n V')
        current = self.head
        # While current is a node and not None
        while current:
            # Print the node and an arrow
            print(current, end=' -> ')
            # Move on to the next node in the linked list
            current = current.next
        # Print None at the end
        print(None)

if __name__ == "__main__":
    library = InventoryManager("Library")

    # Adding books to the library
    library.add_book("Origin", "Dan Brown", "Literature & Fiction", "978-0525563709", 2150)
    library.add_book('Inferno', 'Dan Brown', "Literature & Fiction", "978-0385539852", 1800)
    library.add_book('The Lost Symbol', 'Dan Brown', "Literature & Fiction", "978-0307950680", 1995)
    library.add_book('The Da Vinci Code', 'Dan Brown', "Mystery, Thriller & Suspense", "978-0307277671", 1740)
    library.add_book("The Vivaldi Cipher", "Gary McAvoy", "Mystery, Thriller & Suspense", "978-1954123076", 1220)
    library.add_book('Deception Point', 'Dan Brown', "Mystery, Thriller & Suspense", "978-0743497466", 1150)
    library.add_book('Angels & Demons', 'Dan Brown', "Politics & Social Sciences", "978-0743493468", 1550)
    library.add_book('Digital Fortress', 'Dan Brown', "Mystery, Thriller & Suspense", "978-0312944926", 1420)
    
    # Displaying the inventory
    library.display_inventory()

    # Removing a book from the inventory
    library.remove_book("978-1954123076")
    library.display_inventory()