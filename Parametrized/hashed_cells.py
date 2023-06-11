class hashed_cells:
    def __init__(self, n):
        self.G = [None] * n
        self.P = [None] * n
        self.H = [None] * n
        self.A_prim = [None] * n
        self.n=n

    def negation(self, a):
        if a == 0:
            return 1
        else:
            return 0

    def operation(self, A, B):
        for i in range(self.n - 1, -1, -1):
            self.G[i] = A[i] & B[i]
            self.P[i] = A[i] | B[i]

            self.H[i] = (self.negation(self.G[i]) & self.P[i])
            self.A_prim[i] = (self.negation((self.negation(self.G[i])) & self.P[i]))
