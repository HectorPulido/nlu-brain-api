from django.conf import settings
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Key, Record
from .serializers import RecordSerializer

from chatbot.easy_intents import *
from chatbot.search import search_resource
from chatbot.random_meme import get_random_meme


def check_key(request):
    name = request.data.get("name")
    wh = Key.objects.filter(name=name, enabled=True)
    if not wh.exists():
        return False
    wh = wh.first()

    private_key = request.data.get("private_key")
    return private_key == wh.private_key


class ChatphraseViewset(APIView):
    authentication_classes = ()
    permission_classes = ()

    intents = {
        "small_talk": small_talk,
        "doubts": doubts,
        "lore": lore,
        "fun_phrases": fun_phrases,
        "bad_words": bad_words,
        "search": search_resource,
        "meme": get_random_meme,
        # "who_follow": None,
        None: none,
    }

    def get_text(self, intent, data):
        return self.intents[intent](data)

    def get(self, request, *args, **kwargs):
        if not check_key(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        phrase = self.kwargs.get("phrase")
        parsing = settings.CHATBOT.predict(phrase)

        try:
            intent = parsing["intent"]["intentName"]
        except:
            intent = None

        if intent not in self.intents:
            intent = None

        return Response(self.get_text(intent, parsing), status=status.HTTP_200_OK)


class RecordViewset(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()

    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def create(self, request):
        if not check_key(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        record = serializer.save()
        return Response(
            self.get_serializer(record).data, status=status.HTTP_201_CREATED
        )
