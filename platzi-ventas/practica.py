

if __name__ == "__main__":
    nombre = input('Ingrese su nombre: ')
    edad = input('Ingrese su edad: ')
    sexo = input('Ingrese su sexo: ')
    print("Ingreses las notas para darle su promedio: ")
    nota1 = input('Nota 1: ')
    nota2 = input('Nota 2: ')
    nota3 = input('Nota 3: ')
    nota4 = input('Nota 4: ')

    suma = nota1 + nota2 + nota3 + nota4
    print(type(suma))
    promedio = int(suma) / 4
        
    print('Su nombre es ' + nombre + ' tiene la edad de ' + edad + ' y es de sexo ' + sexo)
    print('Su promedio es de :' , promedio)