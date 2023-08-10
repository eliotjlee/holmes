write_timestamp_func = [{
    "name": "write_single_timestamp",
    "description": "Write the actions of each suspect for a single 15-minute timestamp.",
    "parameters": {
        "type": "object",
        "properties": {
            "time": {
                "type": "string",
                "description": "This timestamp's time (MUST BE IN FORMAT HH:MM AM/PM)"
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
        "required": ["time", "suspect_1_action", "suspect_2_action", "suspect_3_action", "suspect_4_action"]
    }
}
]