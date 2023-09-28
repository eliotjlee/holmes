from story_elements.shared_interaction import SharedInteraction


def parse_shared_interactions(json_data, plot):
    """
    Parses the shared interactions from the given JSON data and stores them within the provided plot object.

    Parameters:
        json_data (dict): A dictionary containing the shared interactions data.
        plot (Plot): The Plot object where the shared interactions will be stored.

    Returns:
        None

    Raises:
        KeyError: If the required keys are not found in the JSON data.
    """

    # Iterates through shared interactions, parses + stores them
    for timestamp_key, timestamp_data in json_data.items():
        timestamp = timestamp_data['time']
        if 'suspect_interaction_pairs' in timestamp_data:
            if 'suspect_a' in timestamp_data['suspect_interaction_pairs']:

                interaction_pair = timestamp_data['suspect_interaction_pairs']
                suspect_a = interaction_pair['suspect_a']
                suspect_b = interaction_pair['suspect_b']
                interaction_id = interaction_pair['interaction_id']
                plot.add_shared_interaction(SharedInteraction(timestamp, suspect_a, suspect_b, interaction_id))
            else:
                plot.add_shared_interaction(SharedInteraction(timestamp, None, None, None))
