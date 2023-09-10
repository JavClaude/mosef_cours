import argparse

from src.cours.domain.usine_et_voiture.usine.usine import UsineDeVoiture


def cli_fabriquer_voiture() -> None:
    parseur_d_arguments_console = argparse.ArgumentParser(
        description="Parseur d'argument CLI pour fabriquer des voitures"
    )

    parseur_d_arguments_console.add_argument(
        "--type-de-la-voiture",
        type=str,
        required=True,
        choices=["décapotable", "électrique"],
        dest="type_de_la_voiture"
    )

    parseur_d_arguments_console.add_argument(
        "--marque",
        type=str,
        required=False,
        dest="marque",
        default="toyota"
    )

    parseur_d_arguments_console.add_argument(
        "--couleur",
        type=str,
        required=False,
        dest="couleur",
        default="jaune"
    )

    parseur_d_arguments_console.add_argument(
        "--puissance",
        type=int,
        required=False,
        dest="puissance",
        default=200
    )

    arguments_console = parseur_d_arguments_console.parse_args()

    voiture = UsineDeVoiture.fabriquer_une_voiture(
        arguments_console.type_de_la_voiture,
        arguments_console.marque,
        arguments_console.couleur,
        arguments_console.puissance
    )

    # Comme j'ai défini une abstraction, je sais que toutes les voitures implémentes ces méthodes
    voiture.démarrer_le_moteur()
    voiture.accélérer()
    voiture.eteindre_le_moteur()
