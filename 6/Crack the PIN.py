from hashlib import md5

def crack(hash: str) -> str:
    def num_to_str(number: int):
        return "0" * (5 - len(str(number))) + str(number)
    password_num = 0
    while password_num < 100000:
        password_str = num_to_str(password_num)
        if md5(password_str.encode()).hexdigest() == hash:
            return password_str
        password_num += 1
    return ''



print(crack("86aa400b65433b608a9db30070ec60cd"))