from math import sin

def get_rope_length(field_diameter, eaten_ratio): # 10, 0.5
    if not(field_diameter) or not(eaten_ratio):
        return 0
    if eaten_ratio == 1:
        return field_diameter


    radius = field_diameter / 2
    alpha = 180 - 1
    f = 1/2 * (alpha - sin(alpha)) * radius ** 2
    return int(field_diameter * eaten_ratio)

print(get_rope_length(200, 0.5))