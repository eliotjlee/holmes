# break up the story even more to create a more formulaic structure -> make it specify murder weapon, victim background, event background, each of the suspect's relations to the vicitm
set_up_story_func = [
    {
        "name": "set_up_story",
        "description": "Set up the game's story by providing a plot summary and descriptions for the four suspects.",
        "parameters": {
            "type": "object",
            "properties": {
                "plot_details": {
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": "string",
                            "description": "Description of the crime's setting and the event all suspects + the victim were in attendance at. What brought them together? What was the locale?"
                        },
                        "victim": {
                            "type": "object",
                            "properties": {
                                "name" : {
                                    "type": "string",
                                    "description": "Full name of the victim."
                                },
                                "bio": {
                                    "type": "string",
                                    "description": "A description of the victim's personality and background."
                                }
                            },
                            "required": ["name", "bio"]
                        },
                        "murder_details": {
                            "type": "object",
                            "properties": {
                                "murder_description": {
                                    "type": "string",
                                    "description": "Brief description of how the murder occurred."
                                },
                                "murder_setting": {
                                    "type": "string",
                                    "description": "Where at the event did the murder take place?"
                                },
                                # "murder_timestamp_MM:HH": {
                                #     "type": "string",
                                #     "description": "The timestamp at which the murder occurred. MUST USE THIS FORMAT: HH:MM [use military time]. MUST BE AN INCREMENT OF 15 MINUTES."
                                # },
                                "murder_weapon": {
                                    "type": "string",
                                    "description": "Name of the object used to carry out the murder."
                                },
                            },
                            "required": ["murder_description", "murder_setting", "murder_time", "murder_weapon"]
                        }
                    },
                    "required": ["setting", "victim", "murder_details"]
                },
                "suspect_1": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Full name of suspect #1."
                        },
                        "bio": {
                            "type": "string",
                            "description": "A description of suspect #1's personality, background, and motives."
                        },
                        "tag_1": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (1/5)"
                        },
                        "tag_2": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (2/5)"
                        },
                        "tag_3": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (3/5)"
                        },
                        "tag_4": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (4/5)"
                        },
                        "tag_5": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (5/5)"
                        },
                        "victim_connection": {
                            "type": "string",
                            "description": "A description of suspect #1's connection to the victim. How do they know each other?"
                        },
                        "guilty": {
                            "type": "boolean",
                            "description": "Whether or not suspect #1 is guilty."
                        },
                    },
                    "required": ["name", "bio", "tag_1", "tag_2", "tag_3", "tag_4", "tag_5", "victim_connection", "guilty"]
                },
                "suspect_2": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Full name of suspect #2."
                        },
                        "bio": {
                            "type": "string",
                            "description": "A description of suspect #2's personality, background, and motives."
                        },
                        "tag_1": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (1/5)"
                        },
                        "tag_2": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (2/5)"
                        },
                        "tag_3": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (3/5)"
                        },
                        "tag_4": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (4/5)"
                        },
                        "tag_5": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (5/5)"
                        },
                        "victim_connection": {
                            "type": "string",
                            "description": "A description of suspect #2's connection to the victim. How do they know each other?"
                        },
                        "guilty": {
                            "type": "boolean",
                            "description": "Whether or not suspect #2 is guilty."
                        },
                    },
                    "required": ["name", "bio", "tag_1", "tag_2", "tag_3", "tag_4", "tag_5", "victim_connection", "guilty"]
                },
                "suspect_3": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Full name of suspect #3."
                        },
                        "bio": {
                            "type": "string",
                            "description": "A description of suspect #3's personality, background, and motives."
                        },
                        "tag_1": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (1/5)"
                        },
                        "tag_2": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (2/5)"
                        },
                        "tag_3": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (3/5)"
                        },
                        "tag_4": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (4/5)"
                        },
                        "tag_5": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (5/5)"
                        },
                        "victim_connection": {
                            "type": "string",
                            "description": "A description of suspect #3's connection to the victim. How do they know each other?"
                        },
                        "guilty": {
                            "type": "boolean",
                            "description": "Whether or not suspect #3 is guilty."
                        },
                    },
                    "required": ["name", "bio", "tag_1", "tag_2", "tag_3", "tag_4", "tag_5", "victim_connection", "guilty"]
                },
                "suspect_4": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Full name of suspect #4."
                        },
                        "bio": {
                            "type": "string",
                            "description": "A description of suspect #4's personality, background, and motives."
                        },
                        "tag_1": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (1/5)"
                        },
                        "tag_2": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (2/5)"
                        },
                        "tag_3": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (3/5)"
                        },
                        "tag_4": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (4/5)"
                        },
                        "tag_5": {
                            "type": "string",
                            "details": "One to two-word trait describing this character. (5/5)"
                        },
                        "victim_connection": {
                            "type": "string",
                            "description": "A description of suspect #4's connection to the victim. How do they know each other?"
                        },
                        "guilty": {
                            "type": "boolean",
                            "description": "Whether or not suspect #4 is guilty."
                        },
                    },
                    "required": ["name", "bio", "tag_1", "tag_2", "tag_3", "tag_4", "tag_5", "victim_connection", "guilty"]
                },
            },
            "required": ["plot_details", "suspect_1", "suspect_2", "suspect_3", "suspect_4"],
        }
    }
]