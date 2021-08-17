from src.main.tools.flocking_behavior.rules.alignment import alignment
from src.main.tools.flocking_behavior.rules.cohesion import cohesion
from src.main.tools.flocking_behavior.rules.separation import separation


def create_rules():
    rules = {'alignment': alignment,
             'cohesion': cohesion,
             'separation': separation}

    return rules
