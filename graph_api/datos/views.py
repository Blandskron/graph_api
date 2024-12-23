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
