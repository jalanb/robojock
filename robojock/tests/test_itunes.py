"""
Tests for the iTunes interface.
"""
import pytest
from unittest.mock import MagicMock, patch

from robojock.itunes import ITunes10, Track


class TestTrack:
    """Tests for the Track class."""
    
    def test_init(self, mock_track):
        """Test Track initialization."""
        track = Track(mock_track)
        assert track.track == mock_track
    
    def test_str(self, mock_track):
        """Test string representation."""
        track = Track(mock_track)
        assert str(track) == "Test Artist/Test Album/Test Track"
    
    def test_info(self, mock_track):
        """Test info method returns all track properties."""
        track = Track(mock_track)
        info = track.info()
        
        assert info["name"] == "Test Track"
        assert info["artist"] == "Test Artist"
        assert info["album"] == "Test Album"
        assert info["genre"] == "Red"
        assert info["rating"] == 100
        assert info["year"] == 2024
        assert info["bpm"] == 120
        assert info["comment"] == "Test comment"
        assert info["compilation"] is False
        assert info["composer"] == "Test Composer"
        assert info["disc_number"] == 1
        assert info["duration"] == 180.5
        assert info["played_count"] == 42
        assert info["played_date"] == "2024-01-01 12:00:00"
        assert info["track_number"] == 5


class TestITunes10:
    """Tests for the ITunes10 class."""
    
    def test_init(self, mock_appscript):
        """Test initialization connects to iTunes."""
        mock_app, _, _ = mock_appscript
        
        itunes = ITunes10()
        
        mock_app.assert_called_once_with("itunes10")
    
    def test_current_track_property(self, mock_appscript):
        """Test current_track property returns string representation."""
        _, mock_instance, _ = mock_appscript
        
        # Set up the mock
        mock_track = MagicMock()
        mock_track.artist.return_value = "Test Artist"
        mock_track.album.return_value = "Test Album"
        mock_track.name.return_value = "Test Track"
        mock_instance.current_track.return_value = mock_track
        
        itunes = ITunes10()
        result = itunes.current_track
        
        assert result == "Test Artist/Test Album/Test Track"
    
    def test_current_track_property_error(self, mock_appscript):
        """Test current_track property handles errors."""
        _, mock_instance, _ = mock_appscript
        
        # Set up the mock to raise an exception
        import appscript
        mock_instance.current_track.side_effect = appscript.reference.CommandError
        
        itunes = ITunes10()
        result = itunes.current_track
        
        assert result == ""
    
    def test_get_current_track(self, mock_appscript):
        """Test get_current_track returns Track object."""
        _, mock_instance, _ = mock_appscript
        
        # Set up the mock
        mock_track = MagicMock()
        mock_instance.current_track.return_value = mock_track
        
        itunes = ITunes10()
        result = itunes.get_current_track()
        
        assert isinstance(result, Track)
        assert result.track == mock_track
    
    def test_get_current_track_error(self, mock_appscript):
        """Test get_current_track handles errors."""
        _, mock_instance, _ = mock_appscript
        
        # Set up the mock to raise an exception
        import appscript
        mock_instance.current_track.side_effect = appscript.reference.CommandError
        
        itunes = ITunes10()
        result = itunes.get_current_track()
        
        assert result is None
    
    def test_play(self, mock_appscript):
        """Test play method."""
        _, mock_instance, _ = mock_appscript
        
        itunes = ITunes10()
        itunes.play()
        
        mock_instance.play.assert_called_once()
    
    def test_pause(self, mock_appscript):
        """Test pause method."""
        _, mock_instance, _ = mock_appscript
        
        itunes = ITunes10()
        itunes.pause()
        
        mock_instance.pause.assert_called_once()
    
    def test_next_track(self, mock_appscript):
        """Test next_track method."""
        _, mock_instance, _ = mock_appscript
        
        itunes = ITunes10()
        itunes.next_track()
        
        mock_instance.next_track.assert_called_once()
    
    def test_previous_track(self, mock_appscript):
        """Test previous_track method."""
        _, mock_instance, _ = mock_appscript
        
        itunes = ITunes10()
        itunes.previous_track()
        
        mock_instance.previous_track.assert_called_once()
    
    def test_get_playlists(self, mock_appscript):
        """Test get_playlists method."""
        _, mock_instance, _ = mock_appscript
        
        # Set up mock playlists
        playlist1 = MagicMock()
        playlist1.name.return_value = "Playlist 1"
        playlist1.tracks.return_value = [1, 2, 3]  # 3 tracks
        
        playlist2 = MagicMock()
        playlist2.name.return_value = "Playlist 2"
        playlist2.tracks.return_value = [1, 2, 3, 4, 5]  # 5 tracks
        
        mock_instance.playlists.return_value = [playlist1, playlist2]
        
        itunes = ITunes10()
        result = itunes.get_playlists()
        
        assert len(result) == 2
        assert result[0]["name"] == "Playlist 1"
        assert result[0]["track_count"] == 3
        assert result[1]["name"] == "Playlist 2"
        assert result[1]["track_count"] == 5
    
    def test_get_playlists_with_limit(self, mock_appscript):
        """Test get_playlists method with limit."""
        _, mock_instance, _ = mock_appscript
        
        # Set up mock playlists
        playlist1 = MagicMock()
        playlist1.name.return_value = "Playlist 1"
        playlist1.tracks.return_value = [1, 2, 3]
        
        playlist2 = MagicMock()
        playlist2.name.return_value = "Playlist 2"
        playlist2.tracks.return_value = [1, 2, 3, 4, 5]
        
        mock_instance.playlists.return_value = [playlist1, playlist2]
        
        itunes = ITunes10()
        result = itunes.get_playlists(limit=1)
        
        assert len(result) == 1
        assert result[0]["name"] == "Playlist 1"
    
    def test_play_playlist(self, mock_appscript):
        """Test play_playlist method."""
        _, mock_instance, _ = mock_appscript
        
        # Set up the mock playlist
        mock_playlist = MagicMock()
        mock_playlist.exists.return_value = True
        mock_instance.playlists.__getitem__.return_value = mock_playlist
        
        itunes = ITunes10()
        result = itunes.play_playlist("Test Playlist")
        
        assert result is True
        mock_instance.playlists.__getitem__.assert_called_with("Test Playlist")
        mock_playlist.play.assert_called_once()
    
    def test_play_playlist_nonexistent(self, mock_appscript):
        """Test play_playlist with nonexistent playlist."""
        _, mock_instance, _ = mock_appscript
        
        # Set up the mock playlist
        mock_playlist = MagicMock()
        mock_playlist.exists.return_value = False
        mock_instance.playlists.__getitem__.return_value = mock_playlist
        
        itunes = ITunes10()
        result = itunes.play_playlist("Nonexistent Playlist")
        
        assert result is False
        mock_playlist.play.assert_not_called()
    
    def test_set_volume(self, mock_appscript):
        """Test set_volume method."""
        _, mock_instance, _ = mock_appscript
        
        itunes = ITunes10()
        itunes.set_volume(50)
        
        mock_instance.sound_volume.set.assert_called_with(50)
    
    def test_set_volume_invalid(self, mock_appscript):
        """Test set_volume with invalid values."""
        _, mock_instance, _ = mock_appscript
        
        itunes = ITunes10()
        
        # Too low
        itunes.set_volume(-10)
        mock_instance.sound_volume.set.assert_not_called()
        
        # Too high
        mock_instance.sound_volume.set.reset_mock()
        itunes.set_volume(110)
        mock_instance.sound_volume.set.assert_not_called()
    
    def test_get_volume(self, mock_appscript):
        """Test get_volume method."""
        _, mock_instance, _ = mock_appscript
        
        mock_instance.sound_volume.get.return_value = 75
        
        itunes = ITunes10()
        result = itunes.get_volume()
        
        assert result == 75
    
    def test_is_playing(self, mock_appscript):
        """Test is_playing method."""
        _, mock_instance, mock_k = mock_appscript
        
        mock_instance.player_state.return_value = mock_k.playing
        
        itunes = ITunes10()
        result = itunes.is_playing()
        
        assert result is True
    
    def test_is_playing_paused(self, mock_appscript):
        """Test is_playing when paused."""
        _, mock_instance, mock_k = mock_appscript
        
        mock_instance.player_state.return_value = mock_k.paused
        
        itunes = ITunes10()
        result = itunes.is_playing()
        
        assert result is False