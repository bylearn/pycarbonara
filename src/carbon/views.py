import json
import asyncio
import base64
import subprocess
from django.http.response import HttpResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.parse import urlencode
from wsgiref.util import FileWrapper


from .serializers import OptionsSerializer
from .custom_renderers import JPEGRenderer, PNGRenderer


# Create your views here.


class CarbonView(APIView):
    def post(self, request):
        options = OptionsSerializer(data=request.data)

        if options.is_valid():
            urlencoded = "https://carbon.now.sh/?" + urlencode(options.data)
            print(urlencoded)

            process = subprocess.Popen(
                ["python", "src/carbon/jobs.py", urlencoded],
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                encoding="utf-8",
            )

            stdout, stderr = process.communicate()

            exit_code = process.wait()
            image = stdout.replace("\n", "").replace("b'", "")[:-1]
            image = image.encode()
            image = base64.b64decode(image)

            return HttpResponse(image, content_type="image/png")
        return Response({"message": options.errors}, status=status.HTTP_400_BAD_REQUEST)
