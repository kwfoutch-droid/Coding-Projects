characters = input("Enter a word: ")
count = len(characters)
print(f"The word '{characters}' has {count} characters.")

words = input("Enter a sentence: ")
word_count = len(words.split())
print(f"The sentence '{words}' has {word_count} words.")