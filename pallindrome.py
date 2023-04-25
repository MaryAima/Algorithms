word = input('give me a word: ')
if word==word[::-1]:
    print(word,' is a pallindrome')
else:
    print(word,' is not a pallindrome')
    word = input('give me a word: ')
