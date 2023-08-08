from story_elements.shared_interaction import SharedInteraction

def parse_shared_interactions(json_data):
    shared_interactions = []

    for timestamp_key, timestamp_data in json_data.items():
        timestamp = timestamp_data['time']
        interaction_pairs = timestamp_data['interaction_pairs']

        for interaction_pair in interaction_pairs:
            suspect_a = interaction_pair['suspect_a']
            suspect_b = interaction_pair['suspect_b']
            interaction_id = interaction_pair['interaction_id']
            shared_interactions.append(SharedInteraction(timestamp, suspect_a, suspect_b, interaction_id))

    return shared_interactions