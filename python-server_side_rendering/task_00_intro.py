#!/usr/bin/python3
""" Module qui génère des invitations personnalisées """


import os


def generate_invitations(template_content, attendees):
    """ Fonction qui génère des invitations personnalisées
              à partir d'un modèle et d'une liste de participants."""

    # Vérifier si template est une chaîne de caractères.
    if not isinstance(template_content, str):
        print(f'Invalid template type: {type(template_content)}')
        return
    # Vérifier si attendees est une liste.
    if not isinstance(attendees, list):
        print(f'Invalid attendees type: {type(attendees)}')
        return

    # Boucle qui parcourt chaque élément de la liste attendees.
    for i, element in enumerate(attendees):
        if not isinstance(element, dict):
            print(f'Invalid attendee element at index {i}: {type(element)}')
            return

    # Gérer les cas où le template est vide.
    if template_content == "":
        print("Template is empty, no output files generated.")
        return

    # Gérer les cas où la liste attendees est vide.
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Numéroter les invitations générées.
    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Créer le texte de l'invitation en remplaçant les espaces réservés dans le modèle.
        invitation_text = template_content
        invitation_text = invitation_text.replace("{name}", name)
        invitation_text = invitation_text.replace("{event_title}", event_title)
        invitation_text = invitation_text.replace("{event_date}", event_date)
        invitation_text = invitation_text.replace("{event_location}", event_location)

        # Écrire le texte de l'invitation dans un fichier nommé de manière unique.
        filename = f"output_{i}.txt"
        if (os.path.exists(filename)):
            os.remove(filename)
        with open(filename, 'w') as file:
            file.write(invitation_text)
