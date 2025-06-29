import pytest
from PyQt5.QtWidgets import QPushButton
from qstatusbar import statusdemo


@pytest.fixture
def status_window(qtbot):
    window = statusdemo()
    qtbot.addWidget(window)
    return window


def test_menu_actions_exist(status_window):
    """Pastikan menu 'File' memiliki aksi: show, add, remove."""
    file_menu = status_window.menuBar().actions()[0].menu()
    action_texts = [action.text() for action in file_menu.actions()]
    assert "show" in action_texts
    assert "add" in action_texts
    assert "remove" in action_texts


def test_show_message(qtbot, status_window):
    """Simulasikan aksi 'show' dan periksa pesan di status bar."""
    status_window.processtrigger(MockAction("show"))
    assert status_window.statusBar.currentMessage() == "show is clicked"


def test_add_button_to_statusbar(status_window):
    """Uji bahwa tombol ditambahkan ke status bar saat 'add' dipicu."""
    status_window.processtrigger(MockAction("add"))
    assert status_window.b in status_window.statusBar.findChildren(QPushButton)


class MockAction:
    """Kelas tiruan untuk QAction simulasi dalam pengujian."""
    def __init__(self, text):
        self._text = text

    def text(self):
        return self._text