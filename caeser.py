char = input("Enter The String:")
cipher = ""
code = int()
for ch in char:
    if not ch.isalpha():
        continue
    ch = ch.upper()
    code = ord(ch)+1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
