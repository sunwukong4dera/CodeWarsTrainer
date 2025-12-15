def make_readable(seconds: int) -> str:
    return f'{str(seconds // 3600).zfill(2)}:{str(seconds // 60 % 60).zfill(2)}:{str(seconds % 60).zfill(2)}'

print(make_readable(3599))
