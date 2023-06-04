class controlled_buffers:
    def __init__(self,n):
        self.A_prim_buffer = [None] * n
        self.B_prim_buffer = [None] * n

    def negation(self,a):
        if a == 0:
            return 1
        if a == 1:
            return 0

        # never used
        return 33

    def operation(self, G, P, H, A_prim, K):
        print("Controlled buffers:")
        print("--------------")
        for i in range(self.n - 1, -1, -1):
            if (K[i] == 0):
                self.A_prim_buffer[i] = H[i]
                self.B_prim_buffer[i] = G[i]
            if (K[i] == 1):
                self.A_prim_buffer[i] = A_prim[i]
                self.B_prim_buffer[i] = P[i]

            print("a_", i, "_prim", "=", self.A_prim_buffer[i])
            print("b_", i, "_next_prim", "=", self.B_prim_buffer[i])
            print(" ")