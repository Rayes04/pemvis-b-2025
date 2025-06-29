import pytest
from qinputdialog import inputdialogdemo


@pytest.fixture
def input_dialog_widget(qtbot):
    widget = inputdialogdemo()
    qtbot.addWidget(widget)
    return widget


def test_getItem_sets_lineedit(monkeypatch, input_dialog_widget):
    """Test getItem() updates the first line edit with selected item."""

    monkeypatch.setattr("qinputdialog.QInputDialog.getItem",
                        lambda *args, **kwargs: ("Python", True))

    input_dialog_widget.getItem()
    assert input_dialog_widget.le.text() == "Python"


def test_getItem_cancel_does_not_set_text(monkeypatch, input_dialog_widget):
    """Test getItem() does not update line edit when canceled."""
    monkeypatch.setattr("qinputdialog.QInputDialog.getItem",
                        lambda *args, **kwargs: ("Python", False))

    input_dialog_widget.getItem()
    assert input_dialog_widget.le.text() == ""


def test_gettext_sets_lineedit(monkeypatch, input_dialog_widget):
    """Test gettext() sets user name in line edit."""
    monkeypatch.setattr("qinputdialog.QInputDialog.getText",
                        lambda *args, **kwargs: ("Zaf", True))

    input_dialog_widget.gettext()
    assert input_dialog_widget.le1.text() == "Zaf"


def test_gettext_cancel(monkeypatch, input_dialog_widget):
    """Test that canceling getText does not update line edit."""
    monkeypatch.setattr("qinputdialog.QInputDialog.getText",
                        lambda *args, **kwargs: ("Zaf", False))

    input_dialog_widget.gettext()
    assert input_dialog_widget.le1.text() == ""


def test_getint_sets_lineedit(monkeypatch, input_dialog_widget):
    """Test getint() updates line edit with integer value."""
    monkeypatch.setattr("qinputdialog.QInputDialog.getInt",
                        lambda *args, **kwargs: (42, True))

    input_dialog_widget.getint()
    assert input_dialog_widget.le2.text() == "42"


def test_getint_cancel(monkeypatch, input_dialog_widget):
    """Test getint() does not update line edit when canceled."""
    monkeypatch.setattr("qinputdialog.QInputDialog.getInt",
                        lambda *args, **kwargs: (42, False))

    input_dialog_widget.getint()
    assert input_dialog_widget.le2.text() == ""