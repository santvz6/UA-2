a = [1 -1/5 -1/25]; % Como mínimo debe valer 1 el primer coeficiente
b = [1 1/3];

% Vector de 101 posiciones con 1 en la 1ª
d  = zeros(size(n));
d(1) = 1;
h = filter(b, a, d);

% Implementación del sistema FIR
hFIR = zeros(size(n));
hFIR(1) = 1;
hFIR(10+1) = 0.8;
hFIR(20+1) = 0.64;

heq=conv(h, hFIR); % Ejecución con comando CONV

figure
stem(n, heq(1:101)), xlabel('n'), ylabel('ht[n]')
title('h total equivalente mediante convolución')