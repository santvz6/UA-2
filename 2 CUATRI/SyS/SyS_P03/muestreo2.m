% La función incluye ahora la fase

function muestreo(fs, Ts, fase)
    T0=1/fs;
    % Continuo (muchos valores -> 10 000)

    t = [0:2*T0/10000:2*T0]; % obtenemos 10 000 puntos entre dos periodos

    xa = cos(2*pi*fs*t + fase);
    subplot(2,1,1);
    plot(t, xa);
    grid;
    xlabel('Tiempo (s)','Fontsize',8);
    ylabel('Amplitud','Fontsize',8);
    title('Señal continua x_{a}(t)');
    
    % Discreto (va de Ts en Ts)
    axis([0 2*T0 -1.5 1.5]);

    nTs = [0:Ts:2*T0]; % dividimos en trozos independientemente de T0 (discreto)

    xs = cos(2*pi*fs*nTs + fase);
    n = 0:length(nTs)-1; subplot(2,1,2);
    stem(n, xs);
    grid;
    xlabel('Índice de muestreo, n. T_s=0.1 ms','Fontsize',8);
    ylabel('Amplitud','Fontsize',8);
    title('Señal discreta x[n]'); axis([0 2*T0/Ts -1.5 1.5])
end