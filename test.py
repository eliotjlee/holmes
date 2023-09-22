from story_elements.pickle_plot import load_plot
from suspect_agents.run_game import build_and_run_agents

def main():
    plot = load_plot("saves/2023-08-10_18-26-30")
    build_and_run_agents(plot)

main()