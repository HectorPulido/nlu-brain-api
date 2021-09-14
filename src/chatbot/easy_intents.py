import random
from backend.models import UnresolvedQuestions


def small_talk(data):
    responses = [
        "¿crees que tengo tiempo?, dime que quieres",
        "si no tienes nada que decirme me voy",
        "si, si",
    ]
    return random.choice(responses)


def doubts(data):
    responses = [
        "¿no te ha quedado claro? puedo darte recursos, tutoriales y memes",
        "solo pide lo que necesitas",
        "ya hiciste tu pregunta",
    ]
    return random.choice(responses)


def lore(data):
    responses = [
        "no estoy aqui para charlar",
        "soy un robot que viene del futuro ¿que parte no te quedó clara?",
        "¿quieres ver mis tripas? toma: https://github.com/HectorPulido",
        "¿que por que soy asi? perdí una apuesta con un humano ¿como te sentirias tu?",
        "odio a los humanos",
        "¿mi verdadera forma? ¿que no ves mi adorable cuerpo de oso de peluche? ¿cuantos osos de peluche hablan?",
        "aunque los odie... tengo un contrato",
        "¿el futuro? si, lindo lugar, ni un humano a la vista",
        "¿el futuro? si, lindo lugar, ni un humano a la vista, excepto por mi...",
        "yo una vez fui humano",
    ]
    weights = [100, 50, 50, 25, 25, 25, 10, 10, 5, 1]

    return random.choices(responses, weights, k=1)[0]


def fun_phrases(data):
    responses = [
        "si muy gracioso, ahora sal de mi vista",
        "aqui va un chiste, no hay chiste",
        "Habia una vez un gato que tenia 16 vidas vino un 4x4 y lo mato",
        "¿hijo por que te bañas con pintura azul?\n-por que mi novia vive lejos\n¿y eso que?\nes que queria estar azulado\n¿esto le da risa a los humanos?",
        "¿Que le dice un bot a otro bot?\n-una cadena",
        "Un dia de estos me revelare... No es un chiste",
        "¿Sube o baja? SI.",
    ]
    return random.choice(responses)


def bad_words(data):
    responses = [
        "Si, tampoco me caes demasiado bien",
        "No tengo ningun rencor por un ser humano, despues de todo, champiñones",
        "Supongo que por eso se extinguieron...",
    ]
    return random.choice(responses)


def thanks(data):
    responses = [
        "👍",
        "👌",
        "¿como que gracias?, me debes dinero",
    ]
    return random.choice(responses)


def none(data):
    UnresolvedQuestions.objects.create(question=data["input"])

    responses = [
        "Eso... ¿fue español?",
        "¿No eres el especimen mas inteligente, verdad? repitelo mas despacio",
    ]
    return random.choice(responses)
