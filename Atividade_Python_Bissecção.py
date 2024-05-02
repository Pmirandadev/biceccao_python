import math
import random
#equação a ser calculada: - * 3 ^ x 2 17
#3*x^2-17
#primeira coisa = colocar a equação polonesa para funfar
class Expressao:
    __switch_op = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: math.pow(a, b)
        }
    
    def __init__(self, exp=None):
        self.s = []  # Stack / Pilha
        self.t = -1  # Top   / Topo

        if exp is None:
            return

        for entry in exp.split(' '):
            if entry.isdigit(): # NESSE CASO TIVE QUE SUBSTITUIR POR ISDIGIT POR QUE 17 DO CODIGO TEM 2 CASAS E DÁ ERRO
            # if any([entry in ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']]):
                self.stack(float(entry))
            else:
                self.stack(entry)

    def stack(self, value):
        self.t = self.t + 1
        self.s.insert(0, value)

    def pop(self):
        self.t = self.t - 1
        return self.s[self.t + 1]

    def eval(self, x, reset=False):
        if reset:
            self.t = len(self.s) - 1
        
        entry = self.pop()

        if type(entry) == float:
            return entry
        elif 'x' in entry:
            return x
        else:
            return self.__switch_op[entry](self.eval(x), self.eval(x))

    def bisseccao (self, p_a, p_b):
        erro = 0.00001
        if (e.eval(p_a, True)) > 0 and (e.eval(p_b, True)) < 0:
                print("O valor de x para um numero Positivo é: ", round(p_a,5))
                positivo = (round(e.eval(p_a, True),5))
                print("Resultado =",positivo)
                print("O valor de x para um numero Negativo é: ", round(p_b,5))
                negativo = (round(e.eval(p_b, True),5))
                print("Resultado =",negativo)
        else:
                print("não foi possivel colocar numeros negativos e numeros positivos")
        
        f_a = positivo
        f_b = negativo
        if f_a * f_b > 0:
            ("Entre esses pontos não tem raiz")
        else:            
            while abs(p_a - p_b) > erro:
                media_entre_pontos = (p_a + p_b) / 2
                media_y = e.eval(media_entre_pontos, True)
                if f_a * media_y > 0:
                    p_a = media_entre_pontos
                elif f_b * media_y > 0 :
                    p_b = media_entre_pontos
        raiz = (p_a + p_b) / 2
        return raiz

if __name__ == "__main__":
    e = Expressao("- * 3 ^ x 2 17")
    p_a = random.uniform(2.4 , 3)
    p_b = random.uniform(1.5 , 2.3) 
    print("A raiz se encontra no ponto:", round(e.bisseccao(p_a, p_b), 5))    