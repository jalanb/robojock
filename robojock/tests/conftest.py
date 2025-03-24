"""
Pytest configuration for robojock tests.
"""
import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_appscript():
    """Mock the appscript module for testing."""
    with patch('appscript.app') as mock_app:
        # Create a mock appscript app
        mock_instance = MagicMock()
        mock_app.return_value = mock_instance
        
        # Add k namespace for constants
        mock_k = MagicMock()
        mock_k.playing = 'playing'
        mock_k.paused = 'paused'
        mock_k.stopped = 'stopped'
        
        with patch('appscript.k', mock_k):
            yield mock_app, mock_instance, mock_k


@pytest.fixture
def mock_track():
    """Create a mock track for testing."""
    mock = MagicMock()
    mock.name.return_value = "Test Track"
    mock.artist.return_value = "Test Artist"
    mock.album.return_value = "Test Album"
    mock.genre.return_value = "Red"
    mock.rating.return_value = 100
    mock.year.return_value = 2024
    mock.bpm.return_value = 120
    mock.comment.return_value = "Test comment"
    mock.compilation.return_value = False
    mock.composer.return_value = "Test Composer"
    mock.disc_number.return_value = 1
    mock.duration.return_value = 180.5
    mock.played_count.return_value = 42
    mock.played_date.return_value = "2024-01-01 12:00:00"
    mock.track_number.return_value = 5
    return mock


@pytest.fixture
def mock_playlist():
    """Create a mock playlist for testing."""
    mock = MagicMock()
    mock.name.return_value = "Test Playlist"
    
    # Create mock tracks
    mock_tracks = []
    for i in range(5):
        track = MagicMock()
        track.name.return_value = f"Track {i}"
        track.artist.return_value = f"Artist {i}"
        mock_tracks.append(track)
    
    mock.tracks.return_value = mock_tracks
    mock.exists.return_value = True
    
    return mock