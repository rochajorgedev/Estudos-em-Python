#várias formas de reverter uma string

def solution(string):
    return string [::-1]
    

def solution2(string):
    return ''.join(reversed(string))

def solution3(string):
    string2 = []
    count = len(string)
    while count:
        count -= 1
        string2.append(string[count])
    return ''.join(string2)

def solution4(string):
    string2 = list(string)
    i = 0
    j =  len(string2)-1
    while i<j:
        if not string2[i].isalpha():
            i+=1
        elif not string2[j].isalpha():
            j-=1
        else:
            string2[i], string2[j] = string2[j] , string2[i]
            i+=1
            j-=1
    return ''.join(string2)

palavra = 'world world world'
print(solution(palavra))
print(solution2(palavra))
print(solution3(palavra))
print(solution4(palavra))
