""""
# open and show all content
file = open("dob.txt")
content = file.read()
print(content)


#read line by listing
file1 = open("dob.txt")
for line in file.readlines():
    print(line)

    #this will append 2 lines of code and then close the file
 file2 = open("dummy.txt", "w")
 file2.write("hey jude\n")
 file2.write("another brick in the wall\n")
 file2.close()    

#automatically closes the file by using a with statement
with open("dummy.txt" , "r") as files3:
    content = file3.read()
    print(content)

    #this resets the cursur to the start of the document (0) selecton position
    object.seek(0) 


with open("dob.txt" , "r") as file_object:
    print(file_object.read())



"""
names = []
birthdates = []

with open("dob.txt", 'r') as file:
    for line in file:
        
        parts = line.strip().split()
        birthdate = ' '.join(parts[-3:])  
        name = ' '.join(parts[:-3])  
        
        names.append(name)
        birthdates.append(birthdate)


print("Name")
for name in names:
    print(name)


print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)

