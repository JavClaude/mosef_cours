from src.cours.domain.usine_et_voiture.voitures.voiture_interface import VoitureInterface
from src.cours.domain.usine_et_voiture.voitures.voiture_decapotable import VoitureDecapotable
from src.cours.domain.usine_et_voiture.voitures.voiture_electrique import VoitureElectrique


class UsineDeVoiture:
    @staticmethod
    def fabriquer_une_voiture(type: str, marque: str, couleur: str, puissance: int) -> VoitureInterface:
        print("Création d'une voiture du type: {}, de couleur: {} et de puissance: {}".format(
            type, couleur, puissance
        ))
        if type == "décapotable":
            voiture = VoitureDecapotable(marque, couleur, puissance)
        elif type == "électrique":
            voiture = VoitureElectrique(marque, couleur, puissance)
        else:
            raise ValueError("Le type de la voiture est incorrect, merci de choisir entre [décapotable et électrique]")

        if UsineDeVoiture._tester_si_la_voiture_est_fonctionnelle(voiture):
            return voiture
        raise Exception("La voiture n'est pas fonctionnelle")

    @staticmethod
    def _tester_si_la_voiture_est_fonctionnelle(voiture_a_tester: VoitureInterface) -> bool:
        # On imagine qu'on a des exceptions qui sont levées a l'intérieur de ces méthodes
        la_voiture_est_fonctionnelle = voiture_a_tester.la_voiture_est_fonctionnelle()
        if la_voiture_est_fonctionnelle:
            return True
        return False
