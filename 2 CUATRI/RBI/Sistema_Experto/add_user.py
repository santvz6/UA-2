def addUser(user: dict):

    # 15

    data = {
        "Edad": 0 or 120
        "Sexo": ["M" or "F"]
        "RazaEtnia": ["African", "European", "American", "Asian", "Oceanic"],
        "DolorToracico": [True or False]
        "Disnea": [True, True, False, True],
        "Fatiga": [True, True, True, False],
        "DolorBrazo": [True, False, False, False],
        "Sudoracion": [True, False, False, True],
        "Nauseas": [True, False, False, False],
        "Palpitaciones": [False, False, True, True],
        "HipertensionArterial": [False, True, False, True], 
        "Dislipidemia": [True, True, False, True],  
        "Diabetes": 0.8
        "Obesidad": [False, True, False, True],  
        "Tabaquismo": [True, False, False, True],  #
        "NivelEducativo": ["Universidad", "Secundaria", "Universidad", "Primaria"],  
        "IngresosEconomicos": ["Alto", "Medio", "Alto", "Bajo"],  
        "Ocupacion": ["Empleado", "Jubilado", "Empleado", "Desempleado"] 
    }


    template = ["age", "..."]

    for key, value in user.items():
        if key in template:
            # Logica
        