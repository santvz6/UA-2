a = [1 -1/5 -1/25]; % Como mínimo debe valer 1 el primer coeficiente
b = [1 1/3];

% Vector de 101 posiciones con 1 en la 1ª
d  = zeros(size(n));
d(1) = 1;
h = filter(b, a, d);

% Implementación del sistema FIR
bb = [1 zeros(1,9) 0.8 zeros(1,9) 0.64];
aa=[1];

%...