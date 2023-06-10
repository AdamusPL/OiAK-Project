from Utility import BinaryArithmeticUtils as Bin

from Parametrized.calc_carry import calc_carry
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


def read():
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
            return A,B,K,n


def negation(a):
    if a == 0:
        return 1
    if a == 1:
        return 0

    # never used
    return 33

if __name__ == '__main__':

    #tuple!
    A, B, K, n = read()

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
    d=dots(n)
    lastRow = d.operation(ec.G_prim_envelope, ec.P_prim_envelope, hc.G, hc.P)

    #calculate carry
    cc=calc_carry(n)
    cc.operation(lastRow)

    #tristate MUXs
    tMUX = tristate_MUXs(n)
    tMUX.operation(cb.B_prim_buffer,cc.C_i_left,cc.C_i_right,hc.H,ec.H_prim_envelope,lastRow)

    #print score
    tMUX.score()

