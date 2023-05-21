def checkAB(X):
    good = True  # when MSB equals 0, we accept everything

    if X[n - 1] == 1:  # when MSB equals 1, check if other bits equals 0
        for x in X:
            if x != 0:
                good = False
                break

    return good


def check(X):
    # check K
    good = True  # when MSB equals 0, we accept everything

    if X[n - 1] == 1:  # MSB can't equal 1
        good = False

    else:  # when MSB equals 0, check if they are other than 0,1,2
        for i in range (n-2,-1,-1):
            if i >= 2 and X[i] != 0:  # if number larger than 3, then good
                break
            good = False #if not, then don't accept

    return good


while True:
    A = input("Enter A=")
    B = input("Enter B=")
    K = input("Enter K=")
    n = int(input("Enter n="))

    A = list(map(int, str(A)))
    B = list(map(int, str(B)))
    K = list(map(int, str(K)))

    A.reverse() #reverse to simulate binary number
    B.reverse()
    K.reverse()

    checkA = checkAB(A)
    checkB = checkAB(B)
    checkK = check(K)

    if checkA is True and checkB is True and checkK is True:
        break

# print("The list from number is " + str(A))
# print("The list from number is " + str(B))
# print("The list from number is " + str(K))

#A+B sum
def sum(X,Y,carry):
    S=list()
    for i in range(n):
        if(X[i]==1 and Y[i]==1):
            if (carry == 0):
                S.append(0)
            else:
                S.append(1)
            carry=1

        elif(X[i]==1 and Y[i]==0 or X[i]==0 and Y[i]==1):
            if(carry==0):
                S.append(1)
            else:
                S.append(0)
                carry=1

        else:
            if (carry == 0):
                S.append(0)
            else:
                S.append(1)
    return S

carry=0
S1=list()
S2=list()

S1=sum(A,B,carry)
carry=0
S2=sum(S1,K,carry)

# if carry=0:
#
# else:


print("The list from number is " + str(S1))
print("The list from number is " + str(S2))

#A+B+K sum

# if carry==1:


