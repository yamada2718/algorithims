count = 0
coins = [0, 10, 50, 100, 500]
for i in coins:
    for j in coins:
        if j > i:
            break
        for k in coins:
            if k > j:
                break
            for l in coins:
                if l > k:
                    break
                for m in coins:
                    if m > l:
                        break
                    for n in coins:
                        if n > m:
                            break
                        for o in coins:
                            if o > n:
                                break
                            for p in coins:
                                if p > o:
                                    break
                                for q in coins:
                                    if q > p:
                                        break
                                    for r in coins:
                                        if r > q:
                                            break
                                        for s in coins:
                                            if s > r:
                                                break
                                            for t in coins:
                                                if t > s:
                                                    break
                                                for u in coins:
                                                    if u > t:
                                                        break
                                                    for v in coins:
                                                        if v > u:
                                                            break
                                                        for w in coins:
                                                            if w > v:
                                                                break
                                                            if i+j+k+l+m+n+o+p+q+r+s+t+u+v+w == 1000:
                                                                count += 1
                                                                # print(i, j, k, l, m, n, o, p, q, r, s, t, u, v, w)
print(count)
