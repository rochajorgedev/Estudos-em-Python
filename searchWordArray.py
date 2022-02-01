#Codigo para achar o index de uma palavra dentro de um array 
def foundWord(word):
    return f'found the word "Dog" at position {word.index("Dog")}'


arr = ['Keyboard', 'Wall', 'Cat', 'Dog', 'Mouse', 'Garbage', 'Ladder']
print(foundWord(arr))