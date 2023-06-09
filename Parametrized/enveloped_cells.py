class enveloped_cells:
    def __init__(self,n):
        self.n=n
        self.A_prim_envelope = [None] * n
        self.B_prim_envelope = [None] * n

        self.G_prim_envelope = [None] * n
        self.P_prim_envelope = [None] * n
        self.H_prim_envelope = [None] * n

    def negation(self,a):
        if a == 0:
            return 1
        if a == 1:
            return 0

        # never used
        return 33

    def operation(self, A_prim_buffer, B_prim_buffer):
        print("Enveloped cells:")
        print("--------------")
        for i in range(self.n - 1, 0, -1):  # iterate from n-1 to 1
            self.A_prim_envelope[i] = A_prim_buffer[i]
            self.B_prim_envelope[i] = B_prim_buffer[i - 1]

            self.G_prim_envelope[i] = self.A_prim_envelope[i] & self.B_prim_envelope[i]
            self.P_prim_envelope[i] = self.A_prim_envelope[i] | self.B_prim_envelope[i]
            self.H_prim_envelope[i] = self.negation(self.G_prim_envelope[i]) & self.P_prim_envelope[i]

            print("g_", i, "_prim", "=", self.G_prim_envelope[i])
            print("p_", i, "_prim", "=", self.P_prim_envelope[i])
            print("h_", i, "_prim", "=", self.H_prim_envelope[i])
            print(" ")

        self.A_prim_envelope[0] = A_prim_buffer[0]
        self.B_prim_envelope[0] = 0

        self.G_prim_envelope[0] = self.A_prim_envelope[0] & self.B_prim_envelope[0]
        self.P_prim_envelope[0] = self.A_prim_envelope[0] | self.B_prim_envelope[0]
        self.H_prim_envelope[0] = self.negation(self.G_prim_envelope[0]) & self.P_prim_envelope[0]

        print("g_", 0, "_prim", "=", self.G_prim_envelope[0])
        print("p_", 0, "_prim", "=", self.P_prim_envelope[0])
        print("h_", 0, "_prim", "=", self.H_prim_envelope[0])
        print(" ")