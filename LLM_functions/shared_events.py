shared_events_func = [
    {
        "name": "shared_events",
        "description": "Details shared events, red herrings, and distractions that occur during the timeline. Each timestamp coincides with the main timeline's intervals.",
        "parameters": {
            "type": "object",
            "properties": {
                "timestamp_1": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_2": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_3": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_4": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_5": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_6": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_7": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_8": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_9": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                },

                "timestamp_10": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "shared_event": {
                            "type": "string",
                            "description": "Description of the shared event occurring at this timestamp."
                        },
                        "interaction_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "suspect_a": {
                                        "type": "string",
                                        "description": "First suspect in the interaction."
                                    },
                                    "suspect_b": {
                                        "type": "string",
                                        "description": "Second suspect in the interaction."
                                    },
                                    "interaction_id": {
                                        "type": "string",
                                        "description": "A unique, descriptive identifier for this interaction, to be used for generating and recalling the conversation."
                                    }
                                },
                                "required": ["suspect_a", "suspect_b", "interaction_id"]
                            },
                            "description": "Pairs of suspects who have interactions at this timestamp."
                        },
                        "red_herring": {
                            "type": "string",
                            "description": "Description of the misleading event or clue at this timestamp."
                        },
                        "distraction": {
                            "type": "string",
                            "description": "Description of an unrelated event or subplot that adds depth to the narrative."
                        }
                    },
                    "required": ["time"]
                }
            }
        }
    }
]
