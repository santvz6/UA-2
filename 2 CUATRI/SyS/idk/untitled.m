n = 0 : 1 : 100;
pulso = zeros(size(n));
pulso(11 : 11 + 50 - 1)=1;

a = [1 -1/5 -1/25]; % Como mínimo debe valer 1 el primer coeficiente
b = [1 1/3];

x = 3*cos(0.05*pi*n).* pulso;
stem(n, x);

y = filter(b, a, x);
figure;
stem(n, y);
