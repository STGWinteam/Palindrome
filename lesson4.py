def is_palindrome(string: str) -> bool:
    return string == string[::-1]

print(is_palindrome(input()))