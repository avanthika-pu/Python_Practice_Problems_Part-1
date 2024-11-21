# string is symmetric or pallindrome
def sympal(s):
    if s == s[::-1]:
        print("This is pallindrome")
    else:
        print("This is not pallindrome")

    size = len(s)
    if size % 2 == 0:
        half = size //2
        if s[0:half] == s[half:size]:
            print("This is symmetric")
    else:
        print("This is not symmetric")

sympal("khokho")