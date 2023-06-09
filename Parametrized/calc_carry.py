class calc_carry:
    def __init__(self, n):
        self.C_prev_left = [None] * n
        self.P_prev_left = [None] * n
        self.G_prev_left = [None] * n
        self.C_prev_right = [None] * n
        self.P_prev_right = [None] * n
        self.G_prev_right = [None] * n
        self.C_i_left = [None] * n
        self.C_i_right = [None] * n

    def operation(self, G_and_prev_right_dot_LR, P_and_prev_right_dot_LR, G_and_prev_left_dot_LR,  P_and_prev_left_dot_LR):
        for i in range(0, n - 1, 1):  # from 0 to n-1
            if i == 0:
                self.C_prev_right[i] = G_and_prev_right_dot_LR[i]

            else:
                self.C_prev_right[i] = self.C_prev_right[i - 1]
            self.P_prev_right[i] = P_and_prev_right_dot_LR[i + 1]
            self.G_prev_right[i] = G_and_prev_right_dot_LR[i + 1]

            self.C_i_right[i] = (self.P_prev_right[i] & self.C_prev_right[i]) | self.G_prev_right[i]

            if i == 0:
                self.C_prev_left[i] = G_and_prev_left_dot_LR[i]
            else:
                self.C_prev_left[i] = self.C_prev_left[i - 1]
            self.P_prev_left[i] = P_and_prev_left_dot_LR[i + 1]
            self.G_prev_left[i] = G_and_prev_left_dot_LR[i + 1]

            self.C_i_left[i] = (self.P_prev_left[i] & self.C_prev_left[i]) | self.G_prev_left[i]
