import sys
import os
import pytest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

# Ensure the script's directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import Example class from event_handler.py
from event_handler import Example


@pytest.fixture(scope="module")
def app():
    """Create a QApplication instance for testing."""
    return QApplication.instance() or QApplication([])


@pytest.fixture
def example_window(app):
    """Create an Example window instance for testing."""
    window = Example()
    return window


def test_window_initialization(example_window):
    """Test if the Example window initializes correctly."""
    assert example_window.windowTitle() == "Event handler"
    assert example_window.width() == 250
    assert example_window.height() == 150
    assert example_window.isVisible()  # Ensure the window is shown


def test_key_press_event(example_window, qtbot):
    """Test if pressing the 'E' key closes the window."""
    assert example_window.isVisible()  # Window should be visible before key press

    # Simulate pressing the 'E' key
    event = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_E, Qt.NoModifier)
    QApplication.sendEvent(example_window, event)

    # After pressing 'E', the window should be closed
    assert not example_window.isVisible()