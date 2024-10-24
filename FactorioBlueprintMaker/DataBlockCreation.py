import json

from .models import *


BASEX = 0
BASEY = 2
SUBSTATIONDELAY = 18


with open("signals.json") as f:
    signals = json.load(f)

signal_name_type = tuple(signals.items())


def madeRow(frame: list, frame_count: int, width: int, height: int, entity_number: int, y: int) -> tuple:
    entity_number += 1
    row = []
    wires = []
    con = []

    for x in range(width):
        row.append(
            Entity(
                entity_number=entity_number,
                name="decider-combinator",
                position=Position(x=BASEX + x, y=BASEY + y),
                control_behavior=DeciderBehavior(
                    decider_conditions=DeciderConditions(
                        conditions=[Condition(constant=frame_count)],
                        outputs=[Outputs()]
                    )
                )
            )
        )

        con.append(entity_number)

        entity_number += 1

        row.append(
            Entity(
                entity_number=entity_number,
                name="constant-combinator",
                position=Position(x=BASEX + x, y=BASEY + y + 1),
                control_behavior=ConstantBehavior(
                    sections=Sections(
                        sections=[Section(
                            filters=[Filter(
                                index=i + 1,
                                type=signal_name_type[i][1],
                                name=signal_name_type[i][0],

                                count=frame[height*(x + 1) - i - 1]
                            ) for i in range(height)]
                        )]
                    )
            )
        )
        )

        if x != 0:
            wires.append(
                [
                    entity_number - 1, 1, entity_number - 3, 1
                ]
            )

        wires.append(
            [
                entity_number, 2, entity_number - 1, 2
            ]
        )

        entity_number += 1

    print(f"Frame {frame_count} created")

    return row, wires, entity_number, con


def madeDataBlock(frames: list, width: int, height: int, entity_number: int) -> tuple:
    entity_number += 1

    block = []
    wires = []
    connectors = []

    count = len(frames)
    yDelay = 3

    last_substation = None
    first_substation = None
    first_electric_pole = None

    for y in range(count // 5 + 1):
        for x in range(width // SUBSTATIONDELAY + int((width - (width // SUBSTATIONDELAY) * SUBSTATIONDELAY) // (SUBSTATIONDELAY / 2)) + 1):
            block.append(
                Entity(
                    entity_number=entity_number,
                    name="substation",
                    position=Position(
                        x=BASEX + x * SUBSTATIONDELAY + 1,
                        y=BASEY + y * SUBSTATIONDELAY + yDelay + 3
                    )
            )
            )

            if x != 0:
                wires.append(
                    [
                        entity_number, 5, entity_number - 1, 5
                    ]
                )

            entity_number += 1

        if last_substation is not None:
            wires.append(
                [
                    last_substation, 5, entity_number - 1, 5
                ]
            )

            if first_substation is None:
                first_substation = last_substation

        last_substation = entity_number - 1


    for i in range(count):
        block_row, block_wires, entity_number, con = madeRow(frames[i], i+1, width, height, entity_number, yDelay)
        block += block_row
        wires += block_wires
        connectors.append(con)

        block.append(
            Entity(
                entity_number=entity_number,
                name="medium-electric-pole",
                position=Position(x=BASEX + width + 2, y=BASEY + yDelay)
        )
        )

        if i != 0:
            wires.append(
                [
                    entity_number, 1, last_electic_pole, 1
                ]
            )

        wires.append(
            [
                entity_number, 1, con[width - 1], 1
            ]
        )

        last_electic_pole = entity_number
        if first_electric_pole is None: first_electric_pole = entity_number
        entity_number += 1

        if i == 0:
            screen_connector = con

        yDelay += 3

        if i % 5 == 0:
            yDelay += 3

    for i in range(1, len(connectors)):
        for j in range(len(connectors[i])):
            wires.append(
                [
                    connectors[i-1][j], 4, connectors[i][j], 4
                ]
            )
        

    return block, wires, entity_number, screen_connector, entity_number, first_electric_pole, first_substation