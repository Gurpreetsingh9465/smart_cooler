from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
import pandas as pd
import os

@api_view(['POST'])
def storeData(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    with open(os.path.join(settings.BASE_DIR, "static", "file.csv"),"a+") as f:
        f.write('\n'+received_json_data["data"])
    return Response(status=200)