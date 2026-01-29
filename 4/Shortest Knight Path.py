"""
a1 b1 c1 d1 e1 f1 g1 h1
a2 b2 c2 d2 e2 f2 g2 h2
a3 b3 c3 d3 e3 f3 g3 h3
a4 b4 c4 d4 e4 f4 g4 h4
a5 b5 c5 d5 e5 f5 g5 h5
a6 b6 c6 d6 e6 f6 g6 h6
a7 b7 c7 d7 e7 f7 g7 h7
a8 b8 c8 d8 e8 f8 g8 h8

"""
def knight(p1, p2):
    pass


def knight_step(current_pos: str):
    list_letters, list_numbers = list('abcdefgh'), [i for i in range(1, 9)]

    current_letter, current_letter_index, current_number, current_number_index \
        = (current_pos[0], list_letters.index(current_pos[0]), int(current_pos[1]), int(current_pos[1]) - 1)

    possible_letters_indexes, possible_numbers_indexes = [], []

    for index in [-2, -1, 1, 2]:
        temp_letter_index = current_letter_index + index
        if 8 > temp_letter_index >= 0:
            possible_letters_indexes.append(temp_letter_index)
        if abs(index) == 1:
            for number_index in [-2, 2]:
                temp_number_index = current_number_index + number_index
                if 8 > temp_number_index >= 0:
                    possible_numbers_indexes.append(temp_number_index)
        elif abs(index) == 2:
            for number_index in [-1, 1]:
                temp_number_index = current_number_index + number_index
                if 8 > temp_number_index >= 0:
                    possible_numbers_indexes.append(temp_number_index)

    possible_numbers_indexes = list(set(possible_numbers_indexes))

    possible_knight_steps = []
    for letter_index in possible_letters_indexes:
        if current_letter_index % 2 == current_number_index % 2: # одинаковая четность
            if letter_index % 2: # нечетные
                for number_index in possible_numbers_indexes:
                    if not (number_index % 2):
                        possible_knight_steps.append(f'{list_letters[letter_index]}{list_numbers[number_index]}')
            else: # четные
                for number_index in possible_numbers_indexes:
                    if number_index % 2:
                        possible_knight_steps.append(f'{list_letters[letter_index]}{list_numbers[number_index]}')
        else: # разная четность
            if letter_index % 2: # нечетные
                for number_index in possible_numbers_indexes:
                    if number_index % 2:
                        possible_knight_steps.append(f'{list_letters[letter_index]}{list_numbers[number_index]}')
            else: # четные
                for number_index in possible_numbers_indexes:
                    if not(number_index % 2):
                        possible_knight_steps.append(f'{list_letters[letter_index]}{list_numbers[number_index]}')
    print(f'symbol: {current_pos}\npositions: {possible_knight_steps}')
    return possible_knight_steps

count, last_steps = 1, []

def looking_for(p1, p2):
    knight_steps = knight_step(p1)
    if p2 in knight_steps:
        return count
    else:
        last_steps.append(p1)
        print(f'\nсписок: {last_steps}')
        for step in knight_steps:
            if step in last_steps:
                continue
            return looking_for(step, p2) + 1

print(looking_for('f6', 'd7'))




















