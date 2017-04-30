def cutstick(sticks, length, members): #sticksは棒の数
    if sticks >= length:
        return 0
    elif sticks <= members:
        return 1 + cutstick(sticks * 2, length, members) #棒の数 <= 人数 なら棒の数は2倍に
    else:
        return 1+ cutstick(sticks + members, length, members) #棒の数 > 人数 なら棒の数は人数分だけ増える
print(cutstick(1, 20, 3))
print(cutstick(1, 100, 5))
