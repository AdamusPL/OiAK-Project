from Parametrized.dot import dot


class white_dot(dot):
    def __init__(self):
        self.g_i_i_delay_left = [None]
        self.p_i_i_delay_left = [None]
        self.g_i_i_delay_right = [None]
        self.p_i_i_delay_right = [None]

    def operation(self, g_i_left, g_i_right, p_i_left, p_i_right):
        self.g_i_i_delay_left = g_i_left
        self.p_i_i_delay_left = p_i_left

        self.g_i_i_delay_right = g_i_right
        self.p_i_i_delay_right = p_i_right
