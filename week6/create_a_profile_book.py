alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

import string 

alphabet = string.ascii_lowercase
print(alphabet)

person = [
    ("first name", "John"),
    ("last name", "Doe"),
    ("birthdate", "12-12-1986"),
    ("age", 37),  
    ("favorite color", "blue")
]

people = []

favorite_foods = (
    "Favorite Foods",["hamburger", "spagetti carbonara", "chicken alfredo"]
)

hobbies = [
    "Hobbies", ["traviling", "reading"]
]

movies = [
    "Favorites Movies" , ["Star Wars: Episode IV - A New Hope", "Avengers: Endgame"]
]

favorite_foods[1].append("pizza")
favorite_foods[1].append("sushi")
favorite_foods[1].pop(0)
favorite_foods[1].remove("spagetti carbonara")
print(favorite_foods[1])

hobbies[1][-1] = "Cooking"
hobbies[1].append("hiking")
hobbies[1].append("Photography")
hobbies[1][0] = hobbies[1][2]
hobbies.pop()
print(hobbies)

movies[1].pop(0)
movies[1].append("The Dark Knight")
movies[1].append("Inception")
print(movies[1])
movies[1][-1] = "The Empire Strikes Back"
print(movies[1])
