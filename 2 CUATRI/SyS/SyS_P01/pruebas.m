x = [0:0.1:100];
y = cos(x);
plot(x, y);
title('Cos(x)');
title('Gráfica Cos(x)');
xlabel('Tiempo (s)');  % texto eje X
ylabel('Amplitud(m)');% texto eje Y
text(50, 0.5, 'Hola');  % aplicar exto en un sitio concreto
gtext('NEGRO');       % aplicar texto donde seleccionas
legend('cos(x)');       % aplicar leyenda
grid on;                    % rejilla
close all;

% PLOTEAR DOS FUNCIONES
x = [0:pi/25:6*pi];
y = sin(x);
y2 = cos(x);
plot(x, y);
plot(x, y2);
plot(x, y, x, y2); % FORMA 1

% PLOTEAR DOS FUNCIONES DE OTRA FORMA
z = eig(rand(20, 20));
plot(real(z), imag(z), '+');
plot(z, 'o');
z2 = eig(rand(20,20));
plot(z, z2);
Z = [z z2]; % FORMA 2
plot(Z);
close;

%
plot(x, y, 'LineStyle', '-.', 'LineWidth', 3, 'Color', 'k', 'Marker', '*', 'MarkerSize', 5);
close;

%
f1 = figure();
a1 = subplot(2, 2, 1);
plot(x, y, 'LineStyle','--', 'LineWidth', 2, 'Marker', '*', 'Color', 'g');
xlabel('Tiempo (s)');
a2 = subplot(2, 2, 2);
plot(x, y2, 'LineStyle','--', 'LineWidth', 1, 'Marker', 'o', 'Color', 'r');
0k8kt-