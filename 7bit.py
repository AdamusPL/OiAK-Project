
while True:
    A = int((input("Enter A: ")), 2)
    B = int((input("Enter B: ")), 2)
    K = int((input("Enter K: ")), 2)
    if A <= 127 and B <= 127 and 3 <= K <= 63:
        break

S1 = A+B
S2 = A+B+K

bit_mask = 128
cout = bit_mask & S2

if cout == 128:
    cout = 1
else:
    cout = 0

if cout == 0:
    S = S1 % 128

else:
    S = S2 % 128

print(bin(S))
