i = 11
while True:
    i_10 = str(i) #stringにキャスト
    if i_10 ==  i_10[::-1]: #文字列の反転
        i_2 = format(i, 'b')
        if i_2 == i_2[::-1]:
            i_8 = format(i, 'o')
            if i_8 == i_8[::-1]:
                break
    i +=2 #2進数が回文数になるのは奇数のときに限られるため
print(i)