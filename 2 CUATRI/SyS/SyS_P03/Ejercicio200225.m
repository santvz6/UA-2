function [Xq, SNq] = cuantificacion(X, Xmax, Xmin, b)
    % CUANTIFICACION: Cuantificación uniforme de una señal
    % Entrada:
    %   X    : señal a cuantificar
    %   Xmax : valor máximo del margen dinámico
    %   Xmin : valor mínimo del margen dinámico
    %   b    : número de bits del cuantificador
    % Salida:
    %   Xq   : señal cuantificada
    %   SNq  : relación señal a ruido de cuantificación (dB)

    % Cálculo del paso de cuantificación
    L = 2^b;                     % Número de niveles
    delta = (Xmax-Xmin) / L;   % Tamaño del paso

    % Cuantificación uniforme
    Xq = zeros(size(X));  % Inicializa el vector de salida

    for i = 1:length(X)
        if abs(X(i)) < Xmax
            % Caso 1: |x| < Xmax
            Xq(i) = delta * (fix(abs(X(i)) / delta) + 0.5) * sign(X(i));
        else
            % Caso 2: |x| >= Xmax (saturación)
            Xq(i) = sign(X(i)) * (Xmax - delta / 2);
        end
    end


    % Cálculo del error de cuantificación
    eq = Xq - X;

    % Cálculo de la potencia de la señal y del error
    Px = mean(X.^2);
    Pq = mean(eq.^2);

    % Relación señal a ruido de cuantificación (dB)
    SNq = 10 * log10(Px / Pq);

    % Representación gráfica
    figure;
    subplot(3,1,1);
    plot(X, 'b');
    title('Señal Original'); grid on;
    ylabel('Amplitud');

    subplot(3,1,2);
    plot(Xq, 'r');
    title(['Señal Cuantificada (', num2str(b), ' bits)']); grid on;
    ylabel('Amplitud');

    subplot(3,1,3);
    plot(eq, 'k');
    title('Error de Cuantificación'); grid on;
    xlabel('Muestras'); ylabel('Error');

    % Mostrar SNR
    disp(['Relación Señal a Ruido (SNR): ', num2str(SNq), ' dB']);
end

% Ejemplo de uso:
f0 = 1/50; N = 200;
n = 0:N-1;
X = sin(2 * pi * f0 * n);
[Xq, SNq] = cuantificacion(X, 1, -1, 2);
