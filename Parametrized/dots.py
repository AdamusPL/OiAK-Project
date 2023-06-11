import math

from Parametrized.double_black_dot import double_black_dot
from Parametrized.white_dot import white_dot


class dots:
    def __init__(self, n):
        self.n = n
        self.rowList = []

    def negation(self, a):
        if a == 0:
            return 1
        else:
            return 0

    def operation(self, G_prim_envelope, P_prim_envelope, G, P):
        global numberOfRows, prevList
        n = self.n

        numberOfRows = math.ceil(math.log2(n))

        # phase of creating dots

        for i in range(1, numberOfRows + 1, 1):

            lista = [None] * n
            dot = False  # False - white dot, True - black dot

            for j in range(1, n + 1, 1):
                if dot is False:
                    wd = white_dot()
                    lista[j-1] = wd
                else:
                    bd = double_black_dot()
                    lista[j-1] = bd

                if j % (2 ** (i - 1)) == 0:
                    dot = not dot

            self.rowList.append(lista)

        curRow = 1

        # phase of calculating inside dots

        for sublist in self.rowList:

            j = 0
            offset = 1
            prevList = self.rowList[curRow-2]

            for obj in sublist:
                if isinstance(obj, double_black_dot):

                    # in first row we take values in other way
                    if curRow == 1:

                        offset = 1

                        obj.operation(G_prim_envelope[j - 1], G_prim_envelope[j], P_prim_envelope[j - 1], P_prim_envelope[j], G[j - 1], G[j], P[j - 1], P[j])

                    else:  # somehow take data from previous row
                        prevDot = prevList[j - offset]  # dot from previous position
                        aboveDot = prevList[j]  # dot above actual dot

                        obj.operation(prevDot.g_i_i_prev_left, aboveDot.g_i_i_prev_left, prevDot.p_i_i_prev_left, aboveDot.p_i_i_prev_left, prevDot.g_i_i_prev_right, aboveDot.g_i_i_prev_right, prevDot.p_i_i_prev_right, aboveDot.p_i_i_prev_right)

                        offset += 1

                elif isinstance(obj, white_dot):
                    if curRow == 1:

                        obj.operation(P_prim_envelope[j], G_prim_envelope[j], P[j], G[j])

                    else:  # somehow take data from previous row
                        offset=1

                        aboveDot = prevList[j]  # dot above actual dot

                        obj.operation(aboveDot.p_i_i_prev_left, aboveDot.g_i_i_prev_left, aboveDot.p_i_i_prev_right, aboveDot.g_i_i_prev_right)

                j += 1
            curRow += 1

        return self.rowList[-1]
