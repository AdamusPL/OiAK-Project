# n = 7
# A + B <= 127
# modulo = 2**n - K = 128 - K
# 3 <= K <= 2**(n-1) - 1 = 63
# S = (A+B) % modulo
# S = {A+B          if A+B < modulo
#     {A+B - modulo if A+B >= modulo
# S = {(A+B)%128   if cout = 0
#     {(A+B+K)%128 if cout = 1
# cout = output carry from A+B+K

