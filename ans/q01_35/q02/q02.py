# operators = ['+', '-', '*', '/', '']
operators = ['*', '']
for i in range(1000, 10000):
    i_str = str(i)
    if '0' in i_str:
        continue
    for j in operators:
        for k in operators:
            for l in operators:
                val = i_str[0] + j + i_str[1] + k +  i_str[2] + l + i_str[3]
                if len(val) > len(i_str):
                    try:
                        if eval(val) == int(i_str[::-1]):
                            print(i)
                    except ZeroDivisionError:
                        pass