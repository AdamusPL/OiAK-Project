# n = 7
# modulo = 2**n - K = 128 - K
# 3 <= K <= 2**(n-1) - 1 = 63
# S = (A+B) % modulo
# S = {A+B          if A+B < modulo
#     {A+B - modulo if A+B >= modulo
# S = {(A+B)%128   if cout = 0
#     {(A+B+K)%128 if cout = 1
# cout = output carry from A+B+K

n = int(input("Enter n="))
A = input("Enter A=")
B = input("Enter B=")
K = input("Enter K=")

A_lista = list(A)
A = list(map(int, str(A)))
B = list(map(int, str(B)))
K = list(map(int, str(K)))

A.reverse()  # reverse to simulate binary number
B.reverse()
K.reverse()
A_lista.reverse()

print(A)
print(A_lista)
