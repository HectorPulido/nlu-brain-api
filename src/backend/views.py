from django.conf import settings
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from .models import Key, Record, ChannelType
from .serializers import RecordSerializer

from chatbot.easy_intents import *
from chatbot.search import search_resource
from chatbot.random_meme import get_random_meme


class CheckKeyMixin:
    def check_key(self, request):
        name = request.data.get("name")
        private_key = request.data.get("private_key")

        wh = Key.get_key_data(name)
        if not wh:
            return False

        return private_key == wh


class InitialConfigurationViewset(APIView, CheckKeyMixin):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        if not self.check_key(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        channel_config = ChannelType.get_all_channels_as_dict()
        return Response(channel_config, status=status.HTTP_200_OK)


class ChatphraseViewset(APIView, CheckKeyMixin):
    authentication_classes = ()
    permission_classes = ()

    intents = {
        "doubts": doubts,
        "search": search_resource,
        "meme": get_random_meme,
        None: gpt3_response,
    }

    def get_text(self, intent, data):
        return self.intents[intent](data)

    def post(self, request, *args, **kwargs):
        if not self.check_key(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        filtered_response = Key.get_key_data("filtered_response")

        query = request.data.get("query")
        if filter_response(query):
            if not filtered_response:
                filtered_response = "Lo siento no puedo responder a eso."

            return Response(filtered_response, status=status.HTTP_200_OK)

        parsing = settings.CHATBOT.predict(query)

        try:
            intent = parsing["intent"]["intentName"]
        except:
            intent = None

        if intent not in self.intents:
            intent = None

        parsing["history"] = request.data.get("history")
        response = self.get_text(intent, parsing)

        if filter_response(response):
            if not filtered_response:
                filtered_response = "Lo siento no puedo responder a eso."

            return Response(filtered_response, status=status.HTTP_200_OK)

        return Response(response, status=status.HTTP_200_OK)


class RecordViewset(viewsets.ModelViewSet, CheckKeyMixin):
    authentication_classes = ()
    permission_classes = ()

    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def create(self, request):
        if not self.check_key(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        record = serializer.save()
        return Response(record, status=status.HTTP_201_CREATED)
