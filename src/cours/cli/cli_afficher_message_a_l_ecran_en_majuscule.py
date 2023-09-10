import argparse

from src.cours.domain.afficher_message.afficher_message_a_l_ecran_en_majuscule import AfficherUnMessageALEcranEnMajuscule


def cli_afficher_un_message_en_majuscule() -> None:
    parseur_d_arguments_console = argparse.ArgumentParser(
        description="Parseur d'argument CLI pour afficher un message en majuscule"
    )

    parseur_d_arguments_console.add_argument(
        "--message-a-afficher",
        dest="message_a_afficher",
        required=False,
        default="message par défaut, en minuscule",
    )

    arguments_console = parseur_d_arguments_console.parse_args()

    afficher_un_message_en_majuscule_a_l_ecran = AfficherUnMessageALEcranEnMajuscule()
    afficher_un_message_en_majuscule_a_l_ecran.afficher_un_message_en_majuscule(arguments_console.message_a_afficher)
