"""
This package contains a collection of classes for storing and manipulating story elements.

Here's a brief description of each:

- plot.py: This is the main class for storing the story plot; it is meant to be passable and acts as a wrapper for
all other story elements.

- suspect.py: Contains the Suspect class for storing suspect information (background,
guilty/innocent, etc.).

- timestamp.py: Contains the Timestamp class for storing the events that occurred during  a
single 15-minute interval in the story.

- timeline.py: Contains the Timeline class for storing the story timeline; holds a list of Timestamp objects.

- murder_details.py: Contains specifics about the committed murder.

- victim.py: Contains information about the departed victim.

- shared_interaction.py: For storing conversations/interactions shared by two suspects; helps to line up their memories

- pickle_plot.py: Provides functions for pickling/unpickling Plot objects (provides save functionality)
"""
