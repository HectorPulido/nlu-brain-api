from django.conf import settings
from backend.models import Record
from chatbot.elastic_search import SearchClient


def search_resource(data):
    try:
        value = data["slots"][0]["rawValue"]
    except:
        return "No tengo nada para ti"

    # Not using Elastic
    if not settings.ELASTICSEARCH:
        result = Record.search_record(value.lower(), "RS")

        if not result:
            return "No tengo nada para ti relacionado a {}".format(value)

        return "Aqui tienes humano: {}".format(result)

    # Using Elastic
    ...

