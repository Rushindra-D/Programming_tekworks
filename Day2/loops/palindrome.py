def palindrome(s):
    return s==s[::-1]
word="radar"
if palindrome(word):
    print("it is a palindrome")
else:
    print("not a palindrome")

