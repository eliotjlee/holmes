def assemble_suspect_context(plot, suspects, suspect_number):
    context_str = f"Case Summary: {plot.summary}\n"
    context_str += f"Victim: {plot.victim.name}\nBio: {plot.victim.bio}\n"
    context_str += f"Murder Details: {plot.murder_details.murder_description}\n"
    context_str += f"Murder Setting: {plot.murder_details.murder_setting}\n"
    context_str += f"Murder Weapon: {plot.murder_details.murder_weapon}\n"

    for i in range(len(suspects)):
        sus = suspects[i]
        if sus.id == suspect_number:
            index = i
            break
    
    if index is not None:
        this_suspect = suspects[index]

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
    else:
        context_str += "You are innocent.\n"

    context_str += "\nHere are the other suspects:\n"
    context_str += other_suspects
    
    return context_str