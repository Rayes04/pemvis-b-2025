import pytest
from qdock import dockdemo
from PyQt5.QtWidgets import QDockWidget, QListWidget, QTextEdit


@pytest.fixture
def dock_window(qtbot):
    window = dockdemo()
    qtbot.addWidget(window)
    return window


def test_dock_widget_exists(dock_window):
    """Verifikasi QDockWidget ditambahkan dan berisi QListWidget."""
    dock = dock_window.items
    assert isinstance(dock, QDockWidget)
    assert isinstance(dock.widget(), QListWidget)


def test_listwidget_contents(dock_window):
    """Pastikan QListWidget memiliki item yang sesuai."""
    list_widget = dock_window.listWidget
    items = [list_widget.item(i).text() for i in range(list_widget.count())]
    assert items == ["item1", "item2", "item3"]


def test_central_widget_is_textedit(dock_window):
    """Pastikan QTextEdit digunakan sebagai central widget."""
    central = dock_window.centralWidget()
    assert isinstance(central, QTextEdit)


def test_menu_file_contains_actions(dock_window):
    """Pastikan menu 'File' memiliki aksi yang diharapkan."""
    menu_bar = dock_window.menuBar()
    file_menu = menu_bar.actions()[0].menu()
    actions = [action.text() for action in file_menu.actions()]
    assert "New" in actions
    assert "save" in actions
    assert "quit" in actions