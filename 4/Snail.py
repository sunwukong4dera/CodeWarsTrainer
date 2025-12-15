def snail(snail_map):
    m_len = len(snail_map)
    if snail_map == [[]]:
        return []
    start, end = 0, m_len - 1

    i, j = 0, 0
    reverse = False
    minus = False
    count = 0
    ret_list = []
    while True:
        if count == m_len ** 2:
            break
        count += 1
        if reverse:
            if minus:
                ret_list.append(snail_map[i][j])
                i -= 1
                if i == start:
                    end -= 1
                    minus = False
                    reverse = False
            else:
                ret_list.append(snail_map[i][j])
                i += 1
                if i == end:
                    # end -= 1
                    reverse = False
                    minus = True
        else:
            if minus:
                ret_list.append(snail_map[i][j])
                j -= 1
                if j == start:
                    start += 1
                    minus = True
                    reverse = True
            else:
                ret_list.append(snail_map[i][j])
                j += 1
                if j == end:
                    reverse = True

    return ret_list

snail([[]])
print(snail([[1,  2,  3,  4],
       [5,  6,  7,  8],
       [9, 10, 11, 12],
       [13,14, 15, 16]]))

snail([[1,2,3],
        [4,5,6],
        [7,8,9]])

