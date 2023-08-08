write_timeline_func = [
    { 
        "name": "write_timeline",
        "description": "Write the timeline detailing the crime that will be used to generate each character's perspective. Each timestamp after the initial one represents a 15-minute increment.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_time": {
                    "type": "string",
                    "description": "The time at which the event began (HH:MM AM/PM)"
                },
                "time_of_murder": {
                    "type": "string",
                    "description": "The time at which the murder occured (HH:HH AM/PM) - MUST COINCIDE WITH ONE OF THE TIMESTAMPS BELOW."
                },
                "timestamp_1": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_2": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_3": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_4": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_5": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_6": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_7": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_8": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_9": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },
                "timestamp_10": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string",
                            "description": "This timestamp's time (HH:MM AM/PM)"
                        },
                        "suspect_1_action": {
                            "type": "string",
                            "description": "A description of what suspect 1 was doing at this timestamp."
                        },
                        "suspect_2_action": {
                            "type": "string",
                            "description": "A description of what suspect 2 was doing at this timestamp."
                        },
                        "suspect_3_action": {
                            "type": "string",
                            "description": "A description of what suspect 3 was doing at this timestamp."
                        },
                        "suspect_4_action": {
                            "type": "string",
                            "description": "A description of what suspect 4 was doing at this timestamp."
                        },
                    },
                    "required": ["time", "suspect_1", "suspect_2", "suspect_3", "suspect_4"]
                },

            },
            "required" : ["timestamp_1", "timestamp_2", "timestamp_3", "timestamp_4", "timestamp_5", "timestamp_6", "timestamp_7", "timestamp_8", "timestamp_9", "timestamp_10"]

        }

    }
]