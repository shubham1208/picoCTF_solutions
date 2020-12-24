import string

a = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
b = list(string.ascii_lowercase)

for i in a:
    print(b[i - 1])
# PICOCTF{THENUMBERSMASON}
