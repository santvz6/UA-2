% Represetnación continua
n = [0:1:19];
x = cos(0.125*pi*n); % cos(2pi*f * n)
plot(n, x)

% Representación discreta
hold on; % Poner una función sobre otra
stem(n, x, 'r');
close all;

%----------------------------------------------------------------------------------------------
% 1.1 Estudio del muestreo en el dominio del tiempo
muestreo(40, 0.0001);
close;
muestreo(600, 0.001)
close;
muestreo(40, 1/(2*40))   % lo necesario para poder reconstruirla fs > 2fmax
                                        % por tanto Ts = 1 / fs * 2 = Tmax
close;

muestreo(40, 0.001)
figure;
muestreo2(40, 0.001, pi/2);
close all;

ejercicio1(40,  1, 0.001, 0);