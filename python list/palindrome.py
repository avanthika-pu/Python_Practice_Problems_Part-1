string = "malayalam , english, malayalam"
split_string = string.split(',')
for word in split_string:
        word = word.strip()
        if word == word[::-1]:
            print(f"palindrome words in string:{word}")
        else:
            print(f"not pallindrome:{word}")
