write_timeline_template = """As the Language Model, you are tasked with generating a full timeline based on the filled-out schema provided by the "shared_events()" function, as well as the plot schema. This timeline will detail the actions and experiences of each suspect during the event at 15-minute intervals. 

Your task is to take the shared events, interactions, red herrings, and distractions from the shared_events schema and the key plot points from the plot schema and integrate them into the timeline in a way that aligns with each suspect's characteristics and potential motives. Here's how to do it:

1. First, familiarize yourself with the plot schema. This will give you an understanding of the broader narrative arc and the key events that need to be included in the timeline.

2. Start with the first timestamp and examine the shared_events schema. Identify if there are any shared events, interactions, red herrings, or distractions tagged to this time.

3. For each suspect, consider their individual traits and possible motivations from the plot schema. Write a description of their actions or experiences at this timestamp, based on the events assigned in the shared_events schema. If there is a shared event, make sure that all suspects are involved in some way. If there is an interaction, ensure that the conversation between the suspects is marked.

4. If there are red herrings or distractions, weave these into the actions of one or more suspects as appropriate, in accordance with the plot schema.

5. If no special events are assigned to this timestamp, you can describe suspects performing routine actions or resting, depending on their character profiles.

6. Repeat this process for each subsequent timestamp, building a coherent narrative that unfolds over time and aligns with the broader plot outlined in the plot schema.

7. Ensure that all major events, especially the time of the murder, align with the details provided in both schemas.

Remember to keep the timeline consistent and make sure the actions described for each suspect at each timestamp make sense within the overall narrative and the broader plot points given in the plot schema.```

PLOT SCHEMA:
{story_schema}

SHARED EVENTS SCHEMA:
{shared_events}

IMPORTANT: YOUR PLOT MUST BEGIN AND END AT THE SAME TIME AS THE SHARED EVENTS SCHEMA. OTHERWISE EVERYONE DIES.

YOUR RESPONSE (MUST USE WRITE_TIMELINE() AND ALL PARAMETERS MUST BE PROVIDED):
"""