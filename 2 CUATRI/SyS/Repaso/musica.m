% --- FUNCIÓN MÚSICA ---
% Calcula muestras de cada sinusoide "musical" 
% y las concatena en la variable total
% Ejemplo de uso: musica(550, 11025)
% Después hay que reproducirlo con: sound(ans,11025,16) 

function [total]=musica(f0, fs)
    f01=f0;
    f02=(9/8)*f01;
    f03=(10/9)*f02;
    f04=(16/15)*f03;
    f05=(9/8)*f04;
    f06=(10/9)*f05;
    f07=(9/8)*f06;
    f08=(16/15)*f07;
    Ts=1/fs;
    n=0:4095;
    do1=sin(2*pi*f01*Ts*n);
    re=sin(2*pi*f02*Ts*n);
    mi=sin(2*pi*f03*Ts*n);
    fa=sin(2*pi*f04*Ts*n);
    sol=sin(2*pi*f05*Ts*n);
    la=sin(2*pi*f06*Ts*n);
    si=sin(2*pi*f07*Ts*n);
    do2=sin(2*pi*f08*Ts*n);
    total=([do1,re,mi,fa,sol,la,si,do2])
    sound(total, 11025, 250);
end

musica(10, 800);
    