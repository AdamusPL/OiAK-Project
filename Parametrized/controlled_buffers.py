class controlled_buffers:
    def __init__(self, n):
        self.n=n
        self.A_prim_buffer = [None] * n
        self.B_prim_buffer = [None] * n

    def negation(self, a):
        if a == 0:
            return 1
        else:
            return 0

    def operation(self, G, P, H, A_prim, K):
        for i in range(self.n - 1, -1, -1):
            if (K[i] == 0):
                self.A_prim_buffer[i] = H[i]
                self.B_prim_buffer[i] = G[i]
            if (K[i] == 1):
                self.A_prim_buffer[i] = A_prim[i]
                self.B_prim_buffer[i] = P[i]
