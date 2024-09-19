"""
Week 6 Lab 3
Question: Python program to create a movie rental system using OOP.
Author: Jobanpreet Singh
"""

class Movie():
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True #initializes movie as available

    def mark_as_rented(self):
        self.available = False #movie is rented, hence not available
    
    def mark_as_available(self):
        self.available = True #movie is available

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre} - {'Available' if self.available else 'Rented'}"
    
class Customer():
    def __init__(self, name):
        self.name = name
        self.rented_movies = [] #creates an empty list named 'rented_movies'
    
    def rent_movie(self,movie):
        if movie.available:
            movie.mark_as_rented()
            self.rented_movies.append(movie) #adds a new movie to the list
            print(f"{self.name} rented {movie.title}")

        else:
            print(f"{movie.title} is not available")

    
    def return_movie(self,movie):
        if movie in self.rented_movies:
            movie.mark_as_available()
            self.rented_movies.remove(movie)
            print(f"{self.name} returned {movie.title}")

        else:
            print(f"{self.name} did not rent {movie.title}")

    
    def list_rented_movies(self):
        if self.rented_movies:
            print(f"{self.name}'s Rented Movies: ")
            for movie in self.rented_movies:
                print(movie)

        else:
            print(f"{self.name} has no rented movies.")

    
class RentalStore():
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def list_movies(self):
        if self.movies:
            print("Available Movies")
            for movie in self.movies:
                print(movie)
        
        else:
            print("No Movies Available")

    def find_movie(self,title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
            
        return None
    
def menu():
    print("Movie Rental System Menu:")
    print("1. List Available Movies")
    print("2. Rent a Movie")
    print("3. Return a Movie")
    print("4. List Rented Movies")
    print("5. Add a Movie to the Store")
    print("6. Exit")


def main():
    store = RentalStore()
    store.add_movie(Movie("The Godfather", "Crime", 1972))
    store.add_movie(Movie("Rockstar", "Musical", 2011))
    store.add_movie(Movie("Annabelle", "Horror", 2013))

    customers = {
        "Alice" : Customer("Alice"),
        "Bob" : Customer("Bob")
    }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            store.list_movies()

        elif choice == "2":
            customer_name = input("Enter your name: ").strip()
            movie_title = input("Enter Movie title to rent: ").strip()
            customer = customers.get(customer_name)
            movie = store.find_movie(movie_title)
            if customer and movie:
                customer.rent_movie(movie)
            elif not customer:
                print("Customer not found.")
            elif not movie:
                print("Movie not found.")

        elif choice == "3":
            customer_name = input("Enter your name: ").strip()
            movie_title = input("Enter the movie title to return: ").strip()
            customer = customers.get(customer_name)
            movie = store.find_movie(movie_title)
            if customer and movie:
                customer.return_movie(movie)
            elif not customer:
                print("Customer not found.")
            elif not movie:
                print("Movie not found.")

        elif choice == "4":
            customer_name = input("Enter your name: ").strip()
            customer = customers.get(customer_name)
            if customer:
                customer.list_rented_movies() 
            else:
                print("Customer not found.")

        elif choice == "5":
            title = input("Enter Movie Title: ").strip()
            genre = input("Enter Movie Genre: ").strip()
            year = int(input("Enter Movie Release Year: ").strip())
            store.add_movie(Movie(title, genre,year))
            print(f"Movie '{title} added to the store")

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        
        
