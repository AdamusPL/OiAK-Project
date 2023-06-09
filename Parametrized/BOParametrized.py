from Utility import BinaryArithmeticUtils as Bin

from Parametrized.controlled_buffers import controlled_buffers
from Parametrized.dots import dots
from Parametrized.enveloped_cells import enveloped_cells
from Parametrized.hashed_cells import hashed_cells
from Parametrized.tristate_MUXs import tristate_MUXs


def check_AB(X, n):
    good = True  # when MSB equals 0, we accept everything

    for i in range(n - 1, -1, -1):
        if X[i] == 1:
            if i == 0:
                good = False
            continue
        else:
            break

    return good


def check(X, n):
    # check K
    good = True  # when MSB equals 0, we accept everything

    if X[n - 1] == 1:  # MSB can't equal 1
        good = False

    else:  # when MSB equals 0, check if they are other than 0,1,2
        for i in range(n - 2, -1, -1):
            if i >= 1 and X[i] != 0:  # if number larger than 3, then good
                return good
        good = False  # if not, then don't accept

    return good


def read(A, B, K, n):
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

        checkA = check_AB(A, n)
        checkB = check_AB(B, n)
        checkK = check(K, n)

        if checkA is True and checkB is True and checkK is True:
            break


def negation(a):
    if a == 0:
        return 1
    if a == 1:
        return 0

    # never used
    return 33

C_prev_left = [None] * 7
P_prev_left = [None] * 7
G_prev_left = [None] * 7
C_prev_right = [None] * 7
P_prev_right = [None] * 7
G_prev_right = [None] * 7
C_i_left = [None] * 7
C_i_right = [None] * 7

def calc_carry(G_and_prev_right_dot_LR, P_and_prev_right_dot_LR, G_and_prev_left_dot_LR,  P_and_prev_left_dot_LR):
    for i in range(0, n - 1, 1):  # from 0 to n-1
        if i == 0:
            C_prev_right[i] = G_and_prev_right_dot_LR[i]

        else:
            C_prev_right[i] = C_prev_right[i - 1]
        P_prev_right[i] = P_and_prev_right_dot_LR[i + 1]
        G_prev_right[i] = G_and_prev_right_dot_LR[i + 1]

        C_i_right[i] = (P_prev_right[i] & C_prev_right[i]) | G_prev_right[i]

        if i == 0:
            C_prev_left[i] = G_and_prev_left_dot_LR[i]
        else:
            C_prev_left[i] = C_prev_left[i - 1]
        P_prev_left[i] = P_and_prev_left_dot_LR[i + 1]
        G_prev_left[i] = G_and_prev_left_dot_LR[i + 1]

        C_i_left[i] = (P_prev_left[i] & C_prev_left[i]) | G_prev_left[i]


calc_carry()

if __name__ == '__main__':
    A, B, K, n = 0, 0, 0, 0

    #reading
    read(A, B, K, n)

    #hashed_cells
    hc = hashed_cells(n)
    hc.operation(A, B)

    #buffer
    cb = controlled_buffers(n)
    cb.operation(hc.G, hc.P, hc.H, hc.A_prim, K)

    #enveloped_cells
    ec = enveloped_cells(n)
    ec.operation(cb.A_prim_buffer, cb.B_prim_buffer)

    #dots
    d=dots()
    d.operation(ec.G_prim_envelope, ec.P_prim_envelope, hc.G, hc.P, )

    #tristate MUXs
    tMUX = tristate_MUXs(n)
    tMUX.operation(cb.B_prim_buffer,)

