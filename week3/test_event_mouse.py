import sys
import os
import pytest
from PyQt5.QtWidgets import QApplication

# Ensure the script's directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import Example class from event_mouse.py
from event_mouse import Example


@pytest.fixture(scope="module")
def app():
    """Create a QApplication instance for testing."""
    return QApplication.instance() or QApplication([])


@pytest.fixture
def example_window(qtbot):
    """Create an Example window instance for testing with qtbot."""
    window = Example()
    qtbot.addWidget(window)  # Ensure PyQt cleanup is handled
    return window


def test_window_initialization(example_window):
    """Test if the Example window initializes correctly."""
    assert example_window.windowTitle() == "Event object"
    assert example_window.width() == 450
    assert example_window.height() == 300
    assert example_window.isVisible()  # Ensure the window is shown