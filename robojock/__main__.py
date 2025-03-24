import typer
import json
from rich.console import Console

from robojock import itunes

robojock = typer.Typer()
itunes10 = itunes.ITunes10()
console = Console()


@robojock.command()
def playing():
    """Show the current track"""
    print(itunes10.current_track)


@robojock.command()
def track_info():
    """Show detailed information about the current track"""
    track = itunes10.get_current_track()
    if track:
        info = track.info()
        for key, value in info.items():
            console.print(f"[bold]{key}:[/bold] {value}")
    else:
        console.print("[yellow]No track is currently playing[/yellow]")


@robojock.command()
def pause():
    """Stop playing music"""
    itunes10.pause()


@robojock.command()
def play():
    """Start playing music"""
    itunes10.play()


@robojock.command()
def next():
    """Skip to the next track"""
    itunes10.next_track()


@robojock.command()
def previous():
    """Go back to the previous track"""
    itunes10.previous_track()


@robojock.command()
def playlists(limit: int = 0):
    """List available playlists

    Args:
        limit: Maximum number of playlists to show (0 for all)
    """
    all_playlists = itunes10.get_playlists(limit=limit)
    if all_playlists:
        for playlist in all_playlists:
            console.print(f"[bold]{playlist['name']}[/bold] ({playlist['track_count']} tracks)")
    else:
        console.print("[yellow]No playlists found[/yellow]")


@robojock.command()
def play_playlist(name: str):
    """Play a specific playlist by name"""
    success = itunes10.play_playlist(name)
    if success:
        console.print(f"[green]Now playing playlist: {name}[/green]")
    else:
        console.print(f"[red]Could not play playlist: {name}[/red]")


@robojock.command()
def volume(level: int = None):
    """Get or set the volume (0-100)"""
    if level is None:
        current = itunes10.get_volume()
        console.print(f"Current volume: {current}")
    else:
        if 0 <= level <= 100:
            itunes10.set_volume(level)
            console.print(f"Volume set to {level}")
        else:
            console.print("[red]Volume must be between 0 and 100[/red]")


def main():
    """robojock provides terminal control of a local iTunes Application"""
    playing()


if __name__ == "__main__":
    robojock()
