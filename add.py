word = input("Enter a word: ")

if word.endswith("ing"):
    word += "ly"
else:
    word += "ing"

print("Modified word:", word)

