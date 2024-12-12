#conversion of snake case to pascal case using capitalize()
def snake_to_pascal_case_1(snake_str):
    words = snake_str.split("_")
    pascal_str = "".join([word.capitalize()for word in words])
    return pascal_str
snake_str = "python_is_simple"
print(snake_to_pascal_case_1(snake_str))