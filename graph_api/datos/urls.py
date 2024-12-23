from django.urls import path
from .views import ventas_reporte_template, VentaGraficoView

urlpatterns = [
    path('reporte/', ventas_reporte_template, name='reporte_template'),
    path('graph/', VentaGraficoView.as_view(), name='reporte_api'),
]
