S, T = map(str, input().split())

w = 1

def split_string_n_chars(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

while w < len(S):
    result = split_string_n_chars(S, w)
    for i in range(w):
        comb = []
        for s in result:
            if(len(s) >= i + 1):
                comb.append(s[i])
        if T == ''.join(comb):
            print('Yes')
            exit()
    w += 1

print('No')
    