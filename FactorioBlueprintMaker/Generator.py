import json, base64, zlib

from .models import *

from .ScreenGenerator import createScreen
from .DataBlockCreation import madeDataBlock
from .CreateTicker import createTicker


class FactorioBlueprintGenerator():
    def __init__(self, gif: dict) -> None:
        framesCount = gif["count"]
        self.width = gif["width"]
        self.height = gif["height"]
        fps = gif["fps"]

        self.entity_number = 0

        frames = gif["frames"]

        self.blueprint = Blueprint(entities=[], wires=[])

        screen_connectors, first_screen_substation = self.addScreen()

        print(f"Screen created")

        data_connectors, for_ticker_connector, first_data_substation = self.addDataBlock(frames)

        print(f"Data block created")

        for i in range(len(screen_connectors)):
            self.blueprint.wires.append(
                [
                    screen_connectors[i], 2, data_connectors[i], 4
                ]
            )

        self.blueprint.wires.append(
            [
                first_screen_substation, 5, first_data_substation, 5
            ]
        )

        entities, wires, ticker_connector = createTicker(fps, framesCount, self.entity_number, self.width)

        print(f"Ticker created")

        self.blueprint.wires.append(
            [
                for_ticker_connector, 1, ticker_connector, 3
            ]
        )

        self.base = Base(blueprint=self.blueprint).model_dump()

        self.base["blueprint"]["entities"] += entities
        self.base["blueprint"]["wires"] += wires

        print(f"Just few seconds")


    def addDataBlock(self, frames) -> tuple:
        dataBlock, wires, self.entity_number, data_connector, self.entity_number, ticker_connector, first_data_substation = madeDataBlock(frames, self.width, self.height, self.entity_number)

        self.blueprint.entities += dataBlock
        self.blueprint.wires += wires

        return data_connector, ticker_connector, first_data_substation


    def addScreen(self) -> tuple:
        screen, screenConnection, screenWires, self.entity_number, first_screen_substation = createScreen(self.width, self.height, self.entity_number)
        self.blueprint.entities += screen
        self.blueprint.wires += screenWires

        return screenConnection, first_screen_substation


    def generate(self) -> str:
        blueprint = self.convertToBase64()

        return blueprint


    def convertToBase64(self) -> str:
        data = json.dumps(self.base)
        data = zlib.compress(data.encode())
        data = str(base64.b64encode(data), 'utf-8')

        return f"0{data}"