* Atividade feita em python para Bicecção

** O metodo consiste em buscar raízes em um intervalo

O projeto é simples e direto, basicamente você dita no __main__ a função desejada e os pontos selecionados:
```
if __name__ == "__main__":
    e = Expressao("- * 3 ^ x 2 17")
    p_a = random.uniform(2.4 , 3)
    p_b = random.uniform(1.5 , 2.3) 
    print("A raiz se encontra no ponto:", round(e.bisseccao(p_a, p_b), 5))
```
