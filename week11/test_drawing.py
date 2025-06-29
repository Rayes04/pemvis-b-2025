import pytest
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPaintEvent
from drawing import Example


@pytest.fixture
def drawing_widget(qtbot):
    """Inisialisasi widget Example dari drawing.py"""
    widget = Example()
    qtbot.addWidget(widget)
    return widget


def test_window_title_and_geometry(drawing_widget):
    """Test judul window dan geometri diinisialisasi dengan benar."""
    assert drawing_widget.windowTitle() == 'Draw Demo'
    rect = drawing_widget.geometry()
    assert rect.width() == 400
    assert rect.height() == 300


def test_paint_event_executes(drawing_widget):
    """Uji bahwa paintEvent() berjalan tanpa exception."""
    # Buat event palsu untuk area lukisan
    fake_event = QPaintEvent(QRect(0, 0, 400, 300))

    # Panggil langsung paintEvent untuk validasi tidak error
    drawing_widget.paintEvent(fake_event)