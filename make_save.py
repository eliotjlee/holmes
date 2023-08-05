import os
import datetime

def make_save():
    # Get full path to project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Create "saves" directory if it doesn't exist
    saves_dir = os.path.join(project_dir, "saves")
    if not os.path.exists(saves_dir):
        os.mkdir(saves_dir)

    # Generate timestamped folder name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = os.path.join(saves_dir, timestamp)

    # Create new folder with timestamped name
    os.mkdir(folder_name)

    # Save timestamped folder path as variable
    timestamped_folder_path = folder_name

    return timestamped_folder_path