import appscript
from typing import List, Dict, Any, Optional


class Track:
    """Represent an iTunes track."""
    
    def __init__(self, appscript_track):
        self.track = appscript_track
    
    def __str__(self) -> str:
        """String representation of track: artist/album/name."""
        return f"{self.track.artist()}/{self.track.album()}/{self.track.name()}"
    
    def info(self) -> Dict[str, Any]:
        """Return all available track information as a dictionary."""
        return {
            "name": self.track.name(),
            "artist": self.track.artist(),
            "album": self.track.album(),
            "genre": self.track.genre(),
            "rating": self.track.rating(),
            "year": self.track.year(),
            "bpm": self.track.bpm(),
            "comment": self.track.comment(),
            "compilation": self.track.compilation(),
            "composer": self.track.composer(),
            "disc_number": self.track.disc_number(),
            "duration": self.track.duration(),
            "played_count": self.track.played_count(),
            "played_date": self.track.played_date(),
            "track_number": self.track.track_number(),
        }


class ITunes10:
    def __init__(self):
        self.app = appscript.app("itunes10")

    @property
    def current_track(self) -> str:
        """Return a string representation of the current track."""
        try:
            track = self.app.current_track()
            return f"{track.artist()}/{track.album()}/{track.name()}"
        except appscript.reference.CommandError:
            return ""
    
    def get_current_track(self) -> Optional[Track]:
        """Get the current track as a Track object."""
        try:
            return Track(self.app.current_track())
        except appscript.reference.CommandError:
            return None

    def play(self) -> None:
        """Start playing music."""
        self.app.play()

    def pause(self) -> None:
        """Pause the current track."""
        self.app.pause()
    
    def next_track(self) -> None:
        """Skip to the next track."""
        self.app.next_track()
    
    def previous_track(self) -> None:
        """Go back to the previous track."""
        self.app.previous_track()
    
    def get_playlists(self, limit: int = 0) -> List[Dict[str, Any]]:
        """Get information about playlists.
        
        Args:
            limit: Maximum number of playlists to return (0 for all)
        """
        playlists = []
        try:
            all_playlists = self.app.playlists()
            # Apply limit if specified
            if limit > 0:
                all_playlists = all_playlists[:limit]
                
            for playlist in all_playlists:
                playlists.append({
                    "name": playlist.name(),
                    "track_count": len(playlist.tracks()) if hasattr(playlist, "tracks") else 0,
                })
            return playlists
        except appscript.reference.CommandError:
            return []
    
    def play_playlist(self, playlist_name: str) -> bool:
        """Play a specific playlist by name."""
        try:
            playlists = self.app.playlists[playlist_name]
            if playlists.exists():
                playlists.play()
                return True
            return False
        except appscript.reference.CommandError:
            return False
    
    def set_volume(self, volume: int) -> None:
        """Set the volume (0-100)."""
        if 0 <= volume <= 100:
            self.app.sound_volume.set(volume)
    
    def get_volume(self) -> int:
        """Get the current volume level."""
        try:
            return self.app.sound_volume.get()
        except appscript.reference.CommandError:
            return 0
            
    def is_playing(self) -> bool:
        """Check if iTunes is currently playing."""
        try:
            return self.app.player_state() == appscript.k.playing
        except appscript.reference.CommandError:
            return False