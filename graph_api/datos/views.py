from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Venta
from .serializers import VentaSerializer
from django.http import JsonResponse
import matplotlib.pyplot as plt
import io
import base64

def ventas_reporte_template(request):
    return render(request, 'datos/reporte.html')

class TotalVentasPorProductoView(APIView):
    def get(self, request):
        ventas = Venta.objects.all()
        resultado = {}

        # Calcular las cantidades totales por producto
        for venta in ventas:
            if venta.producto in resultado:
                resultado[venta.producto] += venta.cantidad
            else:
                resultado[venta.producto] = venta.cantidad

        return Response(resultado)

class IngresosPorProductoView(APIView):
    def get(self, request):
        ventas = Venta.objects.all()
        resultado = {}

        # Calcular ingresos totales por producto
        for venta in ventas:
            if venta.producto in resultado:
                resultado[venta.producto] += venta.cantidad * float(venta.precio)
            else:
                resultado[venta.producto] = venta.cantidad * float(venta.precio)

        return Response(resultado)

class GraficoIngresosPorProductoView(APIView):
    def get(self, request):
        ventas = Venta.objects.all()

        # Calcular ingresos totales por producto
        productos = []
        ingresos = []
        resultado = {}

        for venta in ventas:
            if venta.producto in resultado:
                resultado[venta.producto] += venta.cantidad * float(venta.precio)
            else:
                resultado[venta.producto] = venta.cantidad * float(venta.precio)

        productos = list(resultado.keys())
        ingresos = list(resultado.values())

        # Crear un gráfico
        plt.figure(figsize=(10, 6))
        plt.bar(productos, ingresos, color='green')
        plt.title('Ingresos por Producto')
        plt.xlabel('Producto')
        plt.ylabel('Ingresos Totales')
        plt.tight_layout()

        # Convertir el gráfico a imagen base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        # Respuesta JSON
        return Response({
            'grafico': image_base64
        })

class VentasPorFechaView(APIView):
    def get(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')

        if not fecha_inicio or not fecha_fin:
            return Response({"error": "Debe proporcionar fecha_inicio y fecha_fin"}, status=400)

        ventas = Venta.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
        serializer = VentaSerializer(ventas, many=True)

        return Response(serializer.data)

class VentaGraficoView(APIView):
    def get(self, request):
        # Datos de ventas
        ventas = Venta.objects.all()
        serializer = VentaSerializer(ventas, many=True)

        # Crear un gráfico
        productos = [venta.producto for venta in ventas]
        cantidades = [venta.cantidad for venta in ventas]

        plt.figure(figsize=(10, 6))
        plt.bar(productos, cantidades, color='skyblue')
        plt.title('Ventas por Producto')
        plt.xlabel('Producto')
        plt.ylabel('Cantidad')
        plt.tight_layout()

        # Convertir el gráfico a imagen base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        # Respuesta JSON
        return Response({
            'datos': serializer.data,
            'grafico': image_base64
        })

class EstadisticasGeneralesView(APIView):
    def get(self, request):
        ventas = Venta.objects.all()

        total_ventas = sum([venta.cantidad for venta in ventas])
        ingresos_totales = sum([venta.cantidad * float(venta.precio) for venta in ventas])
        producto_mas_vendido = max(ventas, key=lambda v: v.cantidad).producto if ventas else None

        return Response({
            'total_ventas': total_ventas,
            'ingresos_totales': ingresos_totales,
            'producto_mas_vendido': producto_mas_vendido
        })
