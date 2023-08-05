def assemble_suspect_context(plot, suspects, suspect_number):
    context_str = f"Case Summary: {plot.summary}\n"
    context_str += f"Victim: {plot.victim.name}\nBio: {plot.victim.bio}\n"
    context_str += f"Murder Details: {plot.murder_details.murder_description}\n"
    context_str += f"Murder Setting: {plot.murder_details.murder_setting}\n"
    context_str += f"Murder Weapon: {plot.murder_details.murder_weapon}\n"

    suspect = suspects.pop(suspect_number-1)

    other_suspects = ""

    for sus in suspects:
        other_suspects += sus.name
        other_suspects += f"Bio: {sus.bio}\n"
        other_suspects += f"Tags: {', '.join(sus.tags)}\n"
        other_suspects += f"Victim Connection: {sus.victim_connection}\n\n"

    context_str += f"\nThis is you: {suspect.name}\nBio: {suspect.bio}\n"
    context_str += f"Tags: {', '.join(suspect.tags)}\n"
    context_str += f"Victim Connection: {suspect.victim_connection}\n"
    if suspect.guilty:
        context_str += "You are guilty.\n"
    else:
        context_str += "You are innocent.\n"

    context_str += "\nHere are the other suspects:\n"
    context_str += other_suspects
    
    return context_str