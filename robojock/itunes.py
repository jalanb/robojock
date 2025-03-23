import appscript


class ITunes10:
    def __init__(self):
        self.app = appscript.app("itunes10")

    @property
    def current_track(self) -> str:
        try:
            track = self.app.current_track()
            return f"{track.artist()}/{track.album()}/{track.name()}"
        except appscript.reference.CommandError:
            return ""

    def play(self) -> None:
        self.app.play()

    def pause(self) -> None:
        self.app.pause()
