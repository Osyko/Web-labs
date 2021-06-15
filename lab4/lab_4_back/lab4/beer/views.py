from json import dumps, loads

import logging
import redis
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpRequest

from .models import Company
from .serializer import MySerializer

logger = logging.getLogger('django')
redis_cache = redis.Redis('localhost', port=6379, db=15)

class BeerView(APIView):

     def __init__(self):
        super().__init__()

        self.recruit = Company.objects.all()
        self.serializer = MySerializer

    #read
     def get(self, request: Request):
        id = request.query_params.get('id', None)
        if id is None:
            data = self.recruit.all()
            data_serializer = self.serializer(data, many=True)
            return Response(data_serializer.data, status=200, content_type='application/json')

        return self.get_detail(id)

    #update
     def post(self, request: HttpRequest):
        data = loads(request.body)
        data_serializer = self.serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)

        model = Company(**data_serializer.data)
        model.pk = data_serializer.data['id']
        model.save()
        redis_cache.delete(model.pk)
        return Response(status=200)


    #create
     def put(self, request: HttpRequest):
        data = loads(request.body)
        data_serializer = self.serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)
        Company(**data_serializer.data).save()
        return Response(status=201)

    #delete
     def delete(self, request: HttpRequest):
        try:
            id = loads(request.body)['id']
            self.recruit.get(pk=id).delete()
            redis_cache.delete(id)
        except:
            return Response(status=400)

        return Response(status=200)



     def get_detail(self, id: int):
        logger.info(f"getting record with id={id}")
        cache = redis_cache.get(id)
        if cache:
            logger.info(f"got record with id={id} from redis")
            cache = loads(cache)
            return Response(cache)

        logger.info(f"had to query record with id={id} from db")

        record = self.recruit.get(pk=id)
        if not record:
            return Response(status=400)
        data_serializer = self.serializer(record)
        data = data_serializer.data

        redis_cache.set(id, dumps(data))
        redis_cache.expire(id, 60*8)
        return Response(data )