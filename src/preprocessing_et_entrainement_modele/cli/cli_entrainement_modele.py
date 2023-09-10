import argparse

from src.preprocessing_et_entrainement_modele.infrastructure.recuperation_donnees_titanic import RecuperationDesDonnéesDuTitanic
def cli_entrainement_modele() -> None:
    parseur_d_arguments_cli = argparse.ArgumentParser(
        "Entrainement et sauvegarde d'un modele depuis une CLI"
    )
    parseur_d_arguments_cli.add_argument(
        "--nombre-arbres-random-forest",
    type= int,
required =False,
        default  =50,
        dest="nombre_arbre"
    )
    arguments = parseur_d_arguments_cli.parse_args()

    dataframe_avec_les_données_du_titanic = RecuperationDesDonnéesDuTitanic.get_données_du_titanic()

    # Preprocessing / Transformation
    print("Preprocessing")

    # Entrainement du modèle
    print("Entrainement")

    # Sauvegarder des artefacts
    print("Sauvegarde"
          )
