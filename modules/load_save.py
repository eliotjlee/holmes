import os


def get_latest_saves(base_path="saves"):
    """
    Retrieves the 10 most recent save directories from a specified base path,
    displays them to the user, and prompts the user to select one.
    Returns the path to the user-selected save directory.

    Parameters:
    base_path (str): The path to the directory containing the save folders.
                     Default is "saves".

    Returns:
    str: The path to the save directory selected by the user.

    Raises:
    ValueError: If the user input is not a valid number within the selection range.

    Example:
    >>> get_latest_saves()
    1. save_2023_09_25_15_30
    2. save_2023_09_25_14_15
    3. save_2023_09_25_13_00
    ...
    Pick the number corresponding to the save (1-10): 2
    'saves/save_2023_09_25_14_15'
    """

    # List all the folders in the saves directory
    all_saves = [dir_name for dir_name in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, dir_name))]

    # Sort the saves by timestamp
    sorted_saves = sorted(all_saves, reverse=True)

    # Retrieve the most recent saves (up to 10)
    latest_saves = sorted_saves[:10]
    num_latest_saves = len(latest_saves)

    # Display them to the user
    for i, save in enumerate(latest_saves, 1):
        print(f"{i}. {save}")

    # Prompt the user to make a choice
    while True:
        try:
            choice = int(input(f"Pick the number corresponding to the save (1-{num_latest_saves}): "))
            if 1 <= choice <= num_latest_saves:

                # Return the path to the chosen save
                return os.path.join(base_path, latest_saves[choice - 1])
            else:
                print(f"Invalid choice. Please choose a number between 1 and {num_latest_saves}.")
        except ValueError:
            print("Please enter a valid number.")


