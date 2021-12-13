

def palindrome_check(word):
    word_reversed = word[::-1]
    if word_reversed == word:
        print("This is a Palindrome")
    else:
        print("This is not a palindrome")

while True:
    a_word = input("Enter a word to check if it is a palindrome: ")
    palindrome_check(a_word)
    try_another = input("Do you want to try another word(yes/no): ").lower()
    if try_another == "yes":
        continue 
    else:
        break
