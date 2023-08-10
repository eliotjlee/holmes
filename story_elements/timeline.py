class Timeline:
    def __init__(self, start_time, time_of_murder, timestamps):
        self.start_time = start_time
        self.time_of_murder = time_of_murder
        self.timestamps = timestamps  # This is a list of Timestamp objects

    def get_times_list(self):
        times_list = []
        for timestamp in self.timestamps:
            times_list.append(timestamp.time)
        return times_list