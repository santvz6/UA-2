import random

class Mochila:
    def __init__(self, v, w, W, N):
        self.v = v
        self.w = w
        self.W = W
        self.N = N
        
        self.count = 0
        self.best_x = None
        self.best_v = -1

    def peso(self, x):
        p = 0
        for i in range(N):
            p += x[i] * self.w[i]
        return p 

    def valor(self, x):
        value = 0
        for i in range(N):
            value += x[i] * self.v[i]
        return value 

    def cota_optimista(self, x, i, w_acc, v_acc):
        #return float("inf")
        restante = self.W - w_acc
        indices = sorted(range(i,self.N), key=lambda x : self.v[x] / self.w[x], reverse=True)    
        for j in indices:  
            if self.w[j] <= restante:
                v_acc += self.v[j]
                restante -= self.w[j]
            else:
                v_acc += self.v[j] * (restante / self.w[j])
                break

        return v_acc

    def v_atras(self, x, i, w_acc, v_acc):
        self.count += 1
        if w_acc <= self.W and self.cota_optimista(x,i, w_acc, v_acc) > self.best_v: # Factible y prometedor
            if i == self.N:
                # Nodo hoja
                if v_acc > self.best_v: # Mejor
                    self.best_v = v_acc
                    self.best_x = x.copy()    
            else:
                # Nodo intermedio
                for o in [0, 1]:
                    x[i] = o
                    self.v_atras(x, i+1, w_acc + x[i]*w[i], v_acc + x[i]*v[i])

    def voraz(self):
        indices = sorted(range(self.N), key=lambda x : self.v[x] / self.w[x], reverse=True)    
        x = [0] * self.N
        v_acc = 0
        w_acc = 0
        for i in indices:
            if self.w[i]+w_acc <= self.W:
                x[i] = 1
                v_acc += self.v[i]
                w_acc += self.w[i]

        return x, v_acc

        

    def resolver(self):
        x = [-1]*N
        i = 0
        self.best_x, self.best_v = self.voraz()
        print("Sol. voraz: {}".format(self.best_v))
        self.v_atras(x=x,i=i,w_acc=0,v_acc=0)


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
    print("Llamadas: {}".format(mochila.count))

