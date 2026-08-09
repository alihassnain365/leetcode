
def longest_substring(s:str)->int:
    """retunr the count of the longest substring"""
    substrings = list()
        
    for i in range(0,len(s)):
        curr = ''
        for j in range(i,len(s)):
            if not s[j] in curr:
                curr += s[j]
            else:
                i = j
                substrings.append(curr)
    return len(max(substrings))

print(longest_substring('abcabcabb'))