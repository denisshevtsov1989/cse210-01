

class Director:
    def __init__(self):
        self._hiden_word = HidenWord()
        self._is_playing = True
        self._seeker = Seeker()
        self._terminal_service = TerminalService()

    def start_game(self):
