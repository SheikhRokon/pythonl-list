# string থেকে word,Leter,Digit বেড় করা program
from pydoc import text


numOfWord = 0
numOfLater = 0
numOfDigit = 0

text = input("Enter text and Number :")

for x in text:
    x = x.lower()
    if x >= "a" and x <= "z":
        numOfLater = numOfLater + 1

    elif x >= '0' and x <= '9':
        numOfDigit = numOfDigit + 1

    elif x ==" ":
        numOfWord = numOfWord + 1

print("Words :",numOfWord)
print("Digit :", numOfDigit)
print("Leter :", numOfLater)