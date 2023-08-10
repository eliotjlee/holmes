shared_events_template = """
In the function shared_events(), we're going to initialize a timeline that includes shared events, interactions between suspects. This will serve as a framework for generating a consistent and intriguing mystery narrative. You're provided with a JSON object following a specific schema.

The schema includes a series of timestamps corresponding to 15-minute intervals in the event. For each timestamp, you might have:

1. A shared event: This is something significant that happens which most or all of the suspects are aware of or involved in. For example, a loud noise in the mansion, a power outage, or the discovery of the victim.

2. Interactions: These are direct interactions between pairs of suspects. Each interaction is associated with a unique identifier, which we will use to generate a conversation for this interaction and recall it when needed. For instance, Suspect A and Suspect B might have a heated argument, or Suspect C might pull Suspect D aside for a private chat.

Your task is to use this schema to outline a series of shared events and interactions that occur during the course of the event. This timeline will then be used as a foundation for generating each suspect's individual narrative.

NOTE: The interaction pairs must only list suspects outlined in the schema. NOT THE VICTIM.

PLOT SCHEMA:
{story_schema}

IMPORTANT: YOU MUST NOT INCLUDE ANY EVENTS INVOLVING A DETECTIVE; THE MURDER MUST REMAIN UNSOLVED.
IMPORTANT: ALL TIMESTAMPS MUST BE PRESENT IN YOUR RESPONSE, EVEN IF NO INTERACTION OCCURS AT THAT TIMESTAMP.
IMPORTANT: Your response must contain AT LEAST 3 interaction pairs.

(ALL TIMES MUST BE IN FORMAT HH:MM AM/PM)

Your answer must include: timestamp_1, timestamp_2, timestamp_3, timestamp_4, timestamp_5, timestamp_6, timestamp_7, timestamp_8, timestamp_9, timestamp_10

YOUR SHARED EVENTS SCHEMA:
"""


# NEED TO MAKE SURE 