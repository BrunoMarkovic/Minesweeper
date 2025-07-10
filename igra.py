import config
import numpy as np
import random



class Igra:
    @staticmethod
    def is_valid_position(x, y):
        return 0 <= x < config.NOFROWS and 0 <= y < config.NOFCOLLUMNS

    @staticmethod
    def print_matrix(matrix):
        for i in range(config.NOFROWS):
            for j in range(config.NOFCOLLUMNS):
                print(matrix[i, j], end=" ")
            print()


    def check_for_mines(self, x, y):
        if self.secondmatrix[x,y] == 9:
            pass
        else:
            if self.matrica[x,y] == 0:
                self.secondmatrix[x, y] = 9  # nek za pocetak 9 znaci da je otvoreno
                self.openFieldsCount += 1
                directions = [
                                (-1, -1),
                                (-1, 0), (-1, 1),  # Top-left, Top, Top-right
                              (0, -1), (0, 1),  # Left, Right
                              (1, -1),
                                (1, 0), (1, 1)
                                 ]  # Bottom-left, Bottom, Bottom-right
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if Igra.is_valid_position(nx, ny) and self.secondmatrix[nx][ny] == 0:
                        Igra.check_for_mines(self, nx, ny)
            else:
                self.openFieldsCount += 1
                self.secondmatrix[x, y] = self.matrica[x, y]


    def count_surrounding_mines(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
                      (0, -1),         (0, 1),     # Left, Right
                      (1, -1), (1, 0), (1, 1)]     # Bottom-left, Bottom, Bottom-right
        count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if Igra.is_valid_position(nx, ny) and self.matrica[nx][ny] == -1:
                count += 1

        return count

    def __init__(self):
        self.matrica = np.zeros((config.NOFROWS, config.NOFCOLLUMNS), dtype=int)
        self.openFieldsCount = 0
        bombice = config.BROJBOMBICA
        brojac = 0

        while brojac < bombice:
            x = random.randint(0,config.NOFROWS - 1)
            y = random.randint(0,config.NOFCOLLUMNS - 1)
            if self.matrica[x, y] != -1:
                self.matrica[x,y] = -1
                brojac += 1

        for i in range(config.NOFROWS):
            for j in range(config.NOFCOLLUMNS):
                if self.matrica[i,j] != -1:
                    broj_mina = self.count_surrounding_mines(i,j)
                    self.matrica[i,j] = broj_mina


        self.secondmatrix = np.zeros((config.NOFROWS, config.NOFCOLLUMNS), dtype=int)
        #Igra.print_matrix(self.matrica)

#        Igra.print_matrix(self.matrica)
#        br1 = int(input("koji broj zelite pogledati"))
#        br2 = int(input("koji stupac zelite pogledati"))
#        Igra.check_for_mines(self,br1,br2)
#        Igra.print_matrix(self.secondmatrix)







