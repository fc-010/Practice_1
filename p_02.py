word = "Programming"

print(word[::-1])
print(word[:3], word[-3:])
print(word.lower().count("m"))

def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome("level"), is_palindrome("python"))
