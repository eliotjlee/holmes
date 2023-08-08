shared_events_template = """
In the function shared_events(), we're going to initialize a timeline that includes shared events, interactions between suspects, red herrings, and distractions. This will serve as a framework for generating a consistent and intriguing mystery narrative. You're provided with a JSON object following a specific schema.

The schema includes a series of timestamps corresponding to 15-minute intervals in the event. For each timestamp, you might have:

1. A shared event: This is something significant that happens which most or all of the suspects are aware of or involved in. For example, a loud noise in the mansion, a power outage, or the discovery of the victim.

2. Interactions: These are direct interactions between pairs of suspects. Each interaction is associated with a unique identifier, which we will use to generate a conversation for this interaction and recall it when needed. For instance, Suspect A and Suspect B might have a heated argument, or Suspect C might pull Suspect D aside for a private chat.

3. Red herrings: A red herring is a piece of misleading information or a false clue meant to divert attention away from the actual culprit or solution. This could be something like a misplaced weapon, a suspicious but ultimately innocent behavior, or even a deliberate lie from one of the suspects.

4. Distractions: These are unrelated events or subplots that add depth to the narrative. While they may not contribute directly to the solution of the mystery, they serve to enrich the world and add complexity to the characters' experiences. This could be a personal issue a suspect is dealing with, a secondary conflict between characters, or a minor incident like a lost item or a misunderstanding.

Your task is to use this schema to outline a series of shared events, interactions, red herrings, and distractions that occur during the course of the event. This timeline will then be used as a foundation for generating each suspect's individual narrative.

NOTE: The interaction pairs must only list suspects outlined in the schema. Though suspects can and SHOULD interact with the victim, the victim should NOT be listed as a suspect in the interaction pairs.

PLOT SCHEMA:
{story_schema}

YOUR SHARED EVENTS SCHEMA:
"""


# NEED TO MAKE SURE 