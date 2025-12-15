"""
test.assert_equals(format_duration(0), "now")
        test.assert_equals(format_duration(1), "1 second")
        test.assert_equals(format_duration(62), "1 minute and 2 seconds")
        test.assert_equals(format_duration(120), "2 minutes")
        test.assert_equals(format_duration(3600), "1 hour")
        test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
        test.assert_equals(format_duration(15731080), "182 days, 1 hour, 44 minutes and 40 seconds")
        test.assert_equals(format_duration(132030240), "4 years, 68 days, 3 hours and 4 minutes")
        test.assert_equals(format_duration(205851834), "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
        test.assert_equals(format_duration(253374061), "8 years, 12 days, 13 hours, 41 minutes and 1 second")
        test.assert_equals(format_duration(242062374), "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
        test.assert_equals(format_duration(101956166), "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
        test.assert_equals(format_duration(33243586), "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")

"""
def format_duration(seconds):
    if not seconds:
        return 'now'
    ret_str, delimiter= '', ', '
    dict_times = {
        'years': seconds // 60 // 60 // 24 // 365,
        'days': seconds // 60 // 60 // 24 % 365,
        'hours': seconds // 60 // 60 % 24,
        'minutes': seconds // 60 % 60,
        'seconds': seconds % 60
    }
    for key in dict_times.keys():
        el = dict_times.get(key)
        if el:
            if el == 1:
                key = key[:-1]
            ret_str += f'{el} {key}{delimiter}'
    ret_str = ret_str[:-2]
    index = ret_str.rfind(',')
    return ret_str[:index] + ' and' + ret_str[index + 1:] if index != -1 else ret_str


print(format_duration(132030240))
# '4 years, 1528 days, 3 hours and 4 minutes' should equal '4 years, 68 days, 3 hours and 4 minutes'




