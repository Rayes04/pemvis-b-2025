import sys
import os
import pytest
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# Pastikan path proyek ditambahkan
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), )))

# Sekarang coba impor modul hello
from hello import create_window

@pytest.fixture
def hello_window(qtbot):
    """Create and return the actual window from hello.py for testing."""
    window, label, app = create_window()  # Gunakan fungsi asli
    qtbot.addWidget(window)  # Pastikan QtBot menangani widget
    return window, label

def test_window_initialization(hello_window):
    """Test apakah jendela diinisialisasi dengan benar."""
    window, _ = hello_window
    assert isinstance(window, QWidget)
    assert window.windowTitle() == "Hello PyQt5"
    assert window.width() == 500
    assert window.height() == 300
    assert window.isVisible()  # Pastikan jendela ditampilkan

def test_label_properties(hello_window):
    """Test apakah label memiliki properti yang benar."""
    _, label = hello_window
    assert label.text() == "Hello World!"
    assert label.toolTip() == "Tes Tooltips"
    assert label.x() == 50
    assert label.y() == 50