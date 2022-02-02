#esse codigo é para fazer a soma de todos os numeros existentes numa lista fazendo sendo que eles estão elevado ao quadrado
# por exemplo lista = [1,2] o resultado é 5, pois é 1^2+2^2 = 5
def square_sum(l):
    h = 0
    i = 0
    while i < len(l):
        h += (l[i] ** 2)
        i += 1
    return h

print(square_sum([1,2]))
print(square_sum([1,2,3,5]))