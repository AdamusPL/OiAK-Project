from Parametrized.dot import dot


class double_black_dot(dot):
    def __init__(self):
        self.g_i_i_prev_left = [None]
        self.p_i_i_prev_left = [None]
        self.g_i_i_prev_right = [None]
        self.p_i_i_prev_right = [None]

    def operation(self, g_i_prev_left, g_i_left, p_i_prev_left, p_i_left, g_i_prev_right, g_i_right, p_i_prev_right, p_i_right):
        self.g_i_i_prev_left = (p_i_left & g_i_prev_left) | g_i_left
        self.p_i_i_prev_left = p_i_left & p_i_prev_left

        self.g_i_i_prev_right = (p_i_right & g_i_prev_right) | g_i_right
        self.p_i_i_prev_right = p_i_right & p_i_prev_right
