import asyncio
import base64
import json
import os
import subprocess
from urllib.parse import urlencode
from wsgiref.util import FileWrapper

from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .custom_renderers import JPEGRenderer, PNGRenderer
from .serializers import OptionsSerializer

# Create your views here.


class CarbonView(APIView):
    def post(self, request):
        options = OptionsSerializer(data=request.data)

        if options.is_valid():
            urlencoded = "https://carbon.now.sh/?" + urlencode(options.data)

            jobs = os.path.join(
                settings.BASE_DIR,
                "carbon/jobs.py",
            )
            process = subprocess.Popen(
                ["python", jobs, urlencoded],
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
