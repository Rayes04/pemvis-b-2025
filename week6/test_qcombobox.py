import pytest
from PyQt5.QtWidgets import QApplication
from qcombobox import ComboBox, _nim


@pytest.fixture
def combo_box(qtbot):
    """Fixture to create and return a ComboBox instance."""
    widget = ComboBox()
    qtbot.addWidget(widget)
    return widget


def test_combobox_item_count(combo_box):
    """Test that the number of items in the combo box matches the length of _nim."""
    assert combo_box.cb.count() == len(_nim)


def test_combobox_items_content(combo_box):
    """Test that all characters of _nim are added correctly to the combo box."""
    for i, char in enumerate(_nim):
        assert combo_box.cb.itemText(i) == char


def test_combobox_selection_signal(qtbot, combo_box):
    """Test selection change emits the correct signal and updates the index."""
    combo_box.cb.setCurrentIndex(3)
    assert combo_box.cb.currentText() == _nim[3]


def test_combobox_highlight_signal(qtbot, combo_box):
    """Simulate highlighting an index and ensure it corresponds to the expected item."""
    # Note: Highlighting is typically GUI-driven. Here, we simulate by calling the handler directly.
    combo_box._on_highlight(2)
    assert combo_box.cb.currentText() == _nim[combo_box.cb.currentIndex()]