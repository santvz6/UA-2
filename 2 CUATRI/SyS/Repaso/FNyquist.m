fs1 = 15; % Frecuencia de muestreo baja (menor a 2*f)
fs2 = 40; % Frecuencia de muestreo alta (suficiente según Nyquist)
f = 15;   % Frecuencia de la señal original

t1 = 0:1/fs1:1; 
t2 = 0:1/fs2:1; 
tc = 0:0.001:1; % Tiempo continuo

x_cont = sin(2*pi*f*tc); % Señal continua
x1 = sin(2*pi*f*t1); % Señal muestreada con fs1
x2 = sin(2*pi*f*t2); % Señal muestreada con fs2

figure;
subplot(2,1,1);
plot(tc, x_cont, 'g'); hold on;
stem(t1, x1, 'r', 'filled'); % Muestreo con aliasing
title('Muestreo con frecuencia baja (Aliasing)');
xlabel('Tiempo (s)'); ylabel('Amplitud');

subplot(2,1,2);
plot(tc, x_cont, 'g'); hold on;
stem(t2, x2, 'b', 'filled'); % Muestreo correcto
title('Muestreo con frecuencia adecuada');
xlabel('Tiempo (s)'); ylabel('Amplitud');
