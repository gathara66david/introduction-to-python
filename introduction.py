# this is a comment
""" multi-line comments can be done like this """

# Numbers
print(2 + 2) # addition
print(2 - 2) # subtraction
print(2 * 2 )# multiplication
print(2 / 2) # division
print(2 // 2) # integer division
print(2**3) # exponentiation
print(2 % 2) # modulus
print(type(45))

# mathematics module
import math
math.lcm(3,5,7)
print(dir(math))# list all the functions in the math module
print("""multi line string""")


print('a' + 'string') # concatenate strings
print('a' * 2) # repeat strings
print('a string'[0]) # first character of a string
print('a string'[-1]) # last character of a string
print('a string'[0:4]) # index a string to get first 4 characters
print('a string'[:4]) # index a string to get first 4 characters
print('a string'[::2]) # get every other letter
print('a string'[::-1]) # reverse the string
print('a string'[:5:2]) # every other letter in the first 5 characters

# Python has many built-in functions for strings
""".join() , .split() , .lstrip() / .rstrip() , and .removeprefix() / .removesuffix() """

print('-'.join(['this', 'is', 'a', 'test'])) # join a list of strings with a hyphen
print('this is a test'.split()) # split a string into a list of strings
print('testtest - remove left'.lstrip('tes')) # remove the left side of a string
print('testtest - remove right'.rstrip('ght')) # remove the right side of a string
print('testtest - remove left'.removeprefix('testte')) # remove the left side of a string
print('testtest - remove right'.removesuffix('ght')) # remove the right side of a string
print(f'The answer is  {2 + 2}') # string formatting
print('The answer is {}'.format(2 + 2)) # string formatting


#Variables
books = 5
print(books)# print the value of books
books +=2
print(books)# add 2 to the value of books   
books *=3
print(books)# multiply the value of books by 3
books /=2
print(books)# divide the value of books by 2
books -=1
print(books)# subtract 1 from the value of books
books **=2
print(books)# raise the value of books to the power of 2
books %=2
print(books)# get the modulus of the value of books
books //=2
print(books)# get the integer division of the value of books

a = 'string 1'
b = 'another string'
print(a + b)# concatenate strings

a = 'string 1'
print(type(a))





