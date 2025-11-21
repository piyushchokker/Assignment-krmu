
def loop1(n):
    for i in range(n):
        pass
# Time: O(n), Space: O(1)


def loop2(n):
    for i in range(n):
        for j in range(n):
            pass
# Time: O(n^2), Space: O(1)


def loop3(n):
    for i in range(n):
        for j in range(i):
            pass
# Time: O(n^2), Space: O(1) 


def loop4(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass
# Time: O(n^3), Space: O(1)


def loop5(arr):
    for x in arr:
        pass
# Time: O(n), Space: O(1)


def loop6(arr):
    for x in arr:
        for y in arr:
            pass
# Time: O(n^2), Space: O(1)


def loop7(matrix):
    for row in matrix:
        for val in row:
            pass
# Time: O(n*m), Space: O(1)


def loop8(n):
    for i in range(n):
        for j in range(i, n):
            pass
# Time: O(n^2), Space: O(1)


def loop9(n):
    for i in range(n):
        for j in range(n):
            for k in range(i):
                pass
# Time: O(n^3), Space: O(1)


def loop10(n):
    for i in range(n):
        for j in range(i*i):
            pass
# Time: O(n^3), Space: O(1)


def loop11(n):
    for i in range(n):
        for j in range(n):
            for k in range(j):
                pass
# Time: O(n^3), Space: O(1)


def loop12(arr):
    res = []
    for i in arr:
        res.append(i)
# Time: O(n), Space: O(n)


def loop13(arr):
    res = []
    for i in arr:
        for j in arr:
            res.append((i, j))
# Time: O(n^2), Space: O(n^2)


def loop14(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    pass
# Time: O(n^4), Space: O(1)


def loop15(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                pass
# Time: O(n^3), Space: O(1)


def loop16(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                pass
# Time: O(n^2), Space: O(1)


def loop17(n):
    for i in range(n):
        for j in range(i*i):
            for k in range(j):
                pass
# Time: O(n^4), Space: O(1)


def loop18(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(k):
                    pass
# Time: O(n^4), Space: O(1)


def loop19(n):
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                pass
# Time: O(n^3), Space: O(1)


def loop20(n):
    for i in range(n):
        for j in range(i):
            for k in range(i):
                pass
# Time: O(n^3), Space: O(1)


def loop21(arr):
    s = 0
    for x in arr:
        s += x
# Time: O(n), Space: O(1)


def loop22(arr):
    res = []
    for i in arr:
        for j in arr:
            for k in arr:
                res.append((i, j, k))
# Time: O(n^3), Space: O(n^3)


def loop23(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        pass
# Time: O(n^5), Space: O(1)


def loop24(n):
    for i in range(n):
        for j in range(i*i):
            pass
# Time: O(n^3), Space: O(1)


def loop25(n):
    for i in range(n):
        for j in range(n):
            for k in range(j*j):
                pass
# Time: O(n^4), Space: O(1)


def loop26(arr):
    res = {}
    for i in arr:
        res[i] = 1
# Time: O(n), Space: O(n)


def loop27(arr):
    res = {}
    for i in arr:
        for j in arr:
            res[(i, j)] = 1
# Time: O(n^2), Space: O(n^2)


def loop28(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        for o in range(n):
                            pass
# Time: O(n^6), Space: O(1)


def loop29(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    pass
# Time: O(n^4), Space: O(1)


def loop30(n):
    for i in range(n):
        for j in range(i):
            for k in range(i*i):
                pass
# Time: O(n^4), Space: O(1)


def loop31(n):
    for i in range(n):
        for j in range(i*i):
            for k in range(j):
                for l in range(k):
                    pass
# Time: O(n^5), Space: O(1)


def loop32(arr):
    res = []
    for i in arr:
        for j in arr:
            for k in arr:
                for l in arr:
                    res.append((i, j, k, l))
# Time: O(n^4), Space: O(n^4)


def loop33(n):
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    pass
# Time: O(n^4), Space: O(1)


def loop34(n):
    for i in range(n):
        for j in range(n):
            for k in range(i+j):
                pass
# Time: O(n^3), Space: O(1)


def loop35(matrix):
    for row in matrix:
        for val in row:
            for x in range(val):
                pass
# Time: O(n*m*val), Space: O(1)


def loop36(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        pass
# Time: O(n^5), Space: O(1)


def loop37(n):
    res = []
    for i in range(n):
        for j in range(n):
            res.append(i+j)
# Time: O(n^2), Space: O(n^2)


def loop38(n):
    for i in range(n):
        for j in range(n):
            if i < j:
                for k in range(i):
                    pass
# Time: O(n^3), Space: O(1)


def loop39(arr):
    d = {}
    for i in arr:
        for j in arr:
            d.setdefault(i+j, []).append((i, j))
# Time: O(n^2), Space: O(n^2)


def loop40(n):
    for i in range(n):
        for j in range(i):
            for k in range(i*j):
                pass
# Time: O(n^4), Space: O(1)


def loop61(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        for o in range(n):
                            for p in range(n):
                                pass
# Time: O(n^7), Space: O(1)


def loop62(arr):
    res = []
    for i in arr:
        for j in arr:
            for k in arr:
                for l in arr:
                    for m in arr:
                        res.append((i, j, k, l, m))
# Time: O(n^5), Space: O(n^5)


def loop63(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        for o in range(m):
                            pass
# Time: O(n^6), Space: O(1)


def loop64(n):
    for i in range(n):
        for j in range(i*i):
            for k in range(j*j):
                pass
# Time: O(n^5), Space: O(1)  


def loop65(arr):
    d = {}
    for i in arr:
        for j in arr:
            for k in arr:
                d[(i, j, k)] = i+j+k
# Time: O(n^3), Space: O(n^3)


def loop66(n):
    for i in range(n):
        for j in range(n):
            for k in range(i+j):
                for l in range(i*j+1):
                    pass
# Time: O(n^4), Space: O(1)


def loop67(n):
    res = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res.append(i*j*k)
# Time: O(n^3), Space: O(n^3)


def loop68(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        for o in range(m):
                            for p in range(o):
                                pass
# Time: O(n^7), Space: O(1)


def loop69(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        for o in range(n):
                            for p in range(n):
                                for q in range(n):
                                    pass
# Time: O(n^8), Space: O(1)


def loop70(arr):
    res = []
    for i in arr:
        for j in arr:
            for k in arr:
                for l in arr:
                    for m in arr:
                        for o in arr:
                            res.append((i, j, k, l, m, o))
# Time: O(n^6), Space: O(n^6)



