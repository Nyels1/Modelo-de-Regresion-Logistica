from django.shortcuts import render
import joblib
import numpy as np
import os

modelo_path = os.path.join(os.path.dirname(__file__), 'models/modelo_salario.pkl')
modelo = joblib.load(modelo_path)

def index(request):
    return render(request, 'index.html')    

def predecir(request):
    prediccion = None
    if request.method == 'POST':
        try:
            horas = float(request.POST.get('horas'))
            entrada = np.array([[horas]])
            resultado = modelo.predict(entrada)[0]
            prediccion = round(resultado, 2)
        except Exception as e:
            prediccion = f"Error en la predicción: {e}"

    return render(request, 'index.html', {'prediccion': prediccion})