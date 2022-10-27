import deli as d
import minus as m
import plus as p
import umnozh as u

A = int(input('Введите первое число: '))
B = int(input('Введите второе число число: '))
C = input("Введите действие: ")

def contr():
    if C == '+':
        return p.plus(A, B)
    elif C == '-':
        return m.minus(A, B)
    elif C == '*':
        return u.umnozh(A, B)
    elif C == '/':
        return d.deli(A, B)
    else:
        print('Введите корректный знак действия!!') 
