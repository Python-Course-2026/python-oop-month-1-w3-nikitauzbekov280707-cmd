class Playlist:
    """ЗАДАЧА: Подсчет общей длительности песен (track_list - список секунд)"""
    def __init__(self): self.tracks = []
    def get_duration(self):
        if len(self.tracks)==0:
            return 0
        else:
            return sum([i for i in self.tracks])