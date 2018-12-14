import sys
import random
from lexer import analise_lexica, tokens_da_linguagem
from myparser import analise_sintatica
from simbolos import tabela, adicionar, ler

class Construcao:
  def interpretar(self):
      return None

class AtrSimples (Construcao):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def interpretar(self):
        aux = tabela.get(self.var2)
        if aux:
            adicionar(self.var1, aux)
        else:            
            adicionar(self.var1, self.calcular())

    def calcular(self):
        if ',' in self.var2:
            self.var2 = self.var2.replace(',','.')
            return float(self.var2)
        elif ',' not in self.var2:
            return self.var2    

class Atr (Construcao):
    def __init__(self, var1, var2, var3, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, self.calcular())

    def calcular(self):
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3) 

class AtrRaiz (Construcao):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def interpretar(self):
        aux = tabela.get(self.var2)
        if aux:
            adicionar(self.var1, aux)
        else:
            adicionar(self.var1, self.calcular())           

    def calcular(self):           
        for x in range(int(self.var2)):            
            if x * x == int(self.var2):
                return x          

class AtrFatorial (Construcao):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def interpretar(self):
        aux = tabela.get(self.var2)
        if aux:
            adicionar(self.var1, aux)
        else:
            adicionar(self.var1, self.calcular())           

    def calcular(self):           
        fact = 1
        for x in range(1, int(self.var2) + 1):
            fact = fact * x
        return fact   

class AtrPotencia (Construcao):
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def interpretar(self):
        aux = tabela.get(self.var2)
        if aux:
            adicionar(self.var1, aux)
        else:
            adicionar(self.var1, self.calcular())           

    def calcular(self):           
        return int(self.var2) ** int(self.var3)

class AtrRandom (Construcao):
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def interpretar(self):
        aux = tabela.get(self.var2)
        if aux:
            adicionar(self.var1, aux)
        else:
            adicionar(self.var1, self.calcular())           

    def calcular(self):           
        return random.randrange(int(self.var2),int(self.var3)) 

class AtrDigitoRaiz (Construcao):
    def __init__(self, var1, var2, var3, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, self.calcular())

    def calcular(self):          
        for x in range(int(self.var3)):            
            if x * x == int(self.var3):
                self.var3 = x
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3) 

class AtrDigitoFatorial (Construcao):
    def __init__(self, var1, var2, var3, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, self.calcular())

    def calcular(self):
        fact = 1
        for x in range(1, int(self.var3) + 1):
            fact = fact * x
        self.var3 = fact        
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)             

class AtrDigitoPotencia (Construcao):
    def __init__(self, var1, var2, var3, var4, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        adicionar(self.var1, self.calcular())

    def calcular(self):
        self.var3 = int(self.var3) ** int(self.var4)                
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)  

class AtrDigitoRandom (Construcao):
    def __init__(self, var1, var2, var3, var4, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        adicionar(self.var1, self.calcular())

    def calcular(self):
        self.var3 = random.randrange(int(self.var3),int(self.var4))                 
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)  

class AtrRaizRaiz (Construcao):
    def __init__(self, var1, var2, var3, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, self.calcular())

    def calcular(self):   
        for x in range(int(self.var2)):            
            if x * x == int(self.var2):
                self.var2 = x       
        for x in range(int(self.var3)):            
            if x * x == int(self.var3):
                self.var3 = x
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3) 

class AtrRaizFatorial (Construcao):
    def __init__(self, var1, var2, var3, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, self.calcular())

    def calcular(self):   
        for x in range(int(self.var2)):            
            if x * x == int(self.var2):
                self.var2 = x       
        fact = 1
        for x in range(1, int(self.var2) + 1):
            fact = fact * x
        self.var3 = fact
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3) 

class AtrRaizPotencia (Construcao):
    def __init__(self, var1, var2, var3, var4, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        adicionar(self.var1, self.calcular())

    def calcular(self):   
        for x in range(int(self.var2)):            
            if x * x == int(self.var2):
                self.var2 = x       
        self.var3 = int(self.var3) ** int(self.var4)
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)

class AtrRaizRandom (Construcao):
    def __init__(self, var1, var2, var3, var4, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        adicionar(self.var1, self.calcular())

    def calcular(self):   
        for x in range(int(self.var2)):            
            if x * x == int(self.var2):
                self.var2 = x       
        self.var3 = random.randrange(int(self.var3),int(self.var4))
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)

class AtrFatorialFatorial (Construcao):
    def __init__(self, var1, var2, var3, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        adicionar(self.var1, self.calcular())

    def calcular(self):
        fact = 1
        for x in range(1, int(self.var2) + 1):
            fact = fact * x
        self.var2 = fact
        fact = 1
        for x in range(1, int(self.var3) + 1):
            fact = fact * x
        self.var3 = fact           
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)

class AtrFatorialPotencia (Construcao):
    def __init__(self, var1, var2, var3, var4, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        adicionar(self.var1, self.calcular())

    def calcular(self):
        fact = 1
        for x in range(1, int(self.var2) + 1):
            fact = fact * x
        self.var2 = fact              
        self.var3 = int(self.var3) ** int(self.var4)
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)

class AtrFatorialRandom (Construcao):
    def __init__(self, var1, var2, var3, var4, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        adicionar(self.var1, self.calcular())

    def calcular(self):
        fact = 1
        for x in range(1, int(self.var2) + 1):
            fact = fact * x
        self.var2 = fact              
        self.var3 = random.randrange(int(self.var3),int(self.var4))
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)

class AtrPotenciaPotencia (Construcao):
    def __init__(self, var1, var2, var3, var4, var5, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.var5 = var5
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        aux5 = tabela.get(self.var5)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        if aux5:
            self.var5 = aux5
        adicionar(self.var1, self.calcular())

    def calcular(self):   
        self.var2 = int(self.var2) ** int(self.var3)       
        self.var3 = int(self.var4) ** int(self.var5)
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)

class AtrPotenciaRandom (Construcao):
    def __init__(self, var1, var2, var3, var4, var5, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.var5 = var5
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        aux5 = tabela.get(self.var5)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        if aux5:
            self.var5 = aux5
        adicionar(self.var1, self.calcular())

    def calcular(self):   
        self.var2 = int(self.var2) ** int(self.var3)       
        self.var3 = random.randrange(int(self.var4),int(self.var5))
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)

class AtrRandomRandom (Construcao):
    def __init__(self, var1, var2, var3, var4, var5, operador):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        self.var5 = var5
        self.operador = operador

    def interpretar(self):
        aux2 = tabela.get(self.var2)
        aux3 = tabela.get(self.var3)
        aux4 = tabela.get(self.var4)
        aux5 = tabela.get(self.var5)
        if aux2:
            self.var2 = aux2
        if aux3:
            self.var3 = aux3
        if aux4:
            self.var4 = aux4
        if aux5:
            self.var5 = aux5
        adicionar(self.var1, self.calcular())

    def calcular(self):   
        self.var2 = random.randrange(int(self.var2),int(self.var3))       
        self.var3 = random.randrange(int(self.var4),int(self.var5))
        if self.operador == '+':                       
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 + float(self.var3)                    
            if '.' in str(self.var3):
                if '.' not in str(self.var2):                    
                    return float(self.var2) + self.var3                    
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 + self.var3
            return int(self.var2) + int(self.var3)        
        elif self.operador == '-':            
            if '.' in str(self.var2):
                if '.' not in str(self.var3):                    
                    return self.var2 - float(self.var3)
            if '.' in str(self.var3):
                if '.' not in str(self.var2):
                    return float(self.var2) - self.var3
            if '.' in str(self.var2) and '.' in str(self.var3):                
                self.var2 = float(self.var2)
                self.var3 = float(self.var3)
                return self.var2 - self.var3
            return int(self.var2) - int(self.var3)


class Imprimir (Construcao):
    def __init__(self, var):
        self.var = var

    def interpretar(self):
        print(tabela.get(self.var))        