import pickle


def save_plot(plot_obj, save_path):
    """
    Saves the Plot object to a pickle file.
    """
    filename = f"{save_path}/plot.pkl"
    with open(filename, 'wb') as file:
        pickle.dump(plot_obj, file)


def load_plot(save_path):
    """
    Loads the Plot object from a pickle file.
    """
    filename = f"{save_path}/plot.pkl"
    with open(filename, 'rb') as file:
        return pickle.load(file)

