import logging


def generate_invitations(template, attendees):
    """
    Génère des invitations personnalisées à partir d'un template et d'une liste de participants

    Args:
        template (str): Le template de l'invitation avec des placeholders
        attendees (list): Une liste de dictionnaires contenant les données des participants
    """
    # Vérifie que le template est une chaîne de caractères
    if not isinstance(template, str):
        logging.error("Template is not a string.")
        return

    # Vérifie que attendees est une liste de dictionnaires
    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        logging.error("Attendees is not a list of dictionaries.")
        return

    # Vérifie que le template n'est pas vide
    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    # Vérifie que la liste des participants n'est pas vide
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Génère une invitation pour chaque participant
    for i, attendee in enumerate(attendees, start=1):
        invitation = template
        # Remplace les placeholders par les valeurs du participant
        for key, value in attendee.items():
            invitation = invitation.replace(
                f"{{{key}}}", str(value) if value is not None else "N/A")
        # Écrit l'invitation dans un fichier
        with open(f"output_{i}.txt", "w") as file:
            file.write(invitation)


# Exemple d'utilisation
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Lit le template depuis un fichier
with open('template.txt', 'r') as file:
    template_content = file.read()

# Génère les invitations
generate_invitations(template_content, attendees)
