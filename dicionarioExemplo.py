#criando dicionario 
phonebook = {  
    "John" : 000000000,
    "Jack" : 111111111,
    "Jill" : 222222222
}  

#adicionando e excluindo dados dentro do dicionario

del phonebook["Jack"] #deletar metodo 1
phonebook.pop("Jill") #deletar metodo 2
phonebook["Jack"] = 333333333 #adicionar dado

#mostrar os dados dentro do dicionario em python
for name, number in phonebook.items():
    #primeiro exemplo de como formatar string
    print("Phone number of %s is %d" % (name, number))
    #segundo exemplo de como formatar string
    print(f"Phone number of {name} is {number}")

#verificando se existem dados dentro do dicionario de dados 
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  