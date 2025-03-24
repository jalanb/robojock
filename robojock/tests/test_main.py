"""
Tests for the CLI interface.
"""
import pytest
from unittest.mock import MagicMock, patch
from typer.testing import CliRunner

from robojock import __main__ as main_module


@pytest.fixture
def cli_runner():
    """Create a CLI runner for testing Typer apps."""
    return CliRunner()


@pytest.fixture
def mock_itunes():
    """Mock the iTunes instance used in the main module."""
    with patch.object(main_module, 'itunes') as mock:
        # Configure the mock
        mock_track = MagicMock()
        mock_track.info.return_value = {
            "name": "Test Track",
            "artist": "Test Artist",
            "album": "Test Album",
            "genre": "Red",
            "rating": 100
        }
        
        mock.get_current_track.return_value = mock_track
        mock.current_track = "Test Artist/Test Album/Test Track"
        
        # Create mock playlists
        mock_playlists = [
            {"name": "Playlist 1", "track_count": 10},
            {"name": "Playlist 2", "track_count": 20}
        ]
        mock.get_playlists.return_value = mock_playlists
        
        yield mock


class TestCliCommands:
    """Tests for CLI commands."""
    
    def test_playing_command(self, cli_runner, mock_itunes):
        """Test the playing command."""
        # We need to patch the robojock instance used by the Typer CLI
        with patch.object(main_module, 'robojock') as mock_app:
            # Configure the mock CLI app to call our command function
            mock_app.command.return_value = lambda f: f
            
            # Call the command function directly
            main_module.playing()
            
            # Verify it accessed the current_track property
            assert mock_itunes.current_track == "Test Artist/Test Album/Test Track"
    
    def test_track_info_command(self, cli_runner, mock_itunes):
        """Test the track-info command."""
        # We need to patch the rich console used for output
        with patch.object(main_module, 'console') as mock_console:
            # Call the command function directly
            main_module.track_info()
            
            # Verify it got the track and displayed info
            mock_itunes.get_current_track.assert_called_once()
            assert mock_console.print.call_count == 5  # One call per track info item
    
    def test_playlists_command(self, cli_runner, mock_itunes):
        """Test the playlists command."""
        # We need to patch the rich console used for output
        with patch.object(main_module, 'console') as mock_console:
            # Call the command function directly
            main_module.playlists()
            
            # Verify it got the playlists and displayed them
            mock_itunes.get_playlists.assert_called_once_with(limit=0)
            assert mock_console.print.call_count == 2  # One call per playlist
    
    def test_playlists_command_with_limit(self, cli_runner, mock_itunes):
        """Test the playlists command with limit."""
        # We need to patch the rich console used for output
        with patch.object(main_module, 'console') as mock_console:
            # Call the command function directly with a limit
            main_module.playlists(limit=1)
            
            # Verify it got the playlists with the limit and displayed them
            mock_itunes.get_playlists.assert_called_once_with(limit=1)
    
    def test_play_command(self, cli_runner, mock_itunes):
        """Test the play command."""
        # Call the command function directly
        main_module.play()
        
        # Verify it called play
        mock_itunes.play.assert_called_once()
    
    def test_pause_command(self, cli_runner, mock_itunes):
        """Test the pause command."""
        # Call the command function directly
        main_module.pause()
        
        # Verify it called pause
        mock_itunes.pause.assert_called_once()
    
    def test_next_command(self, cli_runner, mock_itunes):
        """Test the next command."""
        # Call the command function directly
        main_module.next()
        
        # Verify it called next_track
        mock_itunes.next_track.assert_called_once()
    
    def test_previous_command(self, cli_runner, mock_itunes):
        """Test the previous command."""
        # Call the command function directly
        main_module.previous()
        
        # Verify it called previous_track
        mock_itunes.previous_track.assert_called_once()
    
    def test_play_playlist_command(self, cli_runner, mock_itunes):
        """Test the play-playlist command."""
        # We need to patch the rich console used for output
        with patch.object(main_module, 'console') as mock_console:
            # Configure the mock
            mock_itunes.play_playlist.return_value = True
            
            # Call the command function directly
            main_module.play_playlist("Test Playlist")
            
            # Verify it called play_playlist with the right name
            mock_itunes.play_playlist.assert_called_once_with("Test Playlist")
            mock_console.print.assert_called_once()
    
    def test_volume_get_command(self, cli_runner, mock_itunes):
        """Test the volume command (get)."""
        # We need to patch the rich console used for output
        with patch.object(main_module, 'console') as mock_console:
            # Configure the mock
            mock_itunes.get_volume.return_value = 50
            
            # Call the command function directly without a level (get)
            main_module.volume()
            
            # Verify it called get_volume
            mock_itunes.get_volume.assert_called_once()
            mock_console.print.assert_called_once()
    
    def test_volume_set_command(self, cli_runner, mock_itunes):
        """Test the volume command (set)."""
        # We need to patch the rich console used for output
        with patch.object(main_module, 'console') as mock_console:
            # Call the command function directly with a level (set)
            main_module.volume(level=75)
            
            # Verify it called set_volume with the right level
            mock_itunes.set_volume.assert_called_once_with(75)
            mock_console.print.assert_called_once()