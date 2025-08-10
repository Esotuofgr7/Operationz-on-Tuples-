# Empty Tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple with mixed Datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# Nested Tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) 
print(my_tuple)

# Accessing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])   # 'p'
print(my_tuple[5])   # 't'

# Nested Tuple
n_tuple = ("dog", [8, 4, 6], (1, 2, 3))

# Nested index 
print(n_tuple[0][1])  # 'o' — second character of "dog"
print(n_tuple[1][1])  # 4 — second element of the list

# Slicing
print("Sliced :", my_tuple[1:4])  # ['e', 'r', 'm']

# Iterating through tuple
for letter in my_tuple:
    print("Hello", letter)
