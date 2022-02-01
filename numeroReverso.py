def reverseNum(n):
     #esse codigo deixa o numero ao contrario, porém se por exemplo o número for 0321 ele não resolve
    rev = 0
    while n > 0:
        a = n%10
        rev = rev*10 + a
        n = n//10
    x = [int(b) for b in str(rev)]
    return x


def reverNum2(n):
   #ele faz a mesma coisa que o primeiro, só que resolve o problema com o exemplo do número 0321
    num = str(n)
    rev = ''
    for char in num:
        rev = char + rev
    x = [int(b) for b in str(rev)]
    return x


num = 3618027
print(reverseNum(num), " ", reverNum2(num))
