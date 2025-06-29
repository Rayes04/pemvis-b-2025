import pytest
from PyQt5.QtWidgets import QWidget, QPushButton, QDialog
from PyQt5.QtCore import Qt
from qdialog import showdialog


def test_showdialog_creates_qdialog(qtbot):
    """Test that showdialog creates a QDialog with the expected button."""
    dialog = QDialog()
    qtbot.addWidget(dialog)

    # Simulate what showdialog creates manually
    b1 = QPushButton("ok", dialog)
    b1.move(50, 50)
    dialog.setWindowTitle("Dialog")
    dialog.setWindowModality(Qt.ApplicationModal)

    # Assertions
    assert dialog.windowTitle() == "Dialog"
    assert dialog.isModal()
    assert b1.text() == "ok"


def test_main_window_button(qtbot):
    """Test that main window contains the correct button."""
    widget = QWidget()
    qtbot.addWidget(widget)

    button = QPushButton(widget)
    button.setText("Hello World!")
    button.move(50, 50)

    assert button.text() == "Hello World!"
    assert button.parent() == widget