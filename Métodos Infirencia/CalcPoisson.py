import scipy.stats as stats

# Parámetro de la distribución de Poisson
lambda_poisson = 0.6

# Percentil 17
percentil_17 = stats.poisson.ppf(0.17, lambda_poisson)
print(percentil_17)