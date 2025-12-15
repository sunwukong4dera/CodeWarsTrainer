def to_camel_case(text: str):
    return ''.join([word.capitalize() if text.replace('-', ' ').replace('_', ' ').split().index(word) != 0 else word for word in text.replace('-', ' ').replace('_', ' ').split()])

print(to_camel_case('gello-vorld'))