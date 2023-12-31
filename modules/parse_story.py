from story_elements.victim import Victim
from story_elements.murder_details import MurderDetails
from story_elements.plot import Plot
from story_elements.suspect import Suspect


def parse_story(story_dict):
    """
    Parses the given story schema dictionary and constructs a Plot object along with a list of Suspect objects.

    Parameters:
        story_dict (dict): A dictionary containing the story schema including plot, victim, murder details, and suspects.

    Returns:
        tuple: A tuple containing:
            - plot_obj (Plot): A Plot object containing the story's plot, victim, murder details, and suspects.
            - suspects (list): A list of Suspect objects representing the suspects in the story.
    """

    # Extracts plot, victim, murder details
    plot = story_dict.get("plot_details")
    victim = Victim(plot.get("victim").get("name"), plot.get("victim").get("bio"))
    murder_details = MurderDetails(plot.get("murder_details").get("murder_description"),
                                   plot.get("murder_details").get("murder_setting"),
                                   plot.get("murder_details").get("murder_weapon"),
                                   plot.get("murder_details").get("murder_action"))

    # Extracts suspects
    suspects = []
    for i in range(1, 5):
        suspect = story_dict.get(f"suspect_{i}")
        tags = [suspect.get(f"tag_{j}") for j in range(1, 6)]
        suspects.append(Suspect(suspect.get("name"), suspect.get("bio"), tags, suspect.get("victim_connection"),
                                suspect.get("guilty"), i))

    # Construct the Plot object
    plot_obj = Plot(plot.get("summary"), victim, murder_details, suspects)

    return plot_obj, suspects
