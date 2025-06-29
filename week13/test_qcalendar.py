import pytest
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QCalendarWidget, QLabel
from qcalendar import Example


@pytest.fixture
def calendar_widget(qtbot):
    """Buat dan kembalikan instance kalender."""
    widget = Example()
    qtbot.addWidget(widget)
    return widget


def test_calendar_and_label_exist(calendar_widget):
    """Pastikan QCalendarWidget dan QLabel ada."""
    calendar = calendar_widget.findChild(QCalendarWidget)
    label = calendar_widget.findChild(QLabel)

    assert calendar is not None
    assert label is not None


def test_label_updates_on_click(calendar_widget, qtbot):
    """Klik tanggal di kalender dan pastikan label diperbarui."""

    calendar = calendar_widget.findChild(QCalendarWidget)
    label = calendar_widget.findChild(QLabel)

    # Set tanggal tertentu
    date = QDate(2024, 12, 25)
    calendar.setSelectedDate(date)

    # Emit sinyal klik secara manual
    calendar.clicked.emit(date)

    # Verifikasi label berubah
    assert label.text() == date.toString()