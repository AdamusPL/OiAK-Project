

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

def hashed_cells():
    print("Hashed cells:")
    print("--------------")
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

hashed_cells()

A_prim_buffer= [None] * 7
B_prim_buffer= [None] * 7

def controlled_buffers():
    print("Controlled buffers:")
    print("--------------")
    for i in range(n - 1, -1, -1):
        if(K[i]==0):
            A_prim_buffer[i] = H[i]
            B_prim_buffer[i] = G[i]
        if(K[i]==1):
            A_prim_buffer[i] = A_prim[i]
            B_prim_buffer[i] = P[i]

        print("a_", i, "_prim", "=", A_prim_buffer[i])
        print("b_", i, "_next_prim", "=", B_prim_buffer[i])
        print(" ")

controlled_buffers()

A_prim_envelope = [None] * 7
B_prim_envelope = [None] * 7

G_prim_envelope = [None] * 7
P_prim_envelope = [None] * 7
H_prim_envelope = [None] * 7

def enveloped_cells():
    print("Enveloped cells:")
    print("--------------")
    for i in range(n - 1, 0, -1): # iterate from n-1 to 1
        A_prim_envelope[i] = A_prim_buffer[i]
        B_prim_envelope[i] = B_prim_buffer[i-1]

        G_prim_envelope[i] = A_prim_envelope[i] & B_prim_envelope[i]
        P_prim_envelope[i] = A_prim_envelope[i] | B_prim_envelope[i]
        H_prim_envelope[i] = negation(G_prim_envelope[i]) & P_prim_envelope[i]

        print("g_", i, "_prim", "=", G_prim_envelope[i])
        print("p_", i, "_prim", "=", P_prim_envelope[i])
        print("h_", i, "_prim", "=", H_prim_envelope[i])
        print(" ")

    A_prim_envelope[0] = A_prim_buffer[0]
    B_prim_envelope[0] = 0

    G_prim_envelope[0] = A_prim_envelope[0] & B_prim_envelope[0]
    P_prim_envelope[0] = A_prim_envelope[0] | B_prim_envelope[0]
    H_prim_envelope[0] = negation(G_prim_envelope[0]) & P_prim_envelope[0]

    print("g_", 0, "_prim", "=", G_prim_envelope[0])
    print("p_", 0, "_prim", "=", P_prim_envelope[0])
    print("h_", 0, "_prim", "=", H_prim_envelope[0])
    print(" ")

enveloped_cells()

# data from first row, input
G_left_dot_FR = [None] * 7
G_left_prev_dot_FR = [None] * 7
P_left_dot_FR = [None] * 7
P_left_prev_dot_FR = [None] * 7

G_right_dot_FR = [None] * 7
G_right_prev_dot_FR = [None] * 7
P_right_dot_FR = [None] * 7
P_right_prev_dot_FR = [None] * 7

#output
G_and_prev_left_dot_FR = [None] * 7
G_and_prev_right_dot_FR = [None] * 7
P_and_prev_left_dot_FR = [None] * 7
P_and_prev_right_dot_FR = [None] * 7

def first_dot_row():

    for i in range(n - 2, 0, -2): # iterate from 5 to 1 skip by 2 (double black dot)
        G_left_dot_FR[i]=G_prim_envelope[i]
        P_left_dot_FR[i]=P_prim_envelope[i]
        P_left_prev_dot_FR[i]=P_prim_envelope[i - 1]
        G_left_prev_dot_FR[i]=G_prim_envelope[i - 1]

        G_and_prev_left_dot_FR[i]=(P_left_dot_FR[i] & G_left_prev_dot_FR[i]) | G_left_dot_FR[i]
        P_and_prev_left_dot_FR[i]=(P_left_dot_FR[i] & P_left_prev_dot_FR[i])

        G_right_dot_FR[i]=G[i]
        P_right_dot_FR[i]=P[i]
        P_right_prev_dot_FR[i]=P[i - 1]
        G_right_prev_dot_FR[i]=G[i - 1]

        G_and_prev_right_dot_FR[i] = (P_right_dot_FR[i] & G_right_prev_dot_FR[i]) | G_right_dot_FR[i]
        P_and_prev_right_dot_FR[i] = (P_right_dot_FR[i] & P_right_prev_dot_FR[i])

    for i in range(n - 1, -1, -2): # iterate from 6 to 0 skip by 2 (white dot)
        G_left_dot_FR[i] = G_prim_envelope[i]
        P_left_dot_FR[i] = P_prim_envelope[i]

        G_and_prev_left_dot_FR[i]=G_left_dot_FR[i]
        P_and_prev_left_dot_FR[i]=P_left_dot_FR[i]

        G_and_prev_right_dot_FR[i] = G[i]
        P_and_prev_right_dot_FR[i] = P[i]

first_dot_row()

# data from second row
G_left_dot_SR = [None] * 7
G_left_prev_dot_SR = [None] * 7
P_left_dot_SR = [None] * 7
P_left_prev_dot_SR = [None] * 7

G_right_dot_SR = [None] * 7
G_right_prev_dot_SR = [None] * 7
P_right_dot_SR = [None] * 7
P_right_prev_dot_SR = [None] * 7

#output from second row
G_and_prev_left_dot_SR = [None] * 7
G_and_prev_right_dot_SR = [None] * 7
P_and_prev_left_dot_SR = [None] * 7
P_and_prev_right_dot_SR = [None] * 7

# cos nie tak z black dotem na 3. bicie od prawej
def second_dot_row():
    i=n-1
    while(i!=1):  # list[6,3,2]
        G_left_dot_SR[i] = G_and_prev_left_dot_FR[i]  # taking data from previous row
        P_left_dot_SR[i] = P_and_prev_left_dot_FR[i]

        if i==3:
            G_left_prev_dot_SR[i] = G_and_prev_left_dot_FR[i - 2]
            P_left_prev_dot_SR[i] = P_and_prev_left_dot_FR[i - 2]

        else:
            G_left_prev_dot_SR[i] = G_and_prev_left_dot_FR[i - 1]
            P_left_prev_dot_SR[i] = P_and_prev_left_dot_FR[i - 1]

        G_and_prev_left_dot_SR[i] = (P_left_dot_SR[i] & G_left_prev_dot_SR[i]) | G_left_dot_SR[i]
        P_and_prev_left_dot_SR[i] = (P_left_dot_SR[i] & P_left_prev_dot_SR[i])

        G_right_dot_SR[i] = G_and_prev_right_dot_FR[i]  # taking data from previous row
        P_right_dot_SR[i] = P_and_prev_right_dot_FR[i]

        if i==3:
            G_right_prev_dot_SR[i] = G_and_prev_right_dot_FR[i - 2]
            P_right_prev_dot_SR[i] = P_and_prev_right_dot_FR[i - 2]

        else:
            G_right_prev_dot_SR[i] = G_and_prev_right_dot_FR[i - 1]
            P_right_prev_dot_SR[i] = P_and_prev_right_dot_FR[i - 1]

        G_and_prev_right_dot_SR[i] = (P_right_dot_SR[i] & G_right_prev_dot_SR[i]) | G_right_dot_SR[i]
        P_and_prev_right_dot_SR[i] = (P_right_dot_SR[i] & P_right_prev_dot_SR[i])

        if i==6:
            i-=2
        i-=1

    i=n-2
    while(i!=-1): #list[5,4,1,0]
        G_left_dot_FR[i] = G_prim_envelope[i]
        P_left_dot_FR[i] = P_prim_envelope[i]

        G_and_prev_left_dot_SR[i] = G_and_prev_left_dot_FR[i]
        P_and_prev_left_dot_SR[i] = P_and_prev_left_dot_FR[i]

        G_and_prev_right_dot_SR[i] = G_and_prev_right_dot_FR[i]
        P_and_prev_right_dot_SR[i] = P_and_prev_right_dot_FR[i]

        if i==4: # jump over 2
            i-=2
        i-=1

second_dot_row()

# data from second row
G_left_dot_TR = [None] * 7
G_left_prev_dot_TR = [None] * 7
P_left_dot_TR = [None] * 7
P_left_prev_dot_TR = [None] * 7

G_right_dot_TR = [None] * 7
G_right_prev_dot_TR = [None] * 7
P_right_dot_TR = [None] * 7
P_right_prev_dot_TR = [None] * 7

#output from second row
G_and_prev_left_dot_TR = [None] * 7
G_and_prev_right_dot_TR = [None] * 7
P_and_prev_left_dot_TR = [None] * 7
P_and_prev_right_dot_TR = [None] * 7

def third_row():
    offset=3 # bring score from 3 prev higher black dots
    for i in range(n - 1, 3, -1): # list[6,5,4]
        G_left_dot_TR[i]=G_and_prev_left_dot_SR[i]
        P_left_dot_TR[i]=P_and_prev_left_dot_SR[i]

        G_left_prev_dot_TR[i] = G_and_prev_left_dot_SR[i-offset]
        P_left_prev_dot_TR[i] = P_and_prev_left_dot_SR[i-offset]

        G_and_prev_left_dot_TR[i] = (P_left_dot_TR[i] & G_left_prev_dot_TR[i]) | G_left_dot_TR[i]
        P_and_prev_left_dot_TR[i] = (P_left_dot_TR[i] & P_left_prev_dot_TR[i])

        G_right_dot_TR[i] = G_and_prev_right_dot_SR[i]
        P_right_dot_TR[i] = P_and_prev_right_dot_SR[i]

        G_right_prev_dot_TR[i] = G_and_prev_right_dot_SR[i - offset]
        P_right_prev_dot_TR[i] = P_and_prev_right_dot_SR[i - offset]

        G_and_prev_right_dot_TR[i] = (P_right_dot_TR[i] & G_right_prev_dot_TR[i]) | G_right_dot_TR[i]
        P_and_prev_right_dot_TR[i] = (P_right_dot_TR[i] & P_right_prev_dot_TR[i])

        offset-=1

    for i in range(n - 4, -1, -1):
        G_and_prev_left_dot_TR[i] = G_and_prev_left_dot_SR[i]
        P_and_prev_left_dot_TR[i] = P_and_prev_left_dot_SR[i]

        G_and_prev_right_dot_TR[i] = G_and_prev_right_dot_SR[i]
        P_and_prev_right_dot_TR[i] = P_and_prev_right_dot_SR[i]

third_row()
print("Cos")

C_prev_left = [None] * 7
P_prev_left = [None] * 7
G_prev_left = [None] * 7
C_prev_right = [None] * 7
P_prev_right = [None] * 7
G_prev_right = [None] * 7
C_i_left = [None] * 7
C_i_right= [None] * 7
def calc_carry():
    for i in range(0,n-1,1): # from 0 to 5
        if i==0:
            C_prev_right[i]=G_and_prev_right_dot_TR[i]

        else:
            C_prev_right[i]=C_prev_right[i-1]
        P_prev_right[i]=P_and_prev_right_dot_TR[i+1]
        G_prev_right[i]=G_and_prev_right_dot_TR[i+1]

        C_i_right[i]=(P_prev_right[i] & C_prev_right[i]) | G_prev_right[i]

        if i==0:
            C_prev_left[i] = G_and_prev_left_dot_TR[i]
        else:
            C_prev_left[i] = C_prev_left[i - 1]
        P_prev_left[i] = P_and_prev_left_dot_TR[i + 1]
        G_prev_left[i] = G_and_prev_left_dot_TR[i + 1]

        C_i_left[i] = (P_prev_left[i] & C_prev_left[i]) | G_prev_left[i]

calc_carry()

S = [None] * 7

def tristate_MUXs():
    if(B_prim_buffer[n-1]==0):
        C_out=C_i_left[n-2]

    if(B_prim_buffer[n-1]==1):
        C_out=C_i_right[n-2]

    for i in range(n-1, 1, -1):
        if(C_out==0):
            S[i]=H[i]^C_i_right[i-2]
        if(C_out==1):
            S[i]=H_prim_envelope[i]^C_i_left[i-2]

    #S1
    if (C_out == 0):
        S[1] = H[1] ^ G_and_prev_right_dot_TR[0]
    if (C_out == 1):
        S[1] = H_prim_envelope[1] ^ G_and_prev_left_dot_TR[0]

    #S0
    if C_out==0:
        S[0]=H[0]

    if C_out==1:
        S[0]=H_prim_envelope[0]

tristate_MUXs()

S.reverse()
print("Wynik=", S)