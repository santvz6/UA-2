x=[0 0 1 zeros(1,5)];
X=fft(x);
N=length(X);
w=[0:2*pi/N:2*pi/N*(N-1)];
subplot(2,1,1);
%%
% 
%  PREFORMATTED
%  TEXT
% 
plot(w, abs(X),'o-');
title('Espectro de amplitud');
xlabel('\omega');
subplot(2,1,2);
plot(w, unwrap(angle(X)),'o-');
title('Espectro de fase');
xlabel('\omega')