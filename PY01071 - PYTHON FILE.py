def check(s):
    if len(s) < 3: return False
    s = s.lower()
    if s[len(s)-3:] != ".py":
        return False
    for i in s:
        if ord(i) < ord('a') and ord(i) > ord('z') and ord(i) != ord('.') and ord(i) != ord('_'):
            return False
    return True
s = input()
# print(s[len(s)-3:])
if(check(s)): print('yes')
else: print('no')
