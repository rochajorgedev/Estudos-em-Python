#Codigo que conta quantas vogais existem na string enviada para umas das funções 
#primeira função faz a soma de forma simples utilizando count, porém ela só conta de maneira simples e apenas vogais minusculas e não olha para vogais acentuadas (Ex: éÉáãÁÃ)
def contarVogais1(word01):
    vowels = word01.count('a')
    vowels += word01.count('e')
    vowels += word01.count('i')
    vowels += word01.count('o')
    vowels += word01.count('u')
     
    return vowels

#essa segunda função faz a o somatorio atraves da função sum e utiliza a estrutura de repetição for para percorrer toda a string e soma os resultados
#porém diferente da primeira função ela olha também as vogais maiusculas 
def contarVogais2(word02):
    return sum(1 for let in word02 if let in "aeiouéáãÉÁÃAEIOU")


#teste simples para as funções
print(contarVogais1("“Ninguém entra em um mesmo rio uma segunda vez, pois quando isso acontece já não se é o mesmo, assim como as águas que já serão outras.” - (Heráclito)"))
print(contarVogais2("“Ninguém entra em um mesmo rio uma segunda vez, pois quando isso acontece já não se é o mesmo, assim como as águas que já serão outras.” - (Heráclito)"))

#esse segundo teste é para demonstrar que na primeira função ela não olha as letras maiusculas 
print(contarVogais1("“Ninguém entrA Em um mesmo rio Uma segunda vez, pois quando isso acontece já não sE é o mesmo, assim como as águas que já serão outras.” - (Heráclito)"))
print(contarVogais2("“Ninguém entra em um mesmo rio uma segunda vez, pois quando isso acontece já não se é o mesmo, assim como as águas que já serão outras.” - (Heráclito)"))
