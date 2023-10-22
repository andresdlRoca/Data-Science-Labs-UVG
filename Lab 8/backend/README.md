# Laboratorio 8 - Backend


## Dependencias
- Python 3.10.^
- keras
- pandas
- numpy
- joblib
- flask


## Ejecución
En terminal: 
```
python backend.py
```
o
```
flask --app backend.py run
```


## Endpoints
- **/modelo** - GET: Retorna la prediccion del modelo

## Argumentos:
- city
- rooms
- bathrooms
- parking_spaces
- fire_insurance
- furniture