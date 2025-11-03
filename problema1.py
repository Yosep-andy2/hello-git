casos = int(input())  

for i in range(casos):
    numeros = list(map(int, input().split()))
    if sum(numeros) // len(numeros) == numeros[0]:
        print("YES")
    else:
        print("NO")
