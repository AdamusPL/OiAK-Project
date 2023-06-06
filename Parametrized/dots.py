from Parametrized.black_dot import black_dot

class dots:
    def __init__(self, n):
        self.double_black_dot_list=[]

    def negation(self, a):
        if a == 0:
            return 1
        if a == 1:
            return 0

        # never used
        return 33

    def operation(self, G_prim_envelope, P_prim_envelope, G, P):
        global numberOfRows
        n = self.n

        found=False
        i=0

        while(found is False):
            if(2^i <= n < 2^i+1):
               found=True
               numberOfRows = i
            i+=1


        if n % 2 == 0:
            offsetBlack1 = n - 1
            offsetBlack2 = 0
            offsetWhite1 = n - 2
            offsetWhite2 = -1

        else:
            offsetBlack1 = n - 2
            offsetBlack2 = -1
            offsetWhite1 = n - 1
            offsetWhite2 = 0

        for i in range(numberOfRows, 0, -1):
            for i in range():


        for i in range(offsetBlack1, offsetBlack2, -2):  # iterate, skip by 2 (double black dot)

            list=[]
            bdL = black_dot()
            bdL.operation(G_prim_envelope[i], P_prim_envelope[i], P_prim_envelope[i - 1], G_prim_envelope[i - 1])
            list.append(bdL)

            bdP = black_dot()
            bdP.operation(G[i], P[i], P[i - 1], G[i - 1])
            list.append(bdP)

            self.double_black_dot_list.append(list)

        for i in range(offsetWhite1, offsetWhite2, -2):  # iterate, skip by 2 (white dot)
            self.G_left_dot[i] = G_prim_envelope[i]
            self.P_left_dot[i] = P_prim_envelope[i]

            self.G_and_prev_left_dot_output[i] = self.G_left_dot[i]
            self.P_and_prev_left_dot_output[i] = self.P_left_dot[i]

            self.G_and_prev_right_dot_output[i] = G[i]
            self.P_and_prev_right_dot_output[i] = P[i]
