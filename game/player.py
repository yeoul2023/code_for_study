class Player:
    def __init__(self, name):
        self.name = name
        self.play_time = None

    def set_play_time(self, play_time):
        self.play_time = play_time