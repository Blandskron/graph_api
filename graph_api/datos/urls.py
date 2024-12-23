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
