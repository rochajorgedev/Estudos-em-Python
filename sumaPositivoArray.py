#soma de numeros positivos dentro de um array

def positiveSum(num):
    result = 0
    for i in range(0, len(num)):
        if num[i] > 0:
            result = result +num[i]
    
    if result == 0:
        return 0
    else:
        return result




print(positiveSum([1,-4,7,12]))


