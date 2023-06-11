from Parametrized.calc_carry import calc_carry
from Parametrized.controlled_buffers import controlled_buffers
from Parametrized.dots import dots
from Parametrized.enveloped_cells import enveloped_cells
from Parametrized.hashed_cells import hashed_cells
from Parametrized.tristate_MUXs import tristate_MUXs
import csv

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


def int_to_list(A: int, B: int, K: int, n: int):
    A_list = []
    B_list = []
    K_list = []
    while A > 0:
        remainder = A % 2
        A_list.insert(0, remainder)
        A //= 2

    while len(A_list) < n:
        A_list.insert(0, 0)

    while B > 0:
        remainder = B % 2
        B_list.insert(0, remainder)
        B //= 2

    while len(B_list) < n:
        B_list.insert(0, 0)

    while K > 0:
        remainder = K % 2
        K_list.insert(0, remainder)
        K //= 2

    while len(K_list) < n:
        K_list.insert(0, 0)

    A_list.reverse()  # reverse to simulate binary number
    B_list.reverse()
    K_list.reverse()

    return A_list, B_list, K_list


def read():
    while True:
        n = int(input("Enter n="))
        A = input("Enter A=")
        B = input("Enter B=")
        K = input("Enter K=")

        A = list(map(int, str(A)))
        B = list(map(int, str(B)))
        K = list(map(int, str(K)))

        A.reverse()  # reverse to simulate binary number
        B.reverse()
        K.reverse()

        # checkA = check_AB(A, n)
        # checkB = check_AB(B, n)
        checkK = check(K, n)

        if checkK is True:
            return A, B, K, n


def negation(a):
    if a == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # # tuple!
    # A, B, K, n = read()
    #
    # # hashed_cells
    # hc = hashed_cells(n)
    # hc.operation(A, B)
    #
    # # buffer
    # cb = controlled_buffers(n)
    # cb.operation(hc.G, hc.P, hc.H, hc.A_prim, K)
    #
    # # enveloped_cells
    # ec = enveloped_cells(n)
    # ec.operation(cb.A_prim_buffer, cb.B_prim_buffer)
    #
    # #dots
    # d = dots(n)
    # lastRow = d.operation(ec.G_prim_envelope, ec.P_prim_envelope, hc.G, hc.P)
    #
    # #calculate carry
    # cc = calc_carry(n)
    # cc.operation(lastRow)
    #
    # # tristate MUXs
    # tMUX = tristate_MUXs(n)
    # tMUX.operation(cb.B_prim_buffer, cc.C_i_left, cc.C_i_right, hc.H, ec.H_prim_envelope, lastRow)
    #
    # # print score
    # tMUX.score()

    with open("test_results.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['N', 'K', 'for which H = H_prim'])
    x_equal_x_prim = False
    for n in range(1, 11, 1):
        for K in range(3, 2 ** (n - 1), 1):
            for A in range(1, 2 ** n, 1):
                for B in range(1, 2 ** n, 1):
                    # print(f"n = {n}")
                    # print(f"K = {K}")
                    # print(f"A = {A}")
                    # print(f"B = {B}")
                    # zamiana intow na odwrocone listy 0 i 1
                    A_list, B_list, K_list = int_to_list(A, B, K, n)

                    # hashed_cells
                    hc = hashed_cells(n)
                    hc.operation(A_list, B_list)  # z tego bierzemy hc.H G i P

                    # buffer
                    cb = controlled_buffers(n)
                    cb.operation(hc.G, hc.P, hc.H, hc.A_prim, K_list)

                    # enveloped_cells
                    ec = enveloped_cells(n)
                    ec.operation(cb.A_prim_buffer, cb.B_prim_buffer)  # z tego bierzemy ec.H_prim_envelope G i P

                    x_equal_x_prim = False
                    for i in range(0, n, 1):
                        x = hc.H[i]
                        x_prim = ec.H_prim_envelope[i]
                        if x == x_prim:
                            x_equal_x_prim = True
                            break

                    if not x_equal_x_prim:
                        break

                if not x_equal_x_prim:
                    break

            if x_equal_x_prim:
                with open("test_results.csv", 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([n, K])
