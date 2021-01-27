from xkcdpass import xkcd_password as xp

try:
    numwords = int(input("How many words do you want in you password: "))
except ValueError:
    print("Wrong command! ")
    numwords = int(input("Type a number:"))

mylist = []
word = ''
nth_word = 1
isOn = True
while isOn:
    if word == '1':
        isOn = False
    else:
        word = input(f"[{nth_word}] word:")
        nth_word += 1
        if word != '1':
            mylist.append(word)
            print("Type '1' to generate password!")

print(xp.generate_xkcdpassword(mylist, delimiter="", numwords=numwords))