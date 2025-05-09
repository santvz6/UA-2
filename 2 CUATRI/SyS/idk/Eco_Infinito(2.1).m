% ECOINF: Implementación de un eco infinito

% x vector de muestras originales
% FS frecuencia de muestreo en Hz
% ALFA factor de ganancia (será menor que 1)
% T0 retardo en segundosç

% [x, fs] = audioread('voz.wav');
% s=ecoinfinito(x, fs, 0.5,1);
% sound(s, 11025,8)

function y=ecoinfinito(x,fs,alfa,t0, infinito)

n0 = fix(t0*fs); % asigna a n0 la parte entera del retardo por la frecuencia
x = x(:).'; % asegura que vector x sea fila
x = [x, zeros(1,4*n0)]; % se alarga x para 4 ecos

if (infinito)
    a = [1 zeros(1, n0-1) -alfa];
    b = [1];
else 
    a = [1];
    [1 zeros(1, n0-1) alfa zeros(1, n0-1) alfa^2];
end

y = filter(b,a,x);