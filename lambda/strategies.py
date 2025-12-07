from abc import ABC, abstractmethod
from lol_api_handler import LoLApiHandler

class ChampionDataStrategy(ABC):
    """
    Strategy Pattern
    """
    def __init__(self):
        self.api_handler = LoLApiHandler()

    @abstractmethod
    def get_info(self, champion_name, **kwargs):
        pass

class RunesStrategy(ChampionDataStrategy):
    def get_info(self, champion_name, **kwargs):
        try:
            data = self.api_handler.get_champion_runes(champion_name.strip().capitalize())
            return (
                f"Para {champion_name}, los vientos del campo de batalla dictan una configuración más solemne. "
                f"La runa clave recomendada es {data['keystone']}, asentada en la senda ancestral de {data['primary_tree']}. "
                f"Como complemento, se sugiere abrazar el poder de la rama secundaria {data['secondary_tree']}, "
                f"garantizando un equilibrio entre agresión y temple digno de las más duras contiendas."
            )
        except Exception as e:
            return f"Ha ocurrido un error al intentar obtener la informacion de {champion_name}. Por favor, intenta con otra peticion."

class BuildStrategy(ChampionDataStrategy):
    def get_info(self, champion_name, **kwargs):
        try:
            data = self.api_handler.get_champion_build(champion_name.strip().capitalize())
            items = ", ".join(data['core_items'])
            return (
                f"La forja del destino de {champion_name} se fortalece mediante una secuencia de objetos clave: "
                f"{items}. Cada uno aporta un matiz particular a su estilo de combate, refinando su poder para "
                f"dominar los enfrentamientos cruciales. Para completar el conjunto, las botas recomendadas son "
                f"{data['boots']}, esenciales para moverse con determinación por la Grieta del Invocador."
            )
        except Exception:
            return f"Ha ocurrido un error al intentar obtener la informacion de {champion_name}. Por favor, intenta con otra peticion."

class MetaStatsStrategy(ChampionDataStrategy):
    def get_info(self, champion_name, **kwargs):
        try:
            metric = kwargs.get('metric', 'winrate')
            data = self.api_handler.get_meta_stats(metric.strip().capitalize(), champion_name.strip().capitalize())
            return (
                f"Las mareas del metajuego hablan del estado actual de {champion_name}. "
                f"Su {metric} se sitúa en {data['value']}, reflejando su desempeño en la sangrienta danza "
                f"que los invocadores libran día tras día. Estas cifras representan el pulso vivo del equilibrio "
                f"de la Grieta."
            )
        except Exception:
            return f"Ha ocurrido un error al intentar obtener la informacion de {champion_name}. Por favor, intenta con otra peticion."

class CounterStrategy(ChampionDataStrategy):
    def get_info(self, champion_name, **kwargs):
        try:
            data = self.api_handler.get_champion_counter(champion_name.strip().capitalize())
            counters = ", ".join(data['hard_counters'])
            return (
                f"En la historia de los enfrentamientos, incluso los más poderosos encuentran a quienes pueden "
                f"quebrar su determinación. {champion_name} sufre ante los siguientes rivales, capaces de "
                f"desmantelar su influencia en la batalla: {counters}. "
                f"Conocer estas amenazas permite preparar un enfoque más estratégico antes de adentrarse en la Grieta."
            )
        except Exception:
            return f"Ha ocurrido un error al intentar obtener la informacion de {champion_name}. Por favor, intenta con otra peticion."
