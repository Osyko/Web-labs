from json import loads
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import CalculateArea
from .models import DivRequest, DivResponse
from .serializers import DivRequestSerializer, DivResponseSerializer


class AppView(APIView):

    def post(self, request: HttpRequest):
        parsed_data = loads(request.body)

        request_data_serializer = DivRequestSerializer(data=parsed_data)
        if not request_data_serializer.is_valid():
            return Response(status=400)

        request_data = DivRequest(**request_data_serializer.validated_data)
        div_result = CalculateArea.calc(request_data.input_value)

        response_data = DivResponse(div_result)
        response_data_serializer = DivResponseSerializer(response_data)
        response = Response(response_data_serializer.data, content_type='application/json')

        return response