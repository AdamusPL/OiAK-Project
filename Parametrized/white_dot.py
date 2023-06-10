from Parametrized.dot import dot


class white_dot(dot):

    def operation(self, p_i_left, g_i_left, p_i_right, g_i_right):
        self.g_i_i_prev_left = g_i_left
        self.p_i_i_prev_left = p_i_left

        self.g_i_i_prev_right = g_i_right
        self.p_i_i_prev_right = p_i_right
