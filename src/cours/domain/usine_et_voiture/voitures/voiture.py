import pandas as pd

from src.cours.domain.usine_et_voiture.voitures.voiture_interface import VoitureInterface


class Voiture(VoitureInterface):
    def __init__(self, marque: str, couleur: str, puissance: int):
        self.marque = marque
        self.couleur = couleur
        self.puissance = puissance
        self.__est_démarée = False

    def démarrer_le_moteur(self) -> None:
        self.__est_démarée = True
        print(
            "La voiture\n\tMarque: {}\n\tCouleur: {}\n\tPuissance: {}\nDémarre!\n".format(
                self.marque, self.couleur, self.puissance
            )
        )

    def accélérer(self) -> None:
        if not self._la_voiture_est_démarrée():
            raise Exception("Merci de démarrer le moteur avant d'accélérer")
        print(
            "La voiture accélère.........."
        )

    def eteindre_le_moteur(self) -> None:
        self.__est_démarée = False
        print(
            "Le moteur s'arrête"
        )

    def la_voiture_est_fonctionnelle(self) -> bool:
        # Implémenter les règles métiers ou machine learning
        print("Voiture fonctionnelle!")
        return True

    def _la_voiture_est_démarrée(self) -> bool:
        return self.__est_démarée
