from backend.models import Record


def get_random_meme(data):
    result = Record.get_random_record("ME")

    if not result:
        return "No tengo nada para ti"

    return "Aqui tienes humano: {}".format(result.data)
