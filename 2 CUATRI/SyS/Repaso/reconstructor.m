% --- FUNCIÓN RECONSTRUCTOR IDEAL ---
% Esta función recontruye una señal analógica a partir de una señal previamente digitalizada.
% Utiliza sinc y necesita conocer todas las muestras de antemano.
% Ejemplo de uso: reconstructor(4,0.1)
% Teorema Nyquist: fs>2*f0; 1/Ts>2*f0
% Muestreo incorrecto (f0=4,Ts=0.4)
% Muestreo correcto (f0=4,Ts=0.1) 

function reconstructor (f0, Ts);
    f0 = 4;
    Ts = 1/10;
    ta = [0:0.01:1];
    xa = cos(2*pi*f0*ta);
    nTs = (0:Ts:1).';
    xd = cos(2*pi*f0*nTs);
    xr = zeros(size(ta));
    for m=1:length(nTs)
        xr = xr + xd(m).*sinc((ta-nTs(m))/Ts);
    end
    plot(ta,xa,'.-g',nTs,xd,'or',ta,xr,'b');
    grid;
    legend('Original','Muestras','Reconstruida');
    xlabel('Tiempo (s)');
    ylabel('Amplitud');
    axis([0 1 -1.9 1.9]);
end