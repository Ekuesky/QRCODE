# qr_api/views.py
import qrcode
from io import BytesIO
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import QRCodeSerializer
from django.shortcuts import render

def index(request):
 return render(request, 'index.html')

@api_view(['POST'])
def generate_qr_code(request):
    if request.method == 'POST':
        serializer = QRCodeSerializer(data=request.data)

        if serializer.is_valid():
            url_to_encode = serializer.validated_data['url']
            qr = qrcode.QRCode(
              version=1,
              error_correction=qrcode.constants.ERROR_CORRECT_L,
              box_size=10,
              border=4,
          )
            qr.add_data(url_to_encode)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            return HttpResponse(buffer, content_type='image/png')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Please use a POST request to generate the QR code"})
