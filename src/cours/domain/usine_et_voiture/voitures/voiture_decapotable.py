from src.cours.domain.usine_et_voiture.voitures.voiture import Voiture


class VoitureDecapotable(Voiture):
    def __init__(self, marque: str, couleur: str, puissance: int):
        super().__init__(marque, couleur, puissance)
        self.__le_toit_est_ouvert = False

    def ouvrir_le_toit(self) -> None:
        self.__le_toit_est_ouvert = True
        print("Ouverture du toit")

    def fermer_le_toit(self) -> None:
        print("Fermeture du toit")