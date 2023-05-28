from Utility import BinaryArithmeticUtils as Bin

def check_AB(X):
    good = True  # when MSB equals 0, we accept everything

    for i in range(n - 1, -1, -1):
        if X[i] == 1:
            if i == 0:
                good = False
            continue
        else:
            break

    return good


def check(X):
    # check K
    good = True  # when MSB equals 0, we accept everything

    if X[n - 1] == 1:  # MSB can't equal 1
        good = False

    else:  # when MSB equals 0, check if they are other than 0,1,2
        for i in range(n - 2, -1, -1):
            if i >= 2 and X[i] != 0:  # if number larger than 3, then good
                return good
        good = False  # if not, then don't accept

    return good


while True:
    A = input("Enter A=")
    B = input("Enter B=")
    K = input("Enter K=")
    n = int(input("Enter n="))

    A = list(map(int, str(A)))
    B = list(map(int, str(B)))
    K = list(map(int, str(K)))

    A.reverse()  # reverse to simulate binary number
    B.reverse()
    K.reverse()

    checkA = check_AB(A)
    checkB = check_AB(B)
    checkK = check(K)

    if checkA is True and checkB is True and checkK is True:
        break


def negation(a):
    if a == 0:
        return 1
    if a == 1:
        return 0

    # never used
    return 33

# creating empty lists of size 7
G=[None]*7
P=[None]*7
H=[None]*7
A_prim=[None]*7

def hashed_cell():
    for i in range(n - 1, -1, -1):
        G[i] = A[i] & B[i]
        P[i] = A[i] | B[i]

        H[i] = (negation(G[i]) & P[i])
        A_prim[i] = (negation((negation(G[i])) & P[i]))

        print("g_", i, "=", G[i])
        print("p_", i, "=", P[i])
        print("h_", i, "=", H[i])
        print("a_prim_", i, "=", A_prim[i])
        print(" ")

hashed_cell()


A_prim_buffer= [None] * 7
B_prim_buffer= [None] * 7

def controlled_buffer():
    for i in range(n - 1, -1, -1):
        if(K[i]==0):
            A_prim_buffer[i] = H[i]
            B_prim_buffer[i] = G[i]
        if(K[i]==1):
            A_prim_buffer[i] = A_prim[i]
            B_prim_buffer[i] = P[i]


A_prim_envelope = [None] * 7
B_prim_envelope = [None] * 7

G_prim_envelope = [None] * 7
P_prim_envelope = [None] * 7
H_prim_envelope = [None] * 7

def envelope_cell():
    for i in range(n - 1, 0, -1): # iterate from n-1 to 1
        A_prim_envelope[i] = A_prim_buffer[i]
        B_prim_envelope[i] = B_prim_buffer[i-1]

        G_prim_envelope[i] = A_prim_envelope[i] & B_prim_envelope[i]
        P_prim_envelope[i] = A_prim_envelope[i] | B_prim_envelope[i]
        H_prim_envelope[i] = negation(negation(G_prim_envelope[i]) & P_prim_envelope[i])

    A_prim_envelope[0] = A_prim_buffer[0]
    B_prim_envelope[0] = 0

    G_prim_envelope[0] = A_prim_envelope[0] & B_prim_envelope[0]
    P_prim_envelope[0] = A_prim_envelope[0] | B_prim_envelope[0]
    H_prim_envelope[0] = negation(negation(G_prim_envelope[0]) & P_prim_envelope[0])



