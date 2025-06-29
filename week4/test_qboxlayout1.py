import pytest
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton
import qboxlayout1

@pytest.fixture
def test_window(qtbot):
    win = qboxlayout1.create_window()
    qtbot.addWidget(win)
    return win

def test_window_title(test_window):
    assert test_window.windowTitle() == "PyQt"

def test_layout_structure(test_window):
    layout = test_window.layout()
    assert isinstance(layout, QVBoxLayout)
    assert layout.count() == 2  # One stretch, one hbox layout

    # Second item should be the HBoxLayout
    hbox = layout.itemAt(1).layout()
    assert isinstance(hbox, QHBoxLayout)
    assert hbox.count() == 2

    # Check buttons
    b1 = hbox.itemAt(0).widget()
    b2 = hbox.itemAt(1).widget()
    assert isinstance(b1, QPushButton)
    assert isinstance(b2, QPushButton)
    assert b1.text() == "Button1"
    assert b2.text() == "Button2"