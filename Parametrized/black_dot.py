class black_dot():
    def __init__(self):
        self.g_i_i_prev = [None]
        self.p_i_i_prev = [None]

    def operation(self, g_i, g_i_prev, p_i, p_i_prev):
        self.g_i_i_prev = (p_i & g_i_prev) | g_i
        self.p_i_i_prev = p_i & p_i_prev
