def assemble_suspect_context(plot, suspect_number): #suspect number one less than id
    context_str = f"Case Summary: {plot.summary}\n"
    context_str += f"Victim: {plot.victim.name}\nBio: {plot.victim.bio}\n"
    context_str += f"Murder Details: {plot.murder_details.murder_description}\n"
    context_str += f"Murder Setting: {plot.murder_details.murder_setting}\n"
    context_str += f"Murder Weapon: {plot.murder_details.murder_weapon}\n"

    suspects = plot.suspects

    this_suspect = suspects[suspect_number]

    other_suspects = ""

    for sus in suspects:
        if sus != this_suspect:
            other_suspects += f"{sus.name}\n"
            other_suspects += f"Bio: {sus.bio}\n"
            other_suspects += f"Tags: {', '.join(sus.tags)}\n"
            other_suspects += f"Victim Connection: {sus.victim_connection}\n\n"

    context_str += f"\nThis is you: {this_suspect.name}\nBio: {this_suspect.bio}\n"
    context_str += f"Tags: {', '.join(this_suspect.tags)}\n"
    context_str += f"Victim Connection: {this_suspect.victim_connection}\n"
    if this_suspect.guilty:
        context_str += "You are guilty.\n"
        context_str += "Your responses MUST detail how you plotted and carried out the murder"
    else:
        context_str += "You are innocent.\n"

    context_str += "\nHere are the other suspects:\n"
    context_str += other_suspects
    
    return context_str