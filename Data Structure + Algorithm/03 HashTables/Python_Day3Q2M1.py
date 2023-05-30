def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    s_hash, t_hash = {}, {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s not in s_hash:
            s_hash[char_s] = char_t
        if char_t not in t_hash:
            t_hash[char_t] = char_s
        if s_hash[char_s] != char_t or t_hash[char_t] != char_s:
            return False
    return True

print(isomorphic_strings('aacad','bbdbe'))