class tristate_MUXs:
    def __init__(self,n):
        self.S = [None] * 7

    def negation(self,a):
        if a == 0:
            return 1
        if a == 1:
            return 0

        # never used
        return 33

    def operation(self,B_prim_buffer,C_i_left,C_i_right,H,H_prim_envelope,G_and_prev_right_dot,G_and_prev_left_dot):
        n=self.n
        if (B_prim_buffer[n - 1] == 0):
            C_out = C_i_left[n - 2]

        if (B_prim_buffer[n - 1] == 1):
            C_out = C_i_right[n - 2]

        for i in range(n - 1, 1, -1):
            if (C_out == 0):
                self.S[i] = H[i] ^ C_i_right[i - 2]
            if (C_out == 1):
                self.S[i] = H_prim_envelope[i] ^ C_i_left[i - 2]

        # S1
        if (C_out == 0):
            self.S[1] = H[1] ^ G_and_prev_right_dot[0]
        if (C_out == 1):
            self.S[1] = H_prim_envelope[1] ^ G_and_prev_left_dot[0]

        # S0
        if C_out == 0:
            self.S[0] = H[0]

        if C_out == 1:
            self.S[0] = H_prim_envelope[0]

    def score(self):
        self.S.reverse()
        print("Wynik=", self.S)