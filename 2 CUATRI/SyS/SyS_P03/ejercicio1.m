function ejercicio1(f01, k, Ts, fase)
    
    fs = 1 / Ts;
    T0 = 1 / f01; 

    % Frecuencia de la segunda señal cumpliendo la relación dada
    f02 = f01 + k * fs;
    
    % Definimos el tiempo continuo con 10 000 valores
    t = 0:2*T0/10000:2*T0;
    
    % Generamos las señales continuas
    xa1 = cos(2*pi*f01*t + fase);
    xa2 = cos(2*pi*f02*t + fase);
    
    % Muestreo de las señales
    nTs = 0:Ts:2*T0;  % Instantes de muestreo
    xs1 = cos(2*pi*f01*nTs + fase);
    xs2 = cos(2*pi*f02*nTs + fase);
    n = 0:length(nTs)-1;  % Índices de muestreo
    
    % Gráfica para las señales continuas
    subplot(2,2,1);
    plot(t, xa1); 
    grid;
    xlabel('Tiempo (s)');
    ylabel('Amplitud');
    title('Señal continuax_{a1}(t)');
    axis([0 2*T0 -1.5 1.5]);


    subplot(2,2,2);
    plot(t, xa2);
    grid;
    xlabel('Tiempo (s)');
    ylabel('Amplitud');
    title('Señal continua x_{a2}(t)');
    axis([0 2*T0 -1.5 1.5]);
    
    % Gráfica para las señales muestreadas
    subplot(2,2,3);
    stem(n, xs1); 
    grid;
    xlabel('Índice de muestreo, n');
    ylabel('Amplitud');
    title('Señal discreta x_{1}[n]');
    axis([0 2*T0/Ts -1.5 1.5]);

    subplot(2,2,4);
    stem(n, xs2);
    grid;
    xlabel('Índice de muestreo, n');
    ylabel('Amplitud');
    title('Señal discreta x_{1}[n]');
    axis([0 2*Ts-1.5 1.5]);
    
end
