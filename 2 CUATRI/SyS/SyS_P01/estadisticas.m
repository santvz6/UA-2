% Diseña una función para calcular medias estadísticas. 
% Si la variable de entrada es un vector, calcula la media y la desviación típica de todos sus elementos
% Mientras que si la variable de entrada es una matriz,
% obtén un vector fila con los valores medios y las desviaciones típicas de cada columna.

function [media, desviacion] = P1_estadisticas(A)
    [i, j] = size(A);

    % A es una matriz
    if i ~= 1
        media = zeros(1, j);       
        desviacion = zeros(1, j);
        
        for indx = 1 : j
            media(indx) = mean(A(:, indx));       % Media por columna
            desviacion(indx) = std(A(:, indx));   % Desviación estándar por columna
        end
    else
        % A es un vector
        media = mean(A);
        desviacion = std(A);
    end
end

    