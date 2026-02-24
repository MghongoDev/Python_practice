import load_dictionary
word_list = load_dictionary.load('/home/davyce/Python_practice/palingram spells/dictionary.txt')
palindrome_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindrome_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(palindrome_list)))
print(*palindrome_list, sep='\n')

