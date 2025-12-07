import requests
import threading
import json

class LoLApiHandler:
    """
    Singleton Pattern
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(LoLApiHandler, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.base_url = "https://ddragon.leagueoflegends.com/cdn/15.24.1/data/en_US/champion"
        self._initialized = True

    def get_champion_runes(self, champion):
        try:
            response = requests.get(f'{self.base_url}/{champion}/runes', timeout=5)
            keystone = response["keystone"] 
            primary_tree = response["primary_tree"]
            secondary_tree = response["secondary_tree"]
        except Exception:
            #LA API HA REPORTADO FALLOS EN CIERTAS OCASIONES
            #SE UTILIZARAN JSONS COMO FALLBACK POR SI LA API DE RIOT FALLA
            try:
                with open("static/runes.json", 'r', encoding='utf-8') as f:
                    datos_json = json.load(f)
                    keystone = datos_json[champion]["Clave"]
                    primary_tree = datos_json[champion]["Ruta Primaria"]
                    secondary_tree = datos_json[champion]["Ruta Secundaria"]
            except FileNotFoundError:
                raise
        return {
            "keystone": keystone,
            "primary_tree": primary_tree,
            "secondary_tree": secondary_tree
        }

    def get_champion_build(self, champion):
        try:
            response = requests.get(f'{self.base_url}/{champion}/builds', timeout=5)
            core_items = response["core_items"] 
            boots = response["boots"]
        except Exception:
            #LA API HA REPORTADO FALLOS EN CIERTAS OCASIONES
            #SE UTILIZARAN JSONS COMO FALLBACK POR SI LA API DE RIOT FALLA
            try:
                with open("static/builds.json", 'r', encoding='utf-8') as f:
                    datos_json = json.load(f)
                    core_items = []
                    core_items.append(datos_json[champion]["Objeto 1"])
                    core_items.append(datos_json[champion]["Objeto 2"])
                    core_items.append(datos_json[champion]["Objeto 3"])
                    core_items.append(datos_json[champion]["Objeto 4"])
                    core_items.append(datos_json[champion]["Objeto 5"])
                    boots = datos_json[champion]["Botas"]
            except FileNotFoundError:
                raise
        return {
            "core_items": core_items,
            "boots": boots
        }

    def get_meta_stats(self, metric, champion):
        try:
            response = requests.get(f'{self.base_url}/{champion}/meta', timeout=5)
            value = response["stats"][metric]
        except Exception:
            #LA API HA REPORTADO FALLOS EN CIERTAS OCASIONES
            #SE UTILIZARAN JSONS COMO FALLBACK POR SI LA API DE RIOT FALLA
            try:
                with open("static/stats.json", 'r', encoding='utf-8') as f:
                    datos_json = json.load(f)
                    value = float(datos_json[champion][metric])*100
            except FileNotFoundError:
                raise
        return {
            "metric": metric,
            "value": str(value)+"%"
        }

    def get_champion_counter(self, champion):
        try:
            response = requests.get(f'{self.base_url}/{champion}/meta', timeout=5)
            value = response["counterpick"]
        except Exception:
            #LA API HA REPORTADO FALLOS EN CIERTAS OCASIONES
            #SE UTILIZARAN JSONS COMO FALLBACK POR SI LA API DE RIOT FALLA
            try:
                with open("static/counters.json", 'r', encoding='utf-8') as f:
                    datos_json = json.load(f)
                    counters = datos_json[champion]["Counters"]
            except FileNotFoundError:
                raise
        return {
            "hard_counters": counters
        }
