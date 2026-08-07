def is_sequence(s,t):
    """return bool while checking if s , is a sequence of t"""
    if len(s) > len (t):
        return False
    elif len(s) == len(t):
        return s == t

    current = 0
    for i in range(0, len(s)):
        for j in range(current, len(t)):
            if s[i] == t[j]:
                current = j + 1
                break
            if current == len(t) - 1:
                return False
        return True

print(is_sequence("acb","ahbgdc"))
