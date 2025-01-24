#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Lève une exception de type NameError avec un message personnalisé.

    Args:
        message (str): Message à inclure dans l'exception.

    Cette fonction permet de lever une exception de type NameError avec
    un message fourni par l'utilisateur.
    """
    raise NameError(message)  # Lève une exception NameError avec le message
