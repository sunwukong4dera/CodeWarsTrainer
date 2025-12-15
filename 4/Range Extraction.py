def solution(args) -> str:
    ret_str = ''

    index = 0
    tmp_list = []
    while index < len(args):
        if index == len(args) - 1:
            diff = args[index] - args[index - 1]
            if diff == 1:
                print(f'{index=} --> {args[index]=} {args[index - 1]=}')
                tmp_list.append(args[index])
                if len(tmp_list) == 1:
                    ret_str += f'{tmp_list[0]}'
                elif len(tmp_list) == 2:
                    tmp_list.append(args[index])
                    ret_str += f'{tmp_list[0]},{tmp_list[1]},'
                else:
                    ret_str += f'{tmp_list[0]}-{tmp_list[-1]},'
            else:
                if not len(tmp_list):
                    ret_str += f'{args[index]},'
                elif len(tmp_list) == 1:
                    ret_str += f'{tmp_list[0]},{args[index]},'
                elif len(tmp_list) == 2:
                    tmp_list.append(args[index])
                    ret_str += f'{tmp_list[0]}-{tmp_list[-1]},'
                else:
                    ret_str += f'{tmp_list[0]}-{tmp_list[-1]},'
            return ret_str[:-1]

        diff = args[index + 1] - args[index]
        if diff == 1:
            print(f'{index=} --> {args[index]=} {args[index + 1]=}')
            tmp_list.append(args[index])
        else:
            print(f'{index=} \\ {args[index]=} {args[index + 1]=}, ({diff=})')
            if not len(tmp_list):
                ret_str += f'{args[index]},'
            elif len(tmp_list) == 1:
                ret_str += f'{tmp_list[0]},{args[index]},'
            elif len(tmp_list) == 2:
                tmp_list.append(args[index])
                ret_str += f'{tmp_list[0]}-{tmp_list[-1]},'
            else:
                tmp_list.append(args[index])
                ret_str += f'{tmp_list[0]}-{tmp_list[-1]},'

            tmp_list.clear()
        print(tmp_list)
        index += 1







print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))

print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
#
# print(solution([-79, -78, -76, -73, -72, -69, -66, -63, -60, -59, -56, -53, -52, -51, -48, -45, -42, -40, -37]))












