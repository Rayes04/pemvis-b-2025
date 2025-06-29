import pytest
from PyQt5.QtWidgets import QMessageBox
from qlist import myListWidget


@pytest.fixture
def list_widget(qtbot):
    """Set up the list widget with items and connections."""
    widget = myListWidget()
    qtbot.addWidget(widget)
    widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])
    return widget


def test_items_added(list_widget):
    """Test that all items are added to the list widget."""
    assert list_widget.count() == 4
    assert list_widget.item(0).text() == "Item 1"
    assert list_widget.item(3).text() == "Item 4"


def test_item_clicked(monkeypatch, list_widget):
    """Simulate clicking an item and check QMessageBox.warning is called."""
    result = {}

    def fake_warning(parent, title, text):
        result["text"] = text

    monkeypatch.setattr(QMessageBox, "warning", fake_warning)

    item = list_widget.item(1)  # "Item 2"
    list_widget.Clicked(item)

    assert result["text"] == "You clicked: Item 2"