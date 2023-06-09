class hashed_cells:
    def __init__(self,n):
        self.G = [None] * n
        self.P = [None] * n
        self.H = [None] * n
        self.A_prim = [None] * n
        self.n=n

    def negation(self,a):
        if a == 0:
            return 1
        if a == 1:
            return 0

        # never used
        return 33

    def operation(self,A,B):
        print("Hashed cells:")
        print("--------------")
        for i in range(self.n - 1, -1, -1):
            self.G[i] = A[i] & B[i]
            self.P[i] = A[i] | B[i]

            self.H[i] = (self.negation(self.G[i]) & self.P[i])
            self.A_prim[i] = (self.negation((self.negation(self.G[i])) & self.P[i]))

            print("g_", i, "=", self.G[i])
            print("p_", i, "=", self.P[i])
            print("h_", i, "=", self.H[i])
            print("a_prim_", i, "=", self.A_prim[i])
            print(" ")