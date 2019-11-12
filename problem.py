import numpy as np
import  math

class Problem:

    def __init__(self,
                 n,
                 m,
                 a_i,
                 b_i,
                 d_i,
                 p_i,
                 w_kl,
                 f_ij):

        self.n = n
        self.m = m
        self.a_i = a_i
        self.b_i = b_i
        self.d_i = d_i
        self.p_i = p_i
        self.w_kl = w_kl
        self.f_ij = f_ij

    def __init__(self,
                 n,
                 m):

        self.n = n
        self.m = m


    def create_data(self):
        # parameter
        self.a_i = np.empty([self.n])
        self.b_i = np.empty([self.n])
        self.d_i = np.empty([self.n])
        self.p_i = np.empty([self.n])
        self.f_ij = np.empty([self.n, self.n])
        des = 0.8
        # setting of random values
        for i in range(self.n):
            self.a_i[i] = np.random.uniform(1, self.n*70/self.m)
            self.b_i[i] = self.a_i[i] + np.random.uniform(45,74)
            self.d_i[i] = des*(self.a_i[i]+self.b_i[i])
            self.p_i[i] = np.random.uniform(10,14)
            for j in range(self.n):
                if (self.a_i[i] < self.a_i[j]):
                    self.f_ij[i][j] = np.random.random_integers(6, 60)
                else:
                    self.f_ij[i][j] = 0
        # gate distances
        self.createDistanceMatrix()
        # print(self.a_i) # Todo delete if not necessary anymore


    # distance matrix
    def createDistanceMatrix(self):
        self.w_kl = np.empty([self.m,self.m])
        for k in range(self.m):
            kk = k +1
            for l in range(self.m):
                ll = l+1
                if (kk % 2 == 0) == (ll % 2 == 0):
                    self.w_kl[k][l] = math.sqrt(((kk - ll)*0.5) ** 2)
                elif (kk%2==0):
                    self.w_kl[k][l] = 3 + math.sqrt(((kk - 2)*0.5) ** 2) + math.sqrt(((ll - 1)*0.5) ** 2)
                elif (ll%2==0):
                    self.w_kl[k][l] = 3 + math.sqrt(((ll - 2)*0.5) ** 2) + math.sqrt(((kk - 1)*0.5) ** 2)
                else:
                    self.w_kl[k][l] = math.sqrt(((kk - ll) * 0.5) ** 2)
        # print(self.w_kl) Todo delete if not necessary anymore


# subroutines

    def shift_left(self, gate, flight):
        return 'hello world'

    def shift_right(self):
       return 'hello world'

    def shift_interval(self):
        return 'hello world'

    def attempt_shift_interval(self):
        return 'hello world'

    def attempt_shift_interval_right(self):
        return 'hello world'

    def insert(self):
        return 'hello world'

    def tabu_search(self):
        return 'hello world'

    def genetic_algorithm(self):
        return 'hello world'

    def memetic_algorithm(self):
        return 'hello world'

    def solve(self):
        return 'hello world'


