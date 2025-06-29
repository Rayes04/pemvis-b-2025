import pytest
from PyQt5.QtWidgets import QSplitter, QTextEdit, QFrame
from PyQt5.QtCore import Qt
from qsplitter import Example


@pytest.fixture
def splitter_widget(qtbot):
    widget = Example()
    widget.initUI()
    qtbot.addWidget(widget)
    return widget


def test_splitter_structure(splitter_widget):
    """Test QSplitter structure and orientation."""

    # Cari splitter utama (vertikal)
    splitters = splitter_widget.findChildren(QSplitter)
    assert len(splitters) >= 2

    splitter_vertical = next((s for s in splitters if s.orientation() == Qt.Vertical), None)
    splitter_horizontal = next((s for s in splitters if s.orientation() == Qt.Horizontal), None)

    assert splitter_vertical is not None
    assert splitter_horizontal is not None

    # Cek jumlah widget pada horizontal splitter
    assert splitter_horizontal.count() == 3

    # Validasi tipe widget
    widget_types = [type(splitter_horizontal.widget(i)) for i in range(splitter_horizontal.count())]
    assert QFrame in widget_types
    assert widget_types.count(QTextEdit) == 2


def test_splitter_sizes(splitter_widget):
    """Test horizontal splitter's sizes maintain expected proportions."""
    splitter_horizontal = next((s for s in splitter_widget.findChildren(QSplitter)
                                 if s.orientation() == Qt.Horizontal), None)
    assert splitter_horizontal is not None

    sizes = splitter_horizontal.sizes()
    assert len(sizes) == 3

    # Cek proporsi relatif: ukuran kedua harus lebih besar dari pertama
    assert sizes[1] > sizes[0]
