str_manip = input("what is your full name? ")
print(len(str_manip))
print(str_manip.replace("r","@"))
last_3_backwards = str_manip[-3:][::-1]
print(last_3_backwards)

"""
The first 3 characters will be DAL
The last 2 characters will be RR
"""
first_3 = str_manip[:3]
last_2 = str_manip[-2:]

final_word = first_3 + last_2
print(final_word)