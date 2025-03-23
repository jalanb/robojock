import typer

from robojock import itunes

robojock = typer.Typer()
itunes = itunes.ITunes10()


@robojock.command()
def playing():
    """Show the current track"""
    print(itunes.current_track)


@robojock.command()
def pause():
    """Stop playing music"""
    itunes.pause()


@robojock.command()
def play():
    """Start playing music"""
    itunes.play()


@robojock.command()
def main():
    """robojock provides terminal control of a local iTunes Application"""
    playing()


if __name__ == "__main__":
    robojock()
