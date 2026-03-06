# ==============================================================================
#         🐍 PYTHON DATA STRUCTURES — COMPLETE CHEATSHEET
#         Covers: Tuple | List | Set | Dictionary
#         Great for beginners and as a quick reference guide
# ==============================================================================


# ==============================================================================
# 📌 QUICK DECISION GUIDE — Which data structure should I use?
#
#   ┌─────────────┬────────────────────────────────────────────────────────┐
#   │  Structure  │  Use when...                                           │
#   ├─────────────┼────────────────────────────────────────────────────────┤
#   │  Tuple      │  Data that should NEVER change (coordinates, configs)  │
#   │  List       │  Ordered data that you'll add/remove/change often      │
#   │  Set        │  You need UNIQUE items only, order doesn't matter      │
#   │  Dictionary │  You want to label your data with keys (like a form)   │
#   └─────────────┴────────────────────────────────────────────────────────┘
# ==============================================================================


# ==============================================================================
# 1️⃣  TUPLE  ()
# ==============================================================================
# - Created with parentheses ()
# - IMMUTABLE: once created, you CANNOT change, add, or remove items
# - ORDERED: items have a fixed position (index)
# - ALLOWS duplicates
# - Faster than lists because Python knows it won't change
# ==============================================================================

# --- Creating Tuples ---
empty_tuple     = ()
single_item     = (42,)                      # ⚠️ The comma is REQUIRED for single items
coordinates     = (40.7128, -74.0060)        # latitude, longitude of New York
person          = ("Alice", 30, "Engineer")  # name, age, job
rgb_color       = (255, 128, 0)              # an RGB color value

# --- Accessing Items ---
print(person[0])   # "Alice"   → first item  (index starts at 0)
print(person[-1])  # "Engineer" → last item  (negative index counts from end)
print(person[1:3]) # ("30", "Engineer") → slice: from index 1 up to (not including) 3

# --- Tuple Unpacking (very powerful!) ---
# Instead of accessing each item by index, you can unpack in one line
name, age, job = person
print(name)  # "Alice"
print(age)   # 30
print(job)   # "Engineer"

# Real-world example: function returning multiple values as a tuple
def get_dimensions():
    return (1920, 1080)  # width, height

width, height = get_dimensions()
print(f"Screen: {width}x{height}")  # "Screen: 1920x1080"

# --- Useful Tuple Operations ---
print(len(person))          # 3          → number of items
print("Alice" in person)    # True       → check if item exists
print(person.count("Alice"))# 1          → how many times "Alice" appears
print(person.index("Alice"))# 0          → index position of "Alice"

# Concatenation (creates a NEW tuple, doesn't modify original)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2   # (1, 2, 3, 4, 5, 6)

# Convert between tuple and list
my_list  = list(person)   # tuple → list  (now you CAN change it)
my_tuple = tuple(my_list) # list  → tuple (lock it back)

# ⚠️ This will raise a TypeError — tuples are immutable!
# person[0] = "Bob"  → TypeError: 'tuple' object does not support item assignment


# ==============================================================================
# 2️⃣  LIST  []
# ==============================================================================
# - Created with square brackets []
# - MUTABLE: you can change, add, and remove items freely
# - ORDERED: items keep their position unless you move them
# - ALLOWS duplicates
# - The most flexible and commonly used data structure
# ==============================================================================

# --- Creating Lists ---
empty_list    = []
numbers       = [1, 2, 3, 4, 5]
fruits        = ["apple", "banana", "cherry"]
mixed         = [1, "hello", True, 3.14]  # lists can hold different types
nested        = [[1, 2], [3, 4], [5, 6]]  # lists inside lists

# --- Accessing Items ---
print(fruits[0])    # "apple"   → first item
print(fruits[-1])   # "cherry"  → last item
print(fruits[1:3])  # ["banana", "cherry"] → slice

# --- ✏️ MODIFYING ITEMS ---

# Change a specific item by index
fruits[0] = "mango"           # ["mango", "banana", "cherry"]
fruits[-1] = "grape"          # ["mango", "banana", "grape"]  → change last item

# --- ➕ ADDING ITEMS ---

# .append(item) → adds ONE item to the END of the list
# Use this when: you want to add a single item at the end
fruits.append("orange")       # ["mango", "banana", "grape", "orange"]

# .insert(index, item) → adds item at a SPECIFIC POSITION
# Use this when: you need to control WHERE the item goes
fruits.insert(0, "watermelon")  # ["watermelon", "mango", "banana", "grape", "orange"]
fruits.insert(2, "kiwi")        # inserts at index 2, pushes others right

# .extend([items]) → adds MULTIPLE items to the end (merges two lists)
# Use this when: you want to add a whole list at once
fruits.extend(["lemon", "lime"])  # adds both at the end
# Alternative: fruits += ["lemon", "lime"]  → same result

# --- ➖ REMOVING ITEMS ---

# .remove(value) → removes the FIRST occurrence of that VALUE
# Use this when: you know WHAT you want to remove, not WHERE it is
fruits.remove("kiwi")

# .pop() → removes and RETURNS the LAST item
# Use this when: you need to take the last item off the list
last_fruit = fruits.pop()
print(last_fruit)  # "lime" (it was removed AND stored)

# .pop(index) → removes and returns item at a SPECIFIC INDEX
second_fruit = fruits.pop(1)  # removes the item at index 1
print(second_fruit)

# del list[index] → deletes item at index (doesn't return it)
del fruits[0]

# .clear() → removes ALL items, leaving an empty list
temp = [1, 2, 3]
temp.clear()   # []

# --- 🔍 SEARCHING & CHECKING ---
colors = ["red", "green", "blue", "red", "yellow"]

print("red" in colors)          # True  → checks if item exists
print("purple" not in colors)   # True  → checks if item does NOT exist
print(colors.index("blue"))     # 2     → returns index of FIRST match
print(colors.count("red"))      # 2     → counts how many times it appears

# --- 📊 SORTING & ORDERING ---
numbers_list = [5, 1, 9, 3, 7, 2]

# .sort() → sorts the list IN PLACE (modifies the original)
numbers_list.sort()               # [1, 2, 3, 5, 7, 9]  ascending (default)
numbers_list.sort(reverse=True)   # [9, 7, 5, 3, 2, 1]  descending

# sorted() → returns a NEW sorted list, original stays unchanged
original   = [5, 1, 9, 3]
new_sorted = sorted(original)     # [1, 3, 5, 9]
print(original)                   # [5, 1, 9, 3] ← unchanged!

# .reverse() → reverses the list IN PLACE
fruits_rev = ["apple", "banana", "cherry"]
fruits_rev.reverse()  # ["cherry", "banana", "apple"]

# --- 📋 OTHER USEFUL METHODS ---
sample = [10, 20, 30, 40, 50]

print(len(sample))    # 5    → number of items
print(sum(sample))    # 150  → sum of all items (only works with numbers)
print(min(sample))    # 10   → smallest value
print(max(sample))    # 50   → largest value

# .copy() → creates a SHALLOW copy (safe way to duplicate a list)
original_list = [1, 2, 3]
copy_list     = original_list.copy()
copy_list.append(99)
print(original_list)  # [1, 2, 3]  ← not affected!
print(copy_list)      # [1, 2, 3, 99]

# --- 🔥 LIST COMPREHENSION (powerful one-liner) ---
# Pattern: [expression for item in iterable if condition]
squares     = [x**2 for x in range(1, 6)]        # [1, 4, 9, 16, 25]
even_nums   = [x for x in range(20) if x % 2 == 0] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
upper_words = [w.upper() for w in ["hello", "world"]]  # ["HELLO", "WORLD"]


# ==============================================================================
# 3️⃣  SET  {}  or  set()
# ==============================================================================
# - Created with curly braces {} or set() function
# - MUTABLE: you can add and remove items
# - UNORDERED: items have NO guaranteed position, NO indexing!
# - NO DUPLICATES: automatically removes repeated values
# - Very fast for checking if an item exists (faster than lists)
# ==============================================================================

# --- Creating Sets ---
empty_set     = set()             # ⚠️ NOT {} — that creates an empty dict!
unique_nums   = {1, 2, 3, 4, 5}
fruit_set     = {"apple", "banana", "cherry"}

# Duplicates are automatically removed
tags = {"python", "coding", "python", "beginner", "coding"}
print(tags)  # {"python", "coding", "beginner"} → only 3 items!

# Convert list → set to remove duplicates (very common pattern)
messy_list  = [1, 2, 2, 3, 3, 3, 4]
unique_list = list(set(messy_list))  # [1, 2, 3, 4]

# --- ➕ ADDING ITEMS ---

# .add(item) → adds a SINGLE item
# (No .append() in sets — order doesn't matter so there's no "end")
fruit_set.add("mango")

# .update([items]) → adds MULTIPLE items from an iterable
fruit_set.update(["grape", "kiwi"])
fruit_set.update({"lemon", "lime"})  # can also use another set

# --- ➖ REMOVING ITEMS ---

# .remove(item) → removes item, RAISES ERROR if not found
fruit_set.remove("banana")

# .discard(item) → removes item, NO ERROR if not found (safer!)
fruit_set.discard("banana")    # already removed, but no error
fruit_set.discard("pineapple") # doesn't exist, but still no error

# .pop() → removes and returns a RANDOM item (unpredictable!)
popped = fruit_set.pop()

# .clear() → removes ALL items
temp_set = {1, 2, 3}
temp_set.clear()

# --- 🔍 CHECKING MEMBERSHIP ---
programming_langs = {"Python", "JavaScript", "Go", "Rust"}
print("Python" in programming_langs)  # True  → very fast lookup!
print("Java" not in programming_langs) # True

# --- 🔢 SET MATH OPERATIONS (the real power of sets!) ---
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union → all items from BOTH sets (no duplicates)
print(set_a | set_b)          # {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a.union(set_b))     # same result

# Intersection → only items that exist in BOTH sets
print(set_a & set_b)              # {4, 5}
print(set_a.intersection(set_b))  # same result

# Difference → items in set_a that are NOT in set_b
print(set_a - set_b)           # {1, 2, 3}
print(set_a.difference(set_b)) # same result

# Symmetric Difference → items in EITHER set, but NOT IN BOTH
print(set_a ^ set_b)                      # {1, 2, 3, 6, 7, 8}
print(set_a.symmetric_difference(set_b))  # same result

# --- 📐 SET COMPARISON ---
small_set = {1, 2, 3}
big_set   = {1, 2, 3, 4, 5}

print(small_set.issubset(big_set))    # True  → all of small_set is in big_set
print(big_set.issuperset(small_set))  # True  → big_set contains all of small_set
print(small_set.isdisjoint({6, 7}))   # True  → no common items at all


# ==============================================================================
# 4️⃣  DICTIONARY  {}  (key: value pairs)
# ==============================================================================
# - Created with curly braces {} with key: value pairs
# - MUTABLE: you can add, change, and remove key-value pairs
# - ORDERED (since Python 3.7+): insertion order is preserved
# - Keys must be UNIQUE — no duplicate keys!
# - Keys must be IMMUTABLE (strings, numbers, tuples)
# - Values can be ANYTHING (lists, sets, other dicts, etc.)
# ==============================================================================

# --- Creating Dictionaries ---
empty_dict = {}

user = {
    "name":     "Alice",
    "age":      30,
    "email":    "alice@example.com",
    "is_admin": False
}

# Nested dictionary (dict inside dict)
company = {
    "name": "TechCorp",
    "employees": {
        "CEO": "Bob",
        "CTO": "Carol"
    },
    "founded": 2010
}

# --- 🔍 ACCESSING VALUES ---

# Method 1: dict["key"] → raises KeyError if key doesn't exist
print(user["name"])   # "Alice"
print(user["age"])    # 30

# Method 2: dict.get("key") → returns None if key doesn't exist (SAFER!)
print(user.get("name"))         # "Alice"
print(user.get("phone"))        # None  (no error!)
print(user.get("phone", "N/A")) # "N/A" → custom default value

# Accessing nested values
print(company["employees"]["CEO"])  # "Bob"

# --- ✏️ ADDING & UPDATING VALUES ---

# Add a new key-value pair
user["city"] = "New York"

# Update an existing value
user["age"] = 31
user["email"] = "alice_new@example.com"

# .update({}) → add/update MULTIPLE pairs at once
user.update({
    "age":     32,
    "country": "USA",
    "phone":   "555-1234"
})

# .setdefault(key, default) → adds key ONLY if it doesn't exist yet
user.setdefault("nickname", "Ace")   # adds "nickname": "Ace"
user.setdefault("name", "Unknown")   # does NOTHING, "name" already exists
print(user["name"])     # still "Alice"
print(user["nickname"]) # "Ace"

# --- ➖ REMOVING ITEMS ---

# .pop(key) → removes key and RETURNS its value
removed_email = user.pop("email")
print(removed_email)  # "alice_new@example.com"

# .pop(key, default) → returns default instead of error if key missing
val = user.pop("nonexistent", "not found")  # "not found"

# del dict["key"] → deletes the key-value pair
del user["phone"]

# .popitem() → removes and returns the LAST inserted key-value pair as a tuple
last_item = user.popitem()
print(last_item)  # ("nickname", "Ace") or whatever was added last

# .clear() → removes ALL key-value pairs
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()  # {}

# --- 📋 VIEWING CONTENTS ---

profile = {"name": "Bob", "age": 25, "city": "London", "job": "Developer"}

# .keys() → returns all KEYS (as a dict_keys object)
print(profile.keys())    # dict_keys(["name", "age", "city", "job"])
list(profile.keys())     # ["name", "age", "city", "job"] → convert to list

# .values() → returns all VALUES
print(profile.values())  # dict_values(["Bob", 25, "London", "Developer"])

# .items() → returns all KEY-VALUE PAIRS as tuples
print(profile.items())   # dict_items([("name","Bob"), ("age",25), ...])

# --- 🔍 CHECKING & COUNTING ---
print("name" in profile)       # True   → check if KEY exists
print("Bob"  in profile)       # False  → "in" checks KEYS, not values!
print("Bob"  in profile.values()) # True → check values explicitly
print(len(profile))            # 4      → number of key-value pairs

# --- 🔄 LOOPING THROUGH A DICTIONARY ---

# Loop through keys only
for key in profile:
    print(key)

# Loop through values only
for value in profile.values():
    print(value)

# Loop through BOTH keys and values (most common)
for key, value in profile.items():
    print(f"{key}: {value}")

# --- 🔥 DICTIONARY COMPREHENSION ---
# Pattern: {key: value for item in iterable if condition}
word_lengths = {word: len(word) for word in ["apple", "kiwi", "banana"]}
# {"apple": 5, "kiwi": 4, "banana": 6}

squares_dict = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter while building
adults = {name: age for name, age in [("Alice", 30), ("Bob", 15), ("Charlie", 25)] if age >= 18}
# {"Alice": 30, "Charlie": 25}

# --- 📦 MERGING DICTIONARIES ---
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: .update() → merges dict2 INTO dict1 (modifies dict1)
dict1.update(dict2)

# Method 2: {**d1, **d2} → creates a NEW merged dictionary (Python 3.5+)
merged = {**dict1, **dict2}

# Method 3: | operator → clean merge operator (Python 3.9+)
merged = dict1 | dict2


# ==============================================================================
# 5️⃣  USEFUL BUILT-IN FUNCTIONS (work on all data structures)
# ==============================================================================

data = [5, 1, 9, 3, 7, 2, 8, 4, 6]

# len()     → number of items
print(len(data))          # 9

# sorted()  → returns a NEW sorted list (works on any iterable)
print(sorted(data))                   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(data, reverse=True))     # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# min() / max() → smallest / largest value
print(min(data))  # 1
print(max(data))  # 9

# sum() → total of all items (numbers only)
print(sum(data))  # 45

# enumerate() → gives index AND value while looping
fruits_list = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits_list):
    print(f"{index}: {fruit}")   # 0: apple, 1: banana, 2: cherry

# enumerate() with a start index
for index, fruit in enumerate(fruits_list, start=1):
    print(f"{index}. {fruit}")   # 1. apple, 2. banana, 3. cherry

# zip() → loop through TWO lists at the same time
names  = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")  # Alice: 95, etc.

# zip() to create a dictionary from two lists
result_dict = dict(zip(names, scores))  # {"Alice": 95, "Bob": 87, "Charlie": 92}

# any() → True if AT LEAST ONE item is truthy
print(any([False, False, True]))  # True
print(any([0, 0, 0]))             # False

# all() → True if ALL items are truthy
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False


# ==============================================================================
# 6️⃣  TYPE CONVERSIONS — Moving between structures
# ==============================================================================

original_list = [1, 2, 2, 3, 3, 3, 4]

# list → set  (removes duplicates, loses order)
as_set = set(original_list)   # {1, 2, 3, 4}

# set → list  (order may vary!)
as_list = list(as_set)        # [1, 2, 3, 4] (order not guaranteed)

# list → tuple  (makes it immutable)
as_tuple = tuple(original_list)  # (1, 2, 2, 3, 3, 3, 4)

# tuple → list  (makes it mutable)
back_to_list = list(as_tuple)    # [1, 2, 2, 3, 3, 3, 4]

# list of pairs → dictionary
pairs = [("name", "Alice"), ("age", 30), ("city", "NY")]
from_pairs = dict(pairs)   # {"name": "Alice", "age": 30, "city": "NY"}

# string → list of characters
char_list = list("hello")  # ["h", "e", "l", "l", "o"]

# list of strings → single string
word_list  = ["Hello", "World"]
sentence   = " ".join(word_list)   # "Hello World"
csv_format = ",".join(word_list)   # "Hello,World"


# ==============================================================================
# 7️⃣  STRING FORMATTING — Displaying data nicely
# ==============================================================================

name  = "Alice"
age   = 30
score = 98.765

# f-string (modern, recommended — Python 3.6+)
print(f"Name: {name}, Age: {age}")               # Name: Alice, Age: 30
print(f"Score: {score:.2f}")                      # Score: 98.77 → 2 decimal places
print(f"Age in 10 years: {age + 10}")             # Age in 10 years: 40

# Padding for aligned output
print(f"{'Name':<10} {'Score':>10}")              # left-align / right-align
print(f"{name:<10} {score:>10.2f}")

# .format() (older style, still common)
print("Name: {}, Age: {}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))


# ==============================================================================
# 8️⃣  DATETIME — Working with dates and times
# ==============================================================================
import datetime

now       = datetime.datetime.now()   # current date AND time
today     = datetime.date.today()     # current date only

print(now)            # 2024-01-15 14:30:45.123456
print(today)          # 2024-01-15
print(now.year)       # 2024
print(now.month)      # 1
print(now.day)        # 15
print(now.hour)       # 14

# Calculate age
birth_year = 2000
current_age = datetime.datetime.now().year - birth_year
print(f"Age: {current_age}")  # 24 (in 2024)

# Format dates as strings
formatted = now.strftime("%B %d, %Y")      # "January 15, 2024"
formatted2 = now.strftime("%d/%m/%Y")      # "15/01/2024"
formatted3 = now.strftime("%Y-%m-%d")      # "2024-01-15"  (ISO format)


# ==============================================================================
# 9️⃣  REAL-WORLD EXAMPLE — Putting it all together
# ==============================================================================

import datetime

# --- Build a complete user profile using all data structures ---

# TUPLE: immutable birth info
birth_info = ("Alice Johnson", 1995, "New York")

# LIST: dynamic preferences (will be modified)
favorite_foods  = ["Pizza"]
hobbies         = ["Reading"]

# Add more items
favorite_foods.extend(["Sushi", "Tacos", "Burger", "Pizza"])
hobbies.extend(["Coding", "Hiking", "Coding"])

# Clean duplicates using SET, then convert back to sorted LIST
favorite_foods  = sorted(list(set(favorite_foods)))
hobbies         = sorted(list(set(hobbies)))

# DICTIONARY: final profile container
profile = {
    "name":           birth_info[0],
    "birth_year":     birth_info[1],
    "hometown":       birth_info[2],
    "age":            datetime.datetime.now().year - birth_info[1],
    "hobbies":        hobbies,
    "favorite_foods": favorite_foods,
    "movies":         ["Inception", "Interstellar", "The Matrix"],
}

# Update specific fields
profile["name"]                   = "Ace"  # nickname
profile["favorite_foods"][-1]     = "Hamburger"  # update last food
profile["favorite_foods"].sort()  # sort alphabetically
profile["hobbies"].append("Painting")  # add new hobby

# Print the final profile
print("\n" + "=" * 55)
print("           🎉 FINAL USER PROFILE 🎉")
print("=" * 55)
for key, value in profile.items():
    print(f"  {key.upper():<20}: {value}")
print("=" * 55)


# ==============================================================================
#  🗺️  QUICK REFERENCE CHEATSHEET
# ==============================================================================
#
#  TUPLE    ()      │  LIST      []      │  SET       {}      │  DICT  {k:v}
# ──────────────────┼────────────────────┼────────────────────┼──────────────────
#  immutable        │  mutable           │  mutable           │  mutable
#  ordered          │  ordered           │  unordered         │  ordered (3.7+)
#  allows dupes     │  allows dupes      │  NO duplicates     │  unique keys
#  no methods       │  many methods      │  math operations   │  key:value pairs
#  fast access      │  flexible          │  fast lookup       │  labeled data
# ──────────────────┼────────────────────┼────────────────────┼──────────────────
#  [0], [-1]        │  .append()         │  .add()            │  d["key"]
#  unpacking        │  .insert(i, x)     │  .discard()        │  .get("key")
#  len()            │  .extend([])       │  .remove()         │  .update({})
#  .count()         │  .remove(x)        │  .pop()            │  .pop("key")
#  .index()         │  .pop()            │  | & - ^           │  .keys()
#  tuple(list)      │  .pop(i)           │  .union()          │  .values()
#  list(tuple)      │  .sort()           │  .intersection()   │  .items()
#                   │  .reverse()        │  .difference()     │  .setdefault()
#                   │  .copy()           │  .issubset()       │  dict comprehension
#                   │  list comprehension│  set()             │  d | d2  (merge)
# ==============================================================================
