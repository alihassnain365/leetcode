def valid_palindrome(s:str)->bool:
    """return if the give string is a valid palindrome"""
    if s == '':
        return True

    s = "".join(s.split())
    s = s.lower()
    pure_s = [c.lower() for c in s if c.isalnum()]
    print(pure_s)
    
    reverse = list(reversed(pure_s))
    print(reverse)

    if pure_s == reverse:
        return True
    else:
        return False


print(valid_palindrome("A man, a plan, a canal: Panama"))

