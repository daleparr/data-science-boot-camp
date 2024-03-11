swim = int(input("How long was your swim in mins? "))
cycle = int(input("How long was your cycle in mins? "))
run = int(input("How long was your run in mins? "))

total = swim + cycle + run
print(total)

if total < 100:
    print("You awarded the Provincial Colours, Congratulations! ")

elif 101 <= total <= 105:
    print("You awarded the Half-Provincial Colours, Congratulations! ") 

elif 106 <= total <= 110:
    print("You awarded the Provincial Scroll, Congratulations! ") 

else: total > 111
print("Sorry, no award. Improve your time and try again next year ")