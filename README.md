# Pysupuesto
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Modulo de python que permite descargar información presupuestaria de [Presupuesto Abierto](https://www.presupuestoabierto.gob.ar/sici/datos-abiertos). El sitio contiene diversa información presupuestaria desde el ejercicio 1995 a la actualidad.

La motivación para programar este modulo fue la necesidad de contar, de forma sencilla, con series temporales de información presupuestaria. El sitio del ciudadano permite descargar año por año, pero no una base con una serie temporal.

Pysupuesto, mediante ``get_data`` descarga, por el momento, información de crédito y su ejecución, y de recursos. De periodicidad anual, mensual y diaria (según el periodo). 

Tambien, utilizando ``get_docs``, muestra los recursos (en términos de información) disponibles para cada año, por si se necesita descargar manualmente información complementaria.

## Requirimientos

- Python 3.8
- beautifulsoup4=>4.10.0
- bs4=>0.0.1
- pandas=>1.3.3

## Modo de uso

Por el momento no está empaquetado y disponible mediante ``pip``, por lo que se debe copiar localmente:

- Copiar el archivo pysupuesto.py en el directorio de trabajo.
- Importarlo con ``import paysupuesto`` en el archivo de trabajo.

### Sintaxis GET_DATA
 
	df = pysupuesto.get_data('tipo', 'periodicidad', ejercicio inicio, ejercicio cierre)
	
Donde:

- ``tipo``: Por el momento, sólo toma dos valores
    - ``recursos``: Devuelve los recursos presupeustarios.
	- ``credito``: Devuelve la ejecución presupuestaria.
- ``periodicidad``: Dependiendo el año, puede ser:
	- ``a``: Anual (desde 1995 a 2021)
	- ``m``: Mensual (desde 1995 a 2021)
	- ``d``: Diaria (desde 2017 a 2021)
- ``ejercicio inicio``: Ejercicio desde el cual se quiere descargar la información
- ``ejercicio cierre``: Hasta el ejercicio hasta el cual se quiere descargar información. Puede omitirse para sólo descargar 'ejercicio inicio'.

La información es descargada a un dataframe (llamado ``df`` en el ejemplo).

![imagen](https://user-images.githubusercontent.com/660448/133935451-02c52268-383d-4ee9-b2a9-e19cd2cc201f.png)

### Ejemplos

#### Crédito y ejecución

Descargar la información del crédito presupuestario y su ejecución del ejercicio 2018, con periodicidad diaria:

	df = pysupuesto.get_data('credito','d', 2018)
	
Descargar la información del crédito presupuestario y su ejecución desde el ejercicio 1995 al 2021, con periodicidad anual:

	df = pysupuesto.get_data('credito','a', 1995,2021)

#### Recursos 

Descargar la información de recursos presupuestarios del ejercicio 1997, con periodicidad mensual:

	df = pysupuesto.get_data('recursos','m', 1997)
	
Descargar la información de recursos presupuestarios desde el ejercicio 2001 al ejercicio 2005, con periodicidad anual:

	df = pysupuesto.get_data('recursos','a', 2001, 2005)
	
### Sintaxis GET_DOCS

	pysupuesto.get_docs(ejercicio)

Devuelve un print con todos los archivos disponibles para ese ejercicio.

![imagen](https://user-images.githubusercontent.com/660448/133935782-8763d117-0d48-4a26-bba2-f713781e1cd0.png)

## ToDo:

- Empaquetar y compartir en [pypi](https://pypi.org/) para que esté disponible mediante ``pip install``
- Mejorar el loggin.
- Intentar analizar toda la información disponible (para eso cree ``get_docs``) para expandir el modulo y poner a disposición más descargas.


	
