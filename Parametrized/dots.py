from Parametrized.double_black_dot import double_black_dot
from Parametrized.white_dot import white_dot


class dots:
    def __init__(self, n):
        self.rowList=[]

    def negation(self, a):
        if a == 0:
            return 1
        if a == 1:
            return 0

        # never used
        return 33

    def operation(self, G_prim_envelope, P_prim_envelope, G, P):
        global numberOfRows
        n = self.n

        found=False
        i=0

        while(found is False):
            if(2**i <= n < 2**(i+1)):
               found=True
               numberOfRows = i
            i+=1

        # phase of creating dots
        dot = False # False - white dot, True - black dot

        for i in range(1, numberOfRows+1, 1):
            list=[]
            for j in range(1, n+1, 1):
                if dot is False:
                    wd = white_dot()
                    list[j-1]=wd
                else:
                    bd = double_black_dot()
                    list[j-1]=bd

                if j % 2 ** (i-1)==0:
                    dot=True

            self.rowList.append(list)

        curRow=1
        j=0

        for sublist in self.rowList:

            offset=1
            prevList=sublist[offset-2]

            for obj in sublist:
                if(isinstance(obj,double_black_dot)):
                    if curRow==1:

                        offset=1

                        obj.operation(G_prim_envelope[j-1], G_prim_envelope[j], P_prim_envelope[j-1], P_prim_envelope[j],
                                      G[j-1], G[j], P[j-1], P[j])

                    else: # tu jakos wziac z poprzedniego etapu te dane
                        obj.operation(G_i_i_prev_left[j - offset], G_i_i_prev_left[j], P_i_i_prev_left[j - offset], P_i_i_prev_left[j],
                                      G_i_i_prev_right[j - offset], G_i_i_prev_right[j], P_i_i_prev_right[j - offset], P_i_i_prev_right[j])

                        offset+=1


                elif(isinstance(obj,white_dot)):
                    if curRow == 1:
                        obj.operation()

                    else:


            curRow+=1



