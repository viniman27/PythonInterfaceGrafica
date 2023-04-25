import time
import os


class Cronometro:
    
    def __init__(self,seg = 0, min = 0, horas = 0):
        
        self.seg = seg
        self.min = min
        self.horas = horas
        
    def __repr__(self):
        
        return f'{self.horas:02d}:{self.min:02d}:{self.seg:02d}'
    
    def incremento(self):
        
        self.seg += 1
        
        if self.seg >= 60:
            
            self.seg= 0
            self.min += 1
        
        if self.min >= 60:
            
            self.min = 0
            self.horas += 1
            
            
    def start(self):
        
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)
            
cronometro1 = Cronometro()
cronometro1.start()        
