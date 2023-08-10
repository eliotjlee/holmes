import pickle
from story_elements.plot import Plot
from story_elements.murder_details import MurderDetails
from story_elements.victim import Victim
from story_elements.suspect import Suspect
from story_elements.shared_interaction import SharedInteraction
from story_elements.timestamp import Timestamp

def save_plot(plot_obj, save_path):
    filename = f"{save_path}/plot.pkl"
    with open(filename, 'wb') as file:
        pickle.dump(plot_obj, file)

def load_plot(save_path):
    filename = f"{save_path}/plot.pkl"
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Example usage:
# plot_obj = Plot(...)
# save_plot(plot_obj, 'plot.pkl')
# loaded_plot = load_plot('plot.pkl')
