import numpy as np
from markovchain import MarkovChain

def ejercicio_1():
    labels = ["BB", "RB", "NB"]
    M = np.array([
        [0.5, 0.5, 0],
        [0.5, 0, 0.5],
        [0, 0.5, 0.5]
    ])
    mc = MarkovChain(M, labels, percentages=True)
    mc.draw()

def ejercicio_2():
    labels = ["Bajo", "1er Piso", "2do Piso"]
    M = np.array([
        [0, 0.5, 0.5],
        [0.75, 0.25, 0],
        [1, 0, 0]
    ])
    mc = MarkovChain(M, labels, percentages=True)
    mc.draw()

def ejercicio_3():
    labels = ["Hathway", "ADN", "Excitel"]
    M = np.array([
        [0.8, 0.1, 0.1],
        [0.2, 0.6, 0.2],
        [0.1, 0.2, 0.7]
    ])
    mc = MarkovChain(M, labels, percentages=True)
    mc.draw()

def ejercicio_4():
    labels = ["McAfee", "Quickheal", "Kaspersky", "Avira"]
    M = np.array([
        [0.94, 0, 0, 0.02],
        [0, 0.90, 0, 0.06],
        [0, 0, 0.92, 0.05],
        [0, 0, 0, 0.97]
    ])
    mc = MarkovChain(M, labels, percentages=True)
    mc.draw()

def ejercicio_5():
    labels = ["Excelente", "Muy Bueno", "Bueno", "Aceptable", "Riesgoso", "Malo", "Crítico", "Quiebra"]
    P = np.array([[0.9193, 0.0746, 0.0048, 0.0008, 0.0004, 0.0000, 0.0000, 0.0000],
              [0.6400, 0.9181, 0.0676, 0.0060, 0.0006, 0.0012, 0.0003, 0.0000], 
              [0.0700, 0.0227, 0.9169, 0.0512, 0.0056, 0.0025, 0.0001, 0.0004], 
              [0.0400, 0.0270, 0.0556, 0.8788, 0.0483, 0.0102, 0.0017, 0.0024], 
              [0.0400, 0.0010, 0.0061, 0.0775, 0.8148, 0.0790, 0.0111, 0.0101], 
              [0.0000, 0.0010, 0.0028, 0.0046, 0.0695, 0.8280, 0.0396, 0.0545], 
              [0.1900, 0.0000, 0.0037, 0.0075, 0.0243, 0.1213, 0.6045, 0.2369], 
              [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000]])
    mc = MarkovChain(P, labels, percentages=True)
    mc.draw()

def ejercicio_6():
    # Matriz de transición
    P = np.array([[0.9, 0.1, 0.0],
                  [0.85, 0.05, 0.1],
                  [0.5, 0.1, 0.4]])
    
    # Estado inicial (distribución del 1 de septiembre)
    x0 = np.array([1/4, 1/3, 5/12])
    
    # Cálculo de la distribución en noviembre (después de 2 meses)
    x_nov = x0 @ np.linalg.matrix_power(P, 2)
    
    # Cálculo del vector de estado estable (solución de xP = x)
    eigvals, eigvecs = np.linalg.eig(P.T)
    stationary = eigvecs[:, np.isclose(eigvals, 1)]
    stationary = stationary / stationary.sum()
    
    print("Distribución en noviembre:", x_nov)
    print("Vector de estado estable:", stationary.real.flatten())
    
    # Dibujar la cadena de Markov
    labels = ["S1", "S2", "S3"]
    mc = MarkovChain(P, labels)
    mc.draw()

def ejercicio_7():
    # Matriz de transición de la cola
    P = np.array([[2/3, 1/3, 0, 0, 0],
                  [3/8, 2/3, 1/3, 0, 0],
                  [0, 3/8, 2/3, 1/3, 0],
                  [0, 0, 3/8, 2/3, 1/3],
                  [0, 0, 0, 3/8, 5/8]])
    
    # Cálculo del vector de estado estable
    eigvals, eigvecs = np.linalg.eig(P.T)
    stationary = eigvecs[:, np.isclose(eigvals, 1)]
    stationary = stationary / stationary.sum()
    
    print("Vector de estado estable:", stationary.real.flatten())
    
    # Dibujar la cadena de Markov
    labels = ["0", "1", "2", "3", "4"]
    mc = MarkovChain(P, labels)
    mc.draw()


ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()
ejercicio_7()