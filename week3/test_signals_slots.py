import sys
import os
import pytest
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider
from PyQt5.QtCore import Qt

# Ensure the script's directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import Example class from signals_slots.py
from signals_slots import Example


@pytest.fixture(scope="module")
def app():
    """Ensure QApplication is created once for all tests."""
    return QApplication.instance() or QApplication([])


@pytest.fixture
def example_window(qtbot):
    """Create an Example window instance for testing with qtbot."""
    window = Example()
    qtbot.addWidget(window)  # Ensures PyQt cleanup
    return window


def test_window_initialization(example_window):
    """Test if the Example window initializes correctly."""
    assert isinstance(example_window, QWidget)
    assert example_window.windowTitle() == "Signal and slot"
    assert example_window.width() == 250
    assert example_window.height() == 150
    assert example_window.isVisible()  # Ensure the window is shown


def test_slider_updates_lcd(example_window, qtbot):
    """Test if moving the slider updates the LCD display."""
    slider = example_window.findChild(QSlider)
    lcd = example_window.findChild(QLCDNumber)

    assert slider is not None
    assert lcd is not None

    # Move slider to 25
    qtbot.mousePress(slider, Qt.LeftButton)
    slider.setValue(25)  # Set slider value to 25
    qtbot.wait(100)  # Wait for UI update

    assert lcd.value() == 25  # Ensure LCD displays correct value