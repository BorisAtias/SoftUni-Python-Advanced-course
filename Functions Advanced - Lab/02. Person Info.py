def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"

info = {
    'name': 'George',
    'town': 'Sofia',
    "age": 20
}
info2 = ["Georgi", "Sofia", 20]

print(get_info(**info))
print(get_info(*info2))
