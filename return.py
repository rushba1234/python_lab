words = input("Enter a list of words separated by spaces: ").split()

longest_length = max(len(word) for word in words)

print("Length of the longest word:", longest_length)

