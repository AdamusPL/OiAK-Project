class tristate_MUXs:
    def __init__(self,n):
        self.n=n
        self.S = [None] * n

    def negation(self,a):
        if a == 0:
            return 1
        else:
            return 0

    def operation(self,B_prim_buffer,C_i_left,C_i_right,H,H_prim_envelope,lastRow):
        n=self.n
        if (B_prim_buffer[-1] == 0):
            C_out = C_i_left[-1]

        else:
            C_out = C_i_right[-1]

        for i in range(1, n, 1):
            if (C_out == 0):
                self.S[i] = H[i] ^ C_i_right[i]
            else:
                self.S[i] = H_prim_envelope[i] ^ C_i_left[i]

        # S0
        if C_out == 0:
            self.S[0] = H[0]

        else:
            self.S[0] = H_prim_envelope[0]

    def score(self):
        self.S.reverse()
        print("Wynik=", self.S)