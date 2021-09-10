# Aplicación sobre el ejercicio1 para la posicion de Lide Tecnológico

Esta aplicación se basa en la creación de un API-RESTFUL que permita consultar los valores de conversion de valores de EURO a DOLAR los valores fueron consultados desde la pagina: [servicio de Yahoo](https://es-us.finanzas.yahoo.com/quote/EURUSD%3DX/history?p=EURUSD%3DX) 

## Instalación

La aplicación se ha desarrollado usando el Framework Django versión 3.2.+ con la versión de Python 3
.8

Las librerías se instalan usando el archivo requerimientos.txt. Se puede ejecutar la siguiente línea
en el terminal

`pip install -r requerimientos.txt`

## Configuración

Al estar en un ambiente en producción nos ubicamos en la carpeta *ejercicio1*, activamos el entorno virtual de ser el caso y ejecutamos 

`python manage.py runserver`

Esto permite que el API este activo 

Luego volvemos al directorio raiz donde se encuetra el archivo `client.py`

Ejecutamos el archivo de la siguiente manera:

`python client.py`

Esto llama al servicio y golpea al webhook (https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9)

Eso es todo!!




