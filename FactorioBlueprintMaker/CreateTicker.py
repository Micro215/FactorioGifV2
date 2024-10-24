import math


def createTicker(fps: int, frame_count: int, entity_number: int, width: int) -> tuple:
    delay = math.ceil(math.ceil(60 / fps) / 2)

    entities = [
            {
                "entity_number": entity_number + 1,
                "name": "constant-combinator",
                "position": {
                    "x": -126.5 + width + 131 + 4,
                    "y": -374.5 + 377
                },
                "direction": 8,
                "control_behavior": {
                    "sections": {
                        "sections": [
                            {
                                "index": 1,
                                "filters": [
                                    {
                                        "index": 1,
                                        "type": "virtual",
                                        "name": "signal-S",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 2,
                                        "type": "virtual",
                                        "name": "signal-T",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 3,
                                        "type": "virtual",
                                        "name": "signal-A",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 4,
                                        "type": "virtual",
                                        "name": "signal-R",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 5,
                                        "type": "virtual",
                                        "name": "signal-green",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    }
                                ]
                            }
                        ]
                    },
                    "is_on": False
                }
            },
            {
                "entity_number": entity_number + 2,
                "name": "display-panel",
                "position": {
                    "x": -126.5 + width + 131 + 4,
                    "y": -375.5 + 377
                },
                "text": "start",
                "icon": {
                    "type": "virtual",
                    "name": "signal-green"
                }
            },
            {
                "entity_number": entity_number + 3,
                "name": "constant-combinator",
                "position": {
                    "x": -125.5 + width + 131 + 4,
                    "y": -374.5 + 377
                },
                "direction": 8,
                "control_behavior": {
                    "sections": {
                        "sections": [
                            {
                                "index": 1,
                                "filters": [
                                    {
                                        "index": 1,
                                        "type": "virtual",
                                        "name": "signal-S",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 2,
                                        "type": "virtual",
                                        "name": "signal-T",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 3,
                                        "type": "virtual",
                                        "name": "signal-O",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 4,
                                        "type": "virtual",
                                        "name": "signal-P",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    },
                                    {
                                        "index": 5,
                                        "type": "virtual",
                                        "name": "signal-red",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    }
                                ]
                            }
                        ]
                    },
                    "is_on": False
                }
            },
            {
                "entity_number": entity_number + 4,
                "name": "display-panel",
                "position": {
                    "x": -125.5 + width + 131 + 4,
                    "y": -375.5 + 377
                },
                "text": "stop",
                "icon": {
                    "type": "virtual",
                    "name": "signal-red"
                }
            },
            {
                "entity_number": entity_number + 5,
                "name": "decider-combinator",
                "position": {
                    "x": -127.5 + width + 131 + 3,
                    "y": -373 + 377 - 2
                },
                "direction": 8,
                "control_behavior": {
                    "decider_conditions": {
                        "conditions": [
                            {
                                "first_signal": {
                                    "type": "virtual",
                                    "name": "signal-dot"
                                },
                                "constant": 3,
                                "comparator": "\u2264"
                            }
                        ],
                        "outputs": [
                            {
                                "signal": {
                                    "type": "virtual",
                                    "name": "signal-dot"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "entity_number": entity_number + 15,
                "name": "decider-combinator",
                "position": {
                    "x": -127.5 + width + 131 + 1,
                    "y": -373 + 377 - 2
                },
                "direction": 8,
                "control_behavior": {
                    "decider_conditions": {
                        "conditions": [
                            {
                                "first_signal": {
                                    "type": "virtual",
                                    "name": "signal-green"
                                },
                                "constant": 0,
                                "comparator": "="
                            }
                        ],
                        "outputs": [
                            {
                                "signal": {
                                    "type": "virtual",
                                    "name": "signal-dot"
                                },
                                "copy_count_from_input": False
                            }
                        ]
                    }
                }
            },
            {
                "entity_number": entity_number + 6,
                "name": "decider-combinator",
                "position": {
                    "x": -126.5 + width + 131 + 3,
                    "y": -373 + 377 - 2
                },
                "direction": 8,
                "control_behavior": {
                    "decider_conditions": {
                        "conditions": [
                            {
                                "first_signal": {
                                    "type": "virtual",
                                    "name": "signal-green"
                                },
                                "second_signal": {
                                    "type": "virtual",
                                    "name": "signal-red"
                                },
                                "comparator": ">"
                            }
                        ],
                        "outputs": [
                            {
                                "signal": {
                                    "type": "virtual",
                                    "name": "signal-green"
                                },
                                "copy_count_from_input": False
                            }
                        ]
                    }
                }
            },
            {
                "entity_number": entity_number + 7,
                "name": "arithmetic-combinator",
                "position": {
                    "x": -130.5 + width + 131 + 3,
                    "y": -371 + 377 - 2
                },
                "control_behavior": {
                    "arithmetic_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        },
                        "second_constant": 1,
                        "operation": "+",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        }
                    }
                }
            },
            {
                "entity_number": entity_number + 8,  # for fps
                "name": "arithmetic-combinator",
                "position": {
                    "x": -129.5 + width + 131 + 3,
                    "y": -371 + 377 - 2
                },
                "control_behavior": {
                    "arithmetic_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-each"
                        },
                        "second_constant": 1 * delay,
                        "operation": "/",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        }
                    }
                }
            },
            {
                "entity_number": entity_number + 9,
                "name": "arithmetic-combinator",
                "position": {
                    "x": -127.5 + width + 131 + 3,
                    "y": -371 + 377 - 2
                },
                "direction": 8,
                "control_behavior": {
                    "arithmetic_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-each"
                        },
                        "second_constant": 3,
                        "operation": "/",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-each"
                        }
                    }
                }
            },
            {
                "entity_number": entity_number + 10,
                "name": "decider-combinator",
                "position": {
                    "x": -126.5 + width + 131 + 3,
                    "y": -371 + 377 - 2
                },
                "direction": 8,
                "control_behavior": {
                    "decider_conditions": {
                        "conditions": [
                            {
                                "first_signal": {
                                    "type": "virtual",
                                    "name": "signal-green"
                                },
                                "constant": 1
                            }
                        ],
                        "outputs": [
                            {
                                "signal": {
                                    "type": "virtual",
                                    "name": "signal-everything"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "entity_number": entity_number + 11,  # for fps
                "name": "arithmetic-combinator",  
                "position": {
                    "x": -129.5 + width + 131 + 3,
                    "y": -369 + 377 - 2
                },
                "control_behavior": {
                    "arithmetic_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-each"
                        },
                        "second_constant": frame_count * delay,
                        "operation": "%",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        }
                    }
                }
            },
            {
                "entity_number": entity_number + 12,
                "name": "decider-combinator",
                "position": {
                    "x": -127.5 + width + 131 + 3,
                    "y": -369 + 377 - 2
                },
                "direction": 8,
                "control_behavior": {
                    "decider_conditions": {
                        "conditions": [
                            {
                                "first_signal": {
                                    "type": "virtual",
                                    "name": "signal-anything"
                                },
                                "comparator": ">"
                            }
                        ],
                        "outputs": [
                            {
                                "signal": {
                                    "type": "virtual",
                                    "name": "signal-anything"
                                }
                            }
                        ]
                    }
                }
            },
            {
                "entity_number": entity_number + 13,
                "name": "arithmetic-combinator",
                "position": {
                    "x": -126.5 + width + 131 + 3,
                    "y": -369 + 377 - 2
                },
                "control_behavior": {
                    "arithmetic_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        },
                        "second_constant": -1,
                        "operation": "*",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        }
                    }
                }
            },
            {
                "entity_number": entity_number + 16,
                "name": "arithmetic-combinator",
                "position": {
                    "x": -127.5 + width + 131,
                    "y": -373 + 377 - 2
                },
                "control_behavior": {
                    "arithmetic_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        },
                        "second_constant": -10,
                        "operation": "*",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-dot"
                        }
                    }
                }
            },
            {
                "entity_number": entity_number + 14,
                "name": "constant-combinator",
                "position": {
                    "x": -125.5 + width + 131 + 3,
                    "y": -368.5 + 377 - 2
                },
                "control_behavior": {
                    "sections": {
                        "sections": [
                            {
                                "index": 1,
                                "filters": [
                                    {
                                        "index": 1,
                                        "type": "virtual",
                                        "name": "signal-dot",
                                        "quality": "normal",
                                        "comparator": "=",
                                        "count": 1
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        ]

    wires = [
            [
                entity_number + 1,
                1,
                entity_number + 3,
                1
            ],
            [
                entity_number + 1,
                1,
                entity_number + 6,
                1
            ],
            [
                entity_number + 5,
                2,
                entity_number + 5,
                4
            ],
            [
                entity_number + 5,
                2,
                entity_number + 14,
                2
            ],
            [
                entity_number + 5,
                4,
                entity_number + 9,
                2
            ],
            [
                entity_number + 6,
                2,
                entity_number + 6,
                4
            ],
            [
                entity_number + 6,
                3,
                entity_number + 10,
                1
            ],
            [
                entity_number + 7,
                1,
                entity_number + 8,
                3
            ],
            [
                entity_number + 8,
                2,
                entity_number + 11,
                4
            ],
            [
                entity_number + 9,
                4,
                entity_number + 12,
                2
            ],
            [
                entity_number + 10,
                2,
                entity_number + 13,
                4
            ],
            [
                entity_number + 10,
                4,
                entity_number + 12,
                2
            ],
            [
                entity_number + 11,
                2,
                entity_number + 12,
                4
            ],
            [
                entity_number + 12,
                2,
                entity_number + 12,
                4
            ],
            [
                entity_number + 12,
                3,
                entity_number + 13,
                1
            ],
            [
                entity_number + 6,
                4,
                entity_number + 15,
                2
            ],
            [
                entity_number + 15,
                4,
                entity_number + 16,
                2
            ],
            [
                entity_number + 16,
                3,
                entity_number + 7,
                1
            ]
        ]

    return entities, wires, entity_number + 7