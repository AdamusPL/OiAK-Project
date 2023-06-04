class second_dot_row:
    def __init__(self,n):
        self.G_left_dot = [None] * n
        self.G_left_prev_dot = [None] * n
        self.P_left_dot = [None] * n
        self.P_left_prev_dot = [None] * n

        self.G_right_dot = [None] * n
        self.G_right_prev_dot = [None] * n
        self.P_right_dot = [None] * n
        self.P_right_prev_dot = [None] * n

        # output from second row
        self.G_and_prev_left_dot_output = [None] * n
        self.G_and_prev_right_dot_output = [None] * n
        self.P_and_prev_left_dot_output = [None] * n
        self.P_and_prev_right_dot_output = [None] * n

    def negation(self,a):
        if a == 0:
            return 1
        if a == 1:
            return 0

        # never used
        return 33

    def operation(self, G_left_dot, G_left_prev_dot, P_left_dot, P_left_prev_dot, G_right_dot, G_right_prev_dot,
                  P_right_dot, P_right_prev_dot):
        n=self.n

        if n%2 == 0:
            offsetBlack1=n-1
            offsetBlack2=0
            offsetWhite1=n-2
            offsetWhite2=-1

        else:
            offsetBlack1=n-2
            offsetBlack2 = -1
            offsetWhite1=n-1
            offsetWhite2 = 0

        for i in range(offsetBlack1, offsetBlack2, -2):  # iterate, skip by 2 (double black dot)
            self.G_left_dot[i] = G_prim_envelope[i]
            self.P_left_dot[i] = P_prim_envelope[i]
            self.P_left_prev_dot[i] = P_prim_envelope[i - 1]
            self.G_left_prev_dot[i] = G_prim_envelope[i - 1]

            self.G_and_prev_left_dot_output[i] = (self.P_left_dot[i] & self.G_left_prev_dot[i]) | self.G_left_dot[i]
            self.P_and_prev_left_dot_output[i] = (self.P_left_dot[i] & self.P_left_prev_dot[i])

            self.G_right_dot[i] = G[i]
            self.P_right_dot[i] = P[i]
            self.P_right_prev_dot[i] = P[i - 1]
            self.G_right_prev_dot[i] = G[i - 1]

            self.G_and_prev_right_dot_output[i] = (self.P_right_dot[i] & self.G_right_prev_dot[i]) | self.G_right_dot[i]
            self.P_and_prev_right_dot_output[i] = (self.P_right_dot[i] & self.P_right_prev_dot[i])

        for i in range(offsetWhite1, offsetWhite2, -2):  # iterate, skip by 2 (white dot)
            self.G_left_dot[i] = G_prim_envelope[i]
            self.P_left_dot[i] = P_prim_envelope[i]

            self.G_and_prev_left_dot_output[i] = self.G_left_dot[i]
            self.P_and_prev_left_dot_output[i] = self.P_left_dot[i]

            self.G_and_prev_right_dot_output[i] = G[i]
            self.P_and_prev_right_dot_output[i] = P[i]