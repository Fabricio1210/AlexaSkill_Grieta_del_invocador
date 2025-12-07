from strategies import RunesStrategy, BuildStrategy, MetaStatsStrategy, CounterStrategy

class GuiaInvocadorService:
    """
    Facade Pattern
    """
    def __init__(self):
        self.strategies = {
            'runes': RunesStrategy(),
            'build': BuildStrategy(),
            'stats': MetaStatsStrategy(),
            'counter': CounterStrategy()
        }

    def get_champion_runes(self, champion_name):
        return self.strategies['runes'].get_info(champion_name)

    def get_champion_build(self, champion_name):
        return self.strategies['build'].get_info(champion_name)

    def get_meta_stats(self, metric, champion_name):
        return self.strategies['stats'].get_info(champion_name, metric=metric)

    def get_champion_counter(self, champion_name):
        return self.strategies['counter'].get_info(champion_name)

    def get_game_tip(self):
        import random
        tips = [
            "No empujes la línea sin un objetivo; aprende a congelar (freeze) para castigar la posición del rival.",
            "Cronometra el inicio del jungla enemigo para predecir su posición a los 3:15 (Cangrejo).",
            "Mira el minimapa cada vez que mates a un súbdito (CS); es el equivalente a chequear tu postura en el gym.",
            "No sigas una build fija. Adapta tu resistencia (Armor vs MR) según el daño predominante enemigo.",
            "Si el oponente falla una habilidad clave (como la E de Lux), tienes una ventana de castigo de 8-12 segundos.",
            "Coloca centinelas en los campamentos enemigos, no solo en los arbustos del río, para saber dónde ESTARÁ el rival.",
            "Nunca regreses a base con la línea en una mala posición; empuja hasta la torre enemiga antes de irte.",
            "Una torre o un dragón valen más que perseguir a un soporte enemigo por todo el mapa.",
            "Domina a fondo 2 o 3 campeones. La maestría mecánica reduce el costo cognitivo, permitiéndote pensar en macro.",
            "Usa las señales (pings) de forma profesional. Evita el spam; la información debe ser clara y útil.",
            "15-20 súbditos equivalen económicamente a una muerte. No sacrifiques farm por jugadas de alto riesgo.",
            "Conoce el momento exacto en que tu campeón es más fuerte (ej. nivel 6 o el primer ítem completado).",
            "Como ADC/Mago, tu prioridad es sobrevivir. Ataca al objetivo más cercano que sea seguro golpear.",
            "Empuja las líneas laterales antes de que aparezca el Barón o el Dragón para crear presión dividida.",
            "Dedica tiempo a revisar tus muertes. Identifica si fue un error mecánico o de toma de decisiones.",
            "Aplique la misma disciplina que en sus rutinas de ejercicio; el 'tilt' nubla el juicio lógico necesario para ganar.",
            "Ataca al enemigo cuando este se disponga a dar el último golpe a un súbdito tuyo.",
            "Ajusta tus runas secundarias en la fase de selección según el emparejamiento (matchup) específico.",
            "No guardes el Flash 'para la próxima'. Úsalo para asegurar una ventaja temprana o evitar una muerte segura.",
            "Antes de empezar, identifica qué necesita tu equipo para ganar (¿Escalado?, ¿Pick-offs?, ¿Teamfight?)."
        ]
        return random.choice(tips)
