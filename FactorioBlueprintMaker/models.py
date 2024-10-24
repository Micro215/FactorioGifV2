from pydantic import BaseModel
from typing import Optional


class LampSignal(BaseModel):
    type: str
    name: str

class CircuitCondition(BaseModel):
    first_signal: LampSignal
    constant: int = -1
    comparator: str = ">"

class LampBehavior(BaseModel):
    circuit_enabled: bool = True
    circuit_condition: CircuitCondition
    use_colors: bool = True
    rgb_signal: LampSignal
    color_mode: int = 2

class Condition(BaseModel):
    first_signal: dict = {"type": "virtual", "name": "signal-dot"}
    constant: int
    comparator: str = "="

class Outputs(BaseModel):
    signal: dict = {"type": "virtual", "name": "signal-everything"}

class DeciderConditions(BaseModel):
    conditions: list[Condition]
    outputs: list[Outputs]

class DeciderBehavior(BaseModel):
    decider_conditions: DeciderConditions

class Filter(BaseModel):
    index: int
    type: str
    name: str
    quality: str = "normal"
    comparator: str = "="
    count: int

class Section(BaseModel):
    index: int = 1
    filters: list[Filter]

class Sections(BaseModel):
    sections: list[Section]

class ConstantBehavior(BaseModel):
    sections: Sections

class Position(BaseModel):
    x: int
    y: int

class Entity(BaseModel):
    entity_number: int
    name: str
    position: Position
    control_behavior: ConstantBehavior | DeciderBehavior | LampBehavior | None = None

class Blueprint(BaseModel):
    icons: list = [{"signal": {"name": "substation"}, "index": 1}]
    entities: list[Entity]
    wires: list[list[int]] | None = None
    # wires
    # 0: from id
    # 1: from channel
    # 2: to id
    # 3: to channel

    item: str = "blueprint"
    version: int = 562949953945601


class Base(BaseModel):
    blueprint: Blueprint