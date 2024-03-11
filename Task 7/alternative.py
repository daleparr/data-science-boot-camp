
word = input("enter phrase ")

# Part 1:
def alternate_character_case(word):
    result = ""
    for i in range(len(word)):
        if i % 2 == 0:
            result += word[i].lower()
        else:
            result += word[i].upper()
    return result
print(alternate_character_case(word))


# Part 2:
s = input("enter phrase ")
def alternate_word_case(s):
    words = s.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return ' '.join(words)
print(alternate_word_case(s))
