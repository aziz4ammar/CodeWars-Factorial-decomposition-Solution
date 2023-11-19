def decomp(n):

    number_count = {2 : 1}
    return_str = ""

    def add_list(num):
        if num not in number_count:
            number_count[num] = 1
        else:
            number_count[num] += 1

    for x in range(n, 1, -1):
        add = False
        for y in range(1, x):
            if x == 1 or y == 1: continue
            a = True
            while a:
                if x % y == 0 and y != 1:
                    x = int(x / y)
                    add_list(y)
                else:
                    a = False
                    add = True

        if add and x != 1:
            add_list(x)

    number_count3 = {k: number_count[k] for k in sorted(number_count.keys())}

    for x, y in number_count3.items():
        if y == 1:
            return_str += str(x) + " * "
        else:
            return_str += str(x) + "^" + str(y) + " * "

    return return_str[:-3]