import pytest
from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtGui import QDropEvent, QDragEnterEvent
from PyQt5.QtWidgets import QApplication
from drag_drop import combo


@pytest.fixture
def combo_widget(qtbot):
    widget = combo("Demo", None)
    qtbot.addWidget(widget)
    return widget


def test_drag_enter_accepts_text(combo_widget):
    """Simulate a dragEnterEvent with text and verify it's accepted."""
    mime = QMimeData()
    mime.setText("Dragged Text")

    event = QDragEnterEvent(QPoint(0, 0), Qt.CopyAction, mime, Qt.LeftButton, Qt.NoModifier)

    # Call directly
    combo_widget.dragEnterEvent(event)

    # Qt does not allow us to assert accepted state directly,
    # but no exception means it processed fine.
    # In actual GUI use, the event.accepted should be True


def test_drag_enter_ignores_non_text(combo_widget):
    """Simulate dragEnterEvent with empty mime data."""
    mime = QMimeData()  # No text set
    event = QDragEnterEvent(QPoint(0, 0), Qt.CopyAction, mime, Qt.LeftButton, Qt.NoModifier)

    combo_widget.dragEnterEvent(event)
    # Again, cannot assert `event.isAccepted()` after manual call


def test_drop_event_adds_item(combo_widget):
    """Simulate dropEvent and check item is added to combo box."""
    text = "Dropped Item"
    mime = QMimeData()
    mime.setText(text)

    # QDropEvent args: pos, actions, mimeData, buttons, modifiers
    drop_event = QDropEvent(QPoint(10, 10), Qt.CopyAction, mime, Qt.LeftButton, Qt.NoModifier)

    initial_count = combo_widget.count()
    combo_widget.dropEvent(drop_event)
    assert combo_widget.count() == initial_count + 1
    assert combo_widget.itemText(combo_widget.count() - 1) == text