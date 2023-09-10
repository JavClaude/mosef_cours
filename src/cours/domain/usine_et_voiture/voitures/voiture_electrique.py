from src.cours.domain.usine_et_voiture.voitures.voiture import Voiture


class VoitureElectrique(Voiture):
    def __init__(self, marque: str, couleur: str, puissance: int):
        super().__init__(marque, couleur, puissance)
        self.__niveau_de_batterie = 0

    def recharger_la_batterie(self) -> None:
        print("Rechargement de la batterie, niveau de batterie actuel: {}".format(self.__niveau_de_batterie))

    # On n'accède pas aux attributs / méthodes de l'instance donc la méthode doit être statique
    # On ne pourra pas utiliser self. (l'instance)
    @staticmethod
    def debrancher_la_recharge() -> None:
        print("Debranchement de la recharge")