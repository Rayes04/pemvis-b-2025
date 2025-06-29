import pytest
from PyQt5.QtWidgets import QAction
from qtoolbar import tooldemo


@pytest.fixture
def main_window(qtbot):
    """Fixture to create and return the toolbar demo window."""
    window = tooldemo()
    qtbot.addWidget(window)
    return window


def test_toolbar_existence(main_window):
    """Test that toolbars are created and labeled correctly."""
    toolbars = main_window.findChildren(type(main_window.addToolBar("")))
    toolbar_titles = [tb.windowTitle() for tb in toolbars]

    # Toolbars have names "File" and "Edit"
    assert any("File" in tb.objectName() or tb.windowTitle() == "File" for tb in toolbars)
    assert any("Edit" in tb.objectName() or tb.windowTitle() == "Edit" for tb in toolbars)


def test_toolbar_actions_text(main_window):
    """Test that actions have expected text values."""
    toolbars = main_window.findChildren(type(main_window.addToolBar("")))
    file_toolbar = next((tb for tb in toolbars if tb.windowTitle() == "File" or tb.objectName() == "File"), None)

    assert file_toolbar is not None
    action_texts = [action.text() for action in file_toolbar.actions()]
    assert "membuat file baru" in action_texts
    assert "open" in action_texts
    assert "save" in action_texts


def test_toolbar_action_triggered(qtbot, main_window, capsys):
    """Test that triggering a toolbar action prints the expected message."""
    file_toolbar = next((tb for tb in main_window.findChildren(type(main_window.addToolBar("")))
                         if tb.windowTitle() == "File" or tb.objectName() == "File"), None)
    assert file_toolbar is not None

    action = next((a for a in file_toolbar.actions() if a.text() == "open"), None)
    assert action is not None

    # Trigger the action
    action.trigger()

    captured = capsys.readouterr()
    assert "pressed tool button is open" in captured.out