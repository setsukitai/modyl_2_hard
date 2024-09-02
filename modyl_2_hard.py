
def g_pw(n):
    result=''
    for q in range(1,n):
        for d in range(q + 1,n):
            if (q +d) % n == 0:
                result += str(q) + str(d)
    return result
n = int(input('от 3 до 20'))
if 3 <= n <= 20:
    pw = g_pw(n)
    print(f'Пароль  {n}: {pw}')

