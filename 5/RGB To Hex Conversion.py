def rgb(r, g, b):
    res = ''
    for el in (r, g, b):
        if el > 255:
            res += 'FF'
        elif el < 0:
            res += '00'
        else:
            res += str(hex(el))[2:].upper().zfill(2)
    return res



print(rgb(0, 0, 0))
print(rgb(1, 2, 3))
print(rgb(255, 255, 255))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))



