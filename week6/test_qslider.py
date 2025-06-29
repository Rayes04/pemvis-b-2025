import pytest
from PyQt5.QtGui import QFont
from qslider import Slider, _nim


@pytest.fixture
def slider_widget(qtbot):
    """Create and return a Slider instance with qtbot support."""
    widget = Slider()
    qtbot.addWidget(widget)
    return widget


def test_label_initial_text(slider_widget):
    """Test that the QLabel displays the NIM correctly on initialization."""
    assert slider_widget.l1.text() == _nim


def test_slider_value_range(slider_widget):
    """Test that slider min and max values are set correctly."""
    nim_digits = list(_nim)[3:]
    expected_min = int(min(nim_digits)) * 10 + 1
    expected_max = int(max(nim_digits)) * 10 + 1
    assert slider_widget.sl.minimum() == expected_min
    assert slider_widget.sl.maximum() == expected_max


def test_slider_initial_value_and_font(slider_widget):
    """Test that the slider and label font size are initialized properly."""
    expected_font_size = slider_widget.sl.value()
    current_font: QFont = slider_widget.l1.font()
    assert current_font.pointSize() == expected_font_size


def test_slider_changes_font_size(qtbot, slider_widget):
    """Test that moving the slider updates the label font size accordingly."""
    new_value = slider_widget.sl.minimum() + 5
    slider_widget.sl.setValue(new_value)
    qtbot.wait(100)  # Give time for the signal to be processed

    updated_font: QFont = slider_widget.l1.font()
    assert updated_font.pointSize() == new_value