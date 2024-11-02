# git_calculadora_mrm

## Descripción:
Este trabajo es sobre hacer una calculadora básica en la que se pueda mostrar distintos conflictos y cómo se lleva a arreglarlos.

## Funciones
- `suma(a, b)`: Suma dos números.
- `resta(a, b)`: Resta dos números.
- `multiplicacion(a, b)`: Multiplica dos números.
- `division(a, b)`: Divide dos números (maneja división por cero).
- `potencia(a, b)`: Calcula la potencia de un número.
- `raiz_cuadrada(a)`: Calcula la raíz cuadrada.
- `logaritmo(a)`: Calcula el logaritmo natural.

## Uso de Git
### Crear una nueva rama para una característica
```bash
git checkout -b feature/nombre_de_la_funcion

#Se hacen cambios en las ramas

git add calculadora.py
git commit -m "nombre de la actualizacion de los cambios"
git push --set-upstream origin feature/nombre_de_la_funcion

#Se cambia a la rama develop para la fusion

git checkout develop
git merge feature/nombre_de_la_función
git push origin develop


