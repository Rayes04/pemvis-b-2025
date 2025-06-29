import pytest
from PyQt5.QtWidgets import QAction
from qmenu_qaction import menudemo


@pytest.fixture
def main_window(qtbot):
    """Fixture to create and return the menudemo instance."""
    window = menudemo()
    qtbot.addWidget(window)
    return window


def test_menu_structure(main_window):
    """Test that main menus like File, Help, Run exist."""
    bar = main_window.menuBar()
    menu_titles = [bar.actions()[i].text() for i in range(bar.actions().__len__())]
    assert "File" in menu_titles
    assert "Help" in menu_titles
    assert "Run" in menu_titles


def test_save_action_triggered(qtbot, main_window, capsys):
    """Test that triggering Save action prints the correct message."""
    file_menu = main_window.menuBar().actions()[0].menu()  # "File"
    actions = file_menu.actions()
    
    save_action = next((a for a in actions if a.text() == "Save"), None)
    assert save_action is not None

    with qtbot.waitSignal(save_action.triggered, timeout=100):
        save_action.trigger()

    captured = capsys.readouterr()
    assert "save triggered" in captured.out


def test_edit_paste_value_triggered(qtbot, main_window, capsys):
    """Test triggering of 'paste -> by value' action."""
    file_menu = main_window.menuBar().actions()[0].menu()  # "File"
    edit_menu = next((a.menu() for a in file_menu.actions() if a.text() == "Edit"), None)
    assert edit_menu is not None

    paste_menu = next((a.menu() for a in edit_menu.actions() if a.text() == "paste"), None)
    assert paste_menu is not None

    paste_value_action = next((a for a in paste_menu.actions() if a.text() == "by value"), None)
    assert paste_value_action is not None

    with qtbot.waitSignal(paste_value_action.triggered, timeout=100):
        paste_value_action.trigger()

    captured = capsys.readouterr()
    assert "edit paste value triggered" in captured.out