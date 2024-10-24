import json

from .models import *


BASEX = 0
BASEY = 0
SUBSTATIONDELAY = 18

with open("signals.json") as f:
    signals = json.load(f)

def createScreen(width: int, height: int, entity_number: int) -> tuple:
    """Screen ceration function"""
    screen = []
    connectionPorts = []
    wires = []

    signal_name_type = tuple(signals.items())
    signal_counter = 0

    entity_number += 1

    last_substation = None

    localdelayW = width // SUBSTATIONDELAY + int((width - (width // SUBSTATIONDELAY) * SUBSTATIONDELAY) // (SUBSTATIONDELAY / 2)) + 1
    localdelayH = height // SUBSTATIONDELAY + int((height - (height // SUBSTATIONDELAY) * SUBSTATIONDELAY) // (SUBSTATIONDELAY / 2)) + 1

    for x in range(localdelayW):
        if last_substation is not None:
            wires.append(
                [
                    last_substation, 5, entity_number, 5
                ]
            )

        last_substation = entity_number

        if x == localdelayW - 1:
            connection_substation = entity_number

        for y in range(localdelayH):
            screen.append(
                Entity(
                    entity_number=entity_number,
                    name="substation",
                    position=Position(
                        x=BASEX + x * SUBSTATIONDELAY + 1,
                        y=BASEY - y * SUBSTATIONDELAY
                    )
                )
            )

            if y != 0:
                wires.append(
                    [
                        entity_number, 5, entity_number - 1, 5
                    ]
                )

            entity_number += 1

    for x in range(width):
        connectionPorts.append(entity_number)
        signal_counter = 0
        flag = False

        for y in range(height):
            if not((x % 18 == 0 and y % 18 == 1) or (x % 18 == 1 and y % 18 == 1) or (x % 18 == 0 and y % 18 == 0) or (x % 18 == 1 and y % 18 == 0)):
                screen.append(
                    Entity(
                        entity_number=entity_number,
                        name="small-lamp",
                        position=Position(
                            x=BASEX + x,
                            y=BASEY - y
                        ),
                        control_behavior=LampBehavior(
                            circuit_condition=CircuitCondition(
                                first_signal=LampSignal(
                                    type=signal_name_type[signal_counter][1],
                                    name=signal_name_type[signal_counter][0]
                                )
                            ),
                            rgb_signal=LampSignal(
                                type=signal_name_type[signal_counter][1],
                                name=signal_name_type[signal_counter][0]
                            )
                        )
                    )
                )

                if y != 0:
                    wires.append(
                        [
                            entity_number, 2, entity_number-1, 2
                        ]
                    )

                if flag:
                    wires.append(
                        [
                            entity_number, 2, last_lamp, 2
                        ]
                    )
                    flag = False

                entity_number += 1
                
            
            else:
                flag = True
                last_lamp = entity_number

            signal_counter += 1


    return screen, connectionPorts, wires, entity_number, connection_substation