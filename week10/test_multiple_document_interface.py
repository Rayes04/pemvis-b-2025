import pytest
from PyQt5.QtWidgets import QAction, QTextEdit, QMdiSubWindow
from multiple_document_interface import MainWindow


@pytest.fixture
def mdi_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window


def test_menu_actions_exist(mdi_window):
    """Pastikan menu File berisi aksi New, cascade, dan Tiled."""
    menu_bar = mdi_window.menuBar()
    file_menu = menu_bar.actions()[0].menu()

    actions = [action.text() for action in file_menu.actions()]
    assert "New" in actions
    assert "cascade" in actions
    assert "Tiled" in actions


def test_new_subwindow_added(mdi_window):
    """Tes bahwa memilih 'New' menambahkan QMdiSubWindow."""
    file_menu = mdi_window.menuBar().actions()[0].menu()
    new_action = next(a for a in file_menu.actions() if a.text() == "New")

    # Trigger action
    new_action.trigger()

    subwindows = mdi_window.mdi.subWindowList()
    assert len(subwindows) == 1
    assert isinstance(subwindows[0], QMdiSubWindow)
    assert isinstance(subwindows[0].widget(), QTextEdit)


def test_cascade_and_tile_does_not_crash(mdi_window):
    """Tes bahwa cascade dan tile berjalan tanpa error setelah menambah subwindow."""
    # Tambahkan beberapa subwindow
    for _ in range(3):
        mdi_window.windowaction(QAction("New", mdi_window))