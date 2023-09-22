from story_elements.shared_interaction import SharedInteraction


def parse_shared_interactions(json_data, plot):
    shared_interactions = []

    for timestamp_key, timestamp_data in json_data.items():
        timestamp = timestamp_data['time']
        if 'suspect_interaction_pairs' in timestamp_data:
            if 'suspect_a' in timestamp_data['suspect_interaction_pairs']:

                interaction_pair = timestamp_data['suspect_interaction_pairs']
                suspect_a = interaction_pair['suspect_a']
                suspect_b = interaction_pair['suspect_b']
                interaction_id = interaction_pair['interaction_id']
                shared_interactions.append(SharedInteraction(timestamp, suspect_a, suspect_b, interaction_id))
                plot.add_shared_interaction(SharedInteraction(timestamp, suspect_a, suspect_b, interaction_id))
            else:
                shared_interactions.append(SharedInteraction(timestamp, None, None, None))
                plot.add_shared_interaction(SharedInteraction(timestamp, None, None, None))

    return shared_interactions
