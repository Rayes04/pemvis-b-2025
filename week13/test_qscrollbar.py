import pytest
from PyQt5.QtWidgets import QScrollBar, QLabel
from PyQt5.QtGui import QColor, QPalette
from qscrollbar import Example


@pytest.fixture
def scrollbar_widget(qtbot):
    widget = Example()
    qtbot.addWidget(widget)
    return widget


def test_widgets_exist(scrollbar_widget):
    """Pastikan QLabel dan semua QScrollBar dibuat."""
    assert isinstance(scrollbar_widget.l1, QLabel)
    for scrollbar in [scrollbar_widget.s1, scrollbar_widget.s2, scrollbar_widget.s3, scrollbar_widget.s4]:
        assert isinstance(scrollbar, QScrollBar)
        assert scrollbar.maximum() == 255


def test_scrollbar_changes_label_color(scrollbar_widget):
    """Set nilai scrollbars dan verifikasi warna teks QLabel berubah."""

    # Tetapkan nilai RGB + Alpha
    scrollbar_widget.s1.setValue(100)
    scrollbar_widget.s2.setValue(150)
    scrollbar_widget.s3.setValue(200)
    scrollbar_widget.s4.setValue(128)

    # Panggil manual karena tidak semua .valueChanged akan memicu .sliderMoved di pengujian
    scrollbar_widget.sliderval()

    # Ambil palette dari label
    palette = scrollbar_widget.l1.palette()
    color = palette.color(QPalette.Foreground)

    expected_color = QColor(100, 150, 200, 128)
    assert color == expected_color