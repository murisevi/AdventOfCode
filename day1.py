
def solution(archive) :
    listaG = []
    codigos = []
    with open(archive) as arch:
        for line in arch:
            lista = []
            numero = 0
            for char in line:
                if char.isdigit():
                    lista.append(char)
            listaG.append(lista)
            first_digit = (lista[0])
            second_digit = (lista[-1])
            numero = int(first_digit+second_digit)
            codigos.append(numero)
    
    return sum(codigos)

    
if __name__ == '__main__':

    print(solution("day1input.txt"))    
                
            
            
            
            
            
            
    