import matplotlib.pyplot as plt
import numpy as np
import sys
from sympy import *


def handler(arifmEx):
    arifmEx = arifmEx.replace(' ', '')
    if '^' in arifmEx:
        arifmEx = arifmEx.replace('^', '**')
    if len(arifmEx[:arifmEx.find('x**')]) == 0:
        arifmEx = "1*" + arifmEx
    return arifmEx


def check(arifmEx):
    varsFunc = ['sin', 'cos', 'sqrt']
    return any([i in arifmEx for i in varsFunc])


function = sys.argv
function[1] = handler(function[1])
if not check(function[1]):
    n = []

    if '/' in function[1]:
        arifmEx = function[1].split('/')
        x = symbols('x', real=True)
        n = solve(Eq(eval(arifmEx[0]), 0), x) + solve(Eq(eval(arifmEx[1]), 0), x)

    if '/' not in function[1]:
        x = symbols('x', real=True)
        n = solve(Eq(eval(function[1]), 0), x)

        if len(n) == 0 and 'x**2' in function[1] and 'x' in function[1][function[1].find('x**') + 1:]:
            terms = list(map(lambda x: x.replace('**2', '').replace('*', ''), function[1].split('x')))
            a = float(terms[0])
            b = float(terms[1])
            c = float(terms[-1]) if len(terms) > 2 else 0
            discr = b ** 2 - 4 * a * c
            n.append(-b / (2 * a))

    # print(n)

    if len(n) == 0:
        n = [0]

    elif len(n) > 0 and \
            any(([str(type(i)) in ["<class 'sympy.core.numbers.NegativeOne'>", "<class 'sympy.core.add.Add'>"]
                  for i in n])):
        n = [0]

    fig, ax = plt.subplots()
    ax.set_title('Graph function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.grid(True)

    X_min = float(min(n) - 4.0)
    X_max = float(max(n) + 4.0)

    x = np.linspace(X_min, X_max, 100)
    y = eval(function[1])
    ax.plot(x, y)

    plt.show()

else:
    if 'cos' in function[1] or 'sin' in function[1]:
        function[1] = '1*' + function[1]

        fig, ax = plt.subplots()
        ax.set_title('График функции')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.grid(True)

        x = np.linspace(0, 4 * np.pi, 100)
        y = eval(function[1][:function[1].find('sin') - 1]) * \
            np.sin(eval(function[1][function[1].find('sin') + 4:function[1].find(')')])) if 'sin' in function[1] \
            else eval(function[1][:function[1].find('cos') - 1]) * \
                 np.cos(eval(function[1][function[1].find('cos') + 4:function[1].find(')')]))
        ax.plot(x, y)

        plt.show()
    else:
        functioSqrt = function[1][function[1].index('sqrt') + 5:function[1].find(')')]

        fig, ax = plt.subplots()
        ax.set_title('График функции')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.grid(True)

        x = np.linspace(0, 9, 100)
        y = eval(functioSqrt) ** 0.5
        ax.plot(x, y)

        plt.show()
