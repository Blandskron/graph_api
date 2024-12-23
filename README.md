# Proyecto Django: API de Reportes de Ventas

Este proyecto es una API de Django que permite generar reportes de ventas y gráficos relacionados con los datos de ventas, utilizando Django REST Framework y Matplotlib.

---

## Requisitos

Antes de empezar, asegúrate de tener instalado lo siguiente:

1. **Python 3.8 o superior**
2. **Pip**
3. **Virtualenv** (opcional pero recomendado)

---

## Instalación

### 1. Clona el repositorio
```bash
$ git clone <URL_DEL_REPOSITORIO>
$ cd <NOMBRE_DEL_PROYECTO>
```

### 2. Crea un entorno virtual (opcional)
```bash
$ python -m venv venv
$ source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias
Ejecuta el siguiente comando para instalar las librerías requeridas:
```bash
$ pip install -r requirements.txt
```

Si no tienes un archivo `requirements.txt`, usa el siguiente comando para generarlo:
```bash
$ pip freeze > requirements.txt
```

### Librerías necesarias:
A continuación, se detallan las librerías que debes instalar:

1. **Django**: Framework principal para el desarrollo del backend.
    ```bash
    $ pip install django
    ```

2. **Django REST Framework (DRF)**: Herramienta para crear APIs RESTful.
    ```bash
    $ pip install djangorestframework
    ```

3. **Matplotlib**: Para generar gráficos.
    ```bash
    $ pip install matplotlib
    ```

4. **Pillow**: Para manejar imágenes (opcional si trabajas con archivos).
    ```bash
    $ pip install pillow
    ```

---

## Estructura del Proyecto
```
<PROYECTO>/
├── manage.py
├── <NOMBRE_APP>/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── <PROYECTO>/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates/
    └── datos/
        └── reporte.html
```

---

## Configuración del Proyecto

### 1. Configuración de `settings.py`
Asegúrate de que las siguientes aplicaciones estén registradas en `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    '<NOMBRE_APP>',
]
```

---

## Configuración de URLs

### Archivo `urls.py` principal
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datos.urls')),
    path('api/', include('docs.urls')),
]
```

### Archivo `urls.py` de la aplicación
```python
from django.urls import path
from .views import (
    ventas_reporte_template,
    VentaGraficoView,
    TotalVentasPorProductoView,
    IngresosPorProductoView,
    GraficoIngresosPorProductoView,
    VentasPorFechaView,
    EstadisticasGeneralesView
)

urlpatterns = [
    path('reporte/', ventas_reporte_template, name='reporte_template'),
    path('api/graph/', VentaGraficoView.as_view(), name='reporte_api'),
    path('api/total-ventas-producto/', TotalVentasPorProductoView.as_view(), name='total_ventas_producto'),
    path('api/ingresos-producto/', IngresosPorProductoView.as_view(), name='ingresos_producto'),
    path('api/grafico-ingresos/', GraficoIngresosPorProductoView.as_view(), name='grafico_ingresos'),
    path('api/ventas-por-fecha/', VentasPorFechaView.as_view(), name='ventas_por_fecha'),
    path('api/estadisticas/', EstadisticasGeneralesView.as_view(), name='estadisticas_generales'),
]
```

---

## Migraciones
Crea y aplica las migraciones para configurar tu base de datos:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

---

## Ejecución del Servidor
Inicia el servidor de desarrollo de Django:

```bash
$ python manage.py runserver
```
Accede a la aplicación en tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Endpoints

### 1. **Vista del Reporte**
- **URL**: `/reporte/`
- **Método**: `GET`
- **Descripción**: Muestra la plantilla HTML del reporte de ventas.

### 2. **Gráfico de Ventas**
- **URL**: `/api/graph/`
- **Método**: `GET`
- **Descripción**: Devuelve un gráfico de ventas por producto en formato base64.

### 3. **Total de Ventas por Producto**
- **URL**: `/api/total-ventas-producto/`
- **Método**: `GET`
- **Descripción**: Devuelve la cantidad total de ventas agrupadas por producto.

### 4. **Ingresos por Producto**
- **URL**: `/api/ingresos-producto/`
- **Método**: `GET`
- **Descripción**: Devuelve los ingresos totales generados por cada producto.

### 5. **Gráfico de Ingresos por Producto**
- **URL**: `/api/grafico-ingresos/`
- **Método**: `GET`
- **Descripción**: Genera un gráfico de ingresos totales por producto en formato base64.

### 6. **Ventas por Fecha**
- **URL**: `/api/ventas-por-fecha/?fecha_inicio=<YYYY-MM-DD>&fecha_fin=<YYYY-MM-DD>`
- **Método**: `GET`
- **Descripción**: Devuelve las ventas dentro de un rango de fechas especificado.

### 7. **Estadísticas Generales**
- **URL**: `/api/estadisticas/`
- **Método**: `GET`
- **Descripción**: Devuelve estadísticas generales como total de ventas, ingresos y producto más vendido.

---

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Puedes modificarlo y utilizarlo como desees.

---
