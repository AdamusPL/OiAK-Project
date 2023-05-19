
while True:
    n = int(input("Enter n (the number of bits): "))
    A = int((input("Enter A: ")), 2)
    B = int((input("Enter B: ")), 2)
    K = int((input("Enter K: ")), 2)
    if A <= 2**n-1 and B <= 2**n-1 and 3 <= K <= 2**(n-1)-1:
        break

S1 = A+B
S2 = A+B+K

bit_mask = 2**n
cout = bit_mask & S2

if cout == 2**n:
    cout = 1
else:
    cout = 0

if cout == 0:
    S = S1 % 2**n

else:
    S = S2 % 2**n

print(bin(S))
