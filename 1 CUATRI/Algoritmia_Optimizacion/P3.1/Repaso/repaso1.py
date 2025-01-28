class Mochila:
    def __init__(self, w, v, W, n) -> None:
        
        self.w = w
        self.v = v
        self.W = W
        self.n = n

        self.best_v = -1
        self.best_x = None

    def voraz(self):

        ordenado = sorted(range(self.n), key= lambda x: self.v[x] / self.w[x], reverse= True)
        v_acc = 0
        w_acc = 0
        x = [0] * self.n
        
        for i in ordenado:
            if w_acc + self.w[i] <= self.W:
                v_acc += self.v[i]
                w_acc += self.w[i]
                x[i] = 1

        return v_acc, x
    
    def cotaOptimista(self, indice, v_acc, w_acc):

        ordenado = sorted(range(indice, self.n), key= lambda x: self.v[x] / self.w[x], reverse= True)
        W_restante = self.W - w_acc

        for i in ordenado:
            if self.w[i] <= W_restante:
                W_restante -= self.w[i]
                v_acc += self.v[i]
            else:
                v_acc += self.v[i] * (W_restante / self.w[i])
                break
            
        return v_acc
    
    def vueltaAtras(self, indice, x, v_acc, w_acc):
        
        hayEspacio = w_acc <= self.W
        mejorCamino = self.cotaOptimista(indice, v_acc, w_acc) > self.best_v
        

        if hayEspacio and mejorCamino:
            
            nodoHoja = (indice == self.n)

            if nodoHoja:
                if v_acc > self.best_v:
                    self.best_v = v_acc
                    self.best_x = x.copy()

            else:
                for agarrar in [0, 1]:
                    x[indice] = agarrar
                    self.vueltaAtras(indice+1, x, v_acc+self.v[indice]*x[indice], w_acc+self.w[indice]*x[indice])

    
    def resolver(self):
        self.best_v, self.best_x = self.voraz()
        print("Sol. voraz: {}".format(self.best_v))
        self.vueltaAtras(indice= 0, x= [-1]*self.n, v_acc=0, w_acc=0)


import random
if __name__ == "__main__":
    random.seed(67)
    N = 50 # Num Objetos
    v = [random.randint(1,50) for _ in range(N)]
    w = [random.randint(1,50) for _ in range(N)]
    W = random.randint(N*1, N*10)

    mochila = Mochila(v,w,W,N)
    mochila.resolver()
    print("v={}".format(v))
    print("w={}".format(w))
    print("W={}".format(W))
    print("Solucion: {}".format(mochila.best_x))
    print("Valor: {}".format(mochila.best_v))
