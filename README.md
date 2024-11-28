# Proyecto de Scraping en Django: Mercado Libre

Este proyecto utiliza **Django** junto con **Selenium** para realizar un scraping de productos desde Mercado Libre, enfocándose en la búsqueda de consolas PlayStation 5.

## Requisitos

Para ejecutar este proyecto en tu máquina local, necesitas:

- **Python 3.10 o superior**: Puedes descargarlo desde [aquí](https://www.python.org/downloads/).
- **Django 4.x**: Framework web en Python.
- **Selenium**: Biblioteca para automatizar la interacción con el navegador.
- **Chromedriver**: Necesario para usar Selenium con Google Chrome.

## Pasos para la instalación

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git


2. Crear un entorno virtual

Una vez que hayas clonado el repositorio, navega a la carpeta del proyecto y crea un entorno virtual con el siguiente comando:

cd tu_repositorio
python -m venv venv

3. Activar el entorno virtual
En Windows:

.\venv\Scripts\activate
En macOS/Linux:
source venv/bin/activate

4. Instalar las dependencias

Asegúrate de tener el archivo requirements.txt en tu proyecto. Para instalar todas las dependencias necesarias, ejecuta:

pip install -r requirements.txt

5. Descargar y configurar Chromedriver

El proyecto utiliza Selenium y Chromedriver para interactuar con el navegador Google Chrome. Debes asegurarte de que la versión de Chromedriver coincida con la versión de Google Chrome instalada en tu máquina.

6. Configurar Django

Crea las migraciones y ejecuta el servidor de desarrollo de Django.

python manage.py migrate

Ahora, ejecuta el servidor de desarrollo:

python manage.py runserver

7. Ejecutar el scraping

El scraping está configurado en la vista de Django acceder_a_mercadolibre. Puedes acceder a esta vista desde tu navegador web visitando:

http://127.0.0.1:8000/