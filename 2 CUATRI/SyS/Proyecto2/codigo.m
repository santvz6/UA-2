% =========================================================================
% PROYECTO 2 - SISTEMA DE TRANSCRIPCIÓN AUTOMÁTICA DE VOZ A TEXTO
% Señales y Sistemas - Grado en Ingeniería en Inteligencia Artificial
% =========================================================================

clc;
clear;
close all;

%% ==================== CONFIGURACIÓN INICIAL ====================

disp('Inicio del sistema de reconocimiento de voz...');
audioFile = 'AudiosProyecto02/ai.wav'; 

%% ==================== CARGAR Y REPRODUCIR AUDIO ====================

try
    [audioIn, fs] = audioread(audioFile);
    disp(['Archivo de audio cargado: ' audioFile]);
catch
    error('No se ha podido leer el archivo de audio. Revisa la ruta y el nombre.');
end

sound(audioIn, fs);
disp('Reproduciendo el audio...');
pause(length(audioIn) / fs + 1);

%% ==================== TRANSCRIPCIÓN CON SPEECH2TEXT ====================

try
    transcript = speech2text(audioIn, fs, Language="en");
    disp('Transcripción realizada con éxito.');
catch ME
    disp('Error durante la transcripción:');
    disp(ME.message);
    return;
end

%% ==================== MOSTRAR RESULTADOS ====================

disp('==============================================');
disp('RESULTADO DE LA TRANSCRIPCIÓN:');
disp('----------------------------------------------');
disp(transcript);
disp('==============================================');

disp('Fin del sistema. Proyecto completado.');
