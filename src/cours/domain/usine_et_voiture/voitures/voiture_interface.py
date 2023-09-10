from abc import abstractmethod


class VoitureInterface:
    @abstractmethod
    def démarrer_le_moteur(self) -> None:
        # Fournir une implémentation de la méthode
        pass

    @abstractmethod
    def accélérer(self) -> None:
        # Fournir une implémentation de la méthode
        pass

    @abstractmethod
    def eteindre_le_moteur(self) -> None:
        # Fournir une implémentation de la méthode
        pass

    @abstractmethod
    def la_voiture_est_fonctionnelle(self) -> bool:
        # Fournir une implémentation de la méthode
        pass

