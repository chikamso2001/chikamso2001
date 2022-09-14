# a mild mimick of encoding 
# I will define a function that encodes
def encode(word):
    the_ascii = [ord(c) for c in word]
    adjusted_ascii = [c + 4 for c in the_ascii]
    reult_char = [chr(c) for c in adjusted_ascii]
    return ''.join(str(c) for c in reult_char)
a_word = input("Enter a word: ")
encoded_word = encode(a_word)
print(encoded_word)

def decode(word):
    the_ord = [ord(c) for c in word]
    true_ord = [c - 4 for c in the_ord]
    result_char = [chr(c) for c in true_ord]
    return ''.join(str(c) for c in result_char)

to_decode = input("should i decode the encoded word(yes/no): ").lower()
if to_decode == 'yes':
    decoded_word = decode(encoded_word)
    print(decoded_word)
else:
    print("Alright, bye!!!")