# Definimos las probabilidades y realizamos los cálculos

# Total de bolas en la urna 1
total_bolas_urna1 = 18
bolas_blancas_urna1 = 10
bolas_negras_urna1 = 8

# Cálculo de P(A): probabilidad de sacar dos bolas blancas de la urna 1
P_A = (bolas_blancas_urna1 / total_bolas_urna1) * ((bolas_blancas_urna1 - 1) / (total_bolas_urna1 - 1))

# Cálculo de probabilidad de una blanca y una negra (en cualquier orden)
P_una_blanca_una_negra = ((bolas_blancas_urna1 / total_bolas_urna1) * (bolas_negras_urna1 / (total_bolas_urna1 - 1)) +
                          (bolas_negras_urna1 / total_bolas_urna1) * (bolas_blancas_urna1 / (total_bolas_urna1 - 1)))

# Cálculo de probabilidad de dos bolas negras
P_dos_negras = (bolas_negras_urna1 / total_bolas_urna1) * ((bolas_negras_urna1 - 1) / (total_bolas_urna1 - 1))

# Probabilidades condicionales P(B|A), P(B|una blanca y una negra), P(B|dos negras)
P_B_dado_A = 4 / 21  # Si trasladamos dos blancas
P_B_dado_blanca_negra = 3 / 21  # Si trasladamos una blanca y una negra
P_B_dado_dos_negras = 2 / 21  # Si trasladamos dos negras

# Cálculo de P(B) usando la ley de probabilidad total
P_B = (P_A * P_B_dado_A +
       P_una_blanca_una_negra * P_B_dado_blanca_negra +
       P_dos_negras * P_B_dado_dos_negras)

# Finalmente, calculamos P(A|B) usando el teorema de Bayes
P_A_dado_B = (P_B_dado_A * P_A) / P_B

P_A, P_una_blanca_una_negra, P_dos_negras, P_B, P_A_dado_B
