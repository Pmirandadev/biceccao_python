# Atividade feita em python para Bicecção

* O metodo consiste em buscar raízes em um intervalo de 2 pontos.

O projeto é simples e direto, basicamente você dita no __main__ a função desejada e os pontos selecionados:
```
if __name__ == "__main__":
    e = Expressao("- * 3 ^ x 2 17") # Expressão desejada
    p_a = random.uniform(2.4 , 3) # Ponto 1 selecionado
    p_b = random.uniform(1.5 , 2.3) # Ponto 2 selecionado
    print("A raiz se encontra no ponto:", round(e.bisseccao(p_a, p_b), 5))
```
Além de printar a raiz no ponto expecifico dessa expressão, ela retorna também os numeros gerados aleatoriamente para ter um numero</br>
positivo e negativo para que haja resultado.
