#esse codigo é para saber se um numéro tem uma raiz quadrada natural por exemplo a raiz quadrada de 9 é 3 
def is_square(num):
    if num > -1:
        #faz a verificação se o número é maior que -1 e faz o calculo
        square = num ** 0.5
        #aqui é para saber se é realmente uma raiz sem resultados decimais 
        remainder = square % 1
        #essa ultima verificação utilizando a linha anterior é para retornar verdadeiro se realmente for uma raiz e false se não for
        if remainder == 0:
            return True
        else:
            return False
    else:
        return False

print(is_square(9))