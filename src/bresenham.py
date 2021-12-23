from rasterizacao import Rasterizacao


class Bresenham(Rasterizacao):
    def __init__(self, ponto1, ponto2):
        super().__init__([ponto1, ponto2])
        
        self.x1 = ponto1[0]
        self.y1 = ponto1[1]
        
        self.x2 = ponto2[0]
        self.y2 = ponto2[1]
        
        self.pontos = []
        
        self.troca_x = False
        self.troca_y = False
        self.troca_xy = False
        
        
        self.checar_octante()
        
        x = self.x1
        y = self.y1
        
        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1
        
        m = delta_y/delta_x
        e = m - (1/2)
        
        self.pontos.append([x, y])
        
        while x < self.x2:
            if e >= 0:
                y += 1
                e -= 1
            x += 1
            e += m
            self.pontos.append([x, y])
            
        self.reflexao(self.pontos)
        
        self.saida = self.pontos
            
    def checar_octante(self):
        
        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1
        
        m = delta_y/delta_x
        
        if m > 1 or m < -1:
            [self.x1, self.y1] = [self.y1, self.x1]
            [self.x2, self.y2] = [self.y2, self.x2]
            self.troca_xy = True
            
        if self.x1 > self.x2:
            self.x1 = -self.x1
            self.x2 = -self.x2
            self.troca_x = True
            
        if self.y1 > self.y2:
            self.y1 = -self.y1
            self.y2 = -self.y2
            self.troca_y = True    
    
    def reflexao(self, pts: list):
        if self.troca_y:
            for pt in self.pontos:
                pt[1] = -pt[1]
                
        if self.troca_x:
            for pt in self.pontos:
                pt[0] = -pt[0]
                
        if self.troca_xy:
            for pt in self.pontos:
                [pt[0], pt[1]] = [pt[1], pt[0]]
                
                