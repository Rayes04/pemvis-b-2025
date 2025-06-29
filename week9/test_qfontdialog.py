import pytest
from PyQt5.QtGui import QFont
from qfontdialog import fontdialogdemo


@pytest.fixture
def font_dialog_widget(qtbot):
    """Fixture untuk membuat dan menambahkan widget fontdialogdemo."""
    widget = fontdialogdemo()
    qtbot.addWidget(widget)
    return widget


def test_widget_components_exist(font_dialog_widget):
    """Tes bahwa tombol dan label muncul dengan teks yang benar."""
    assert font_dialog_widget.btn.text() == "choose font"
    assert font_dialog_widget.le.text() == "Hello"


def test_getfont_sets_label_font(monkeypatch, font_dialog_widget):
    """Tes bahwa getfont() mengubah font label jika user memilih font."""

    # Buat font tiruan
    fake_font = QFont("Arial", 20)

    # Monkeypatch dialog supaya tidak membuka GUI
    monkeypatch.setattr("qfontdialog.QFontDialog.getFont", lambda *args, **kwargs: (fake_font, True))

    # Panggil langsung
    font_dialog_widget.getfont()

    # Verifikasi bahwa font label berubah
    applied_font = font_dialog_widget.le.font()
    assert applied_font.family() == "Arial"
    assert applied_font.pointSize() == 20


def test_getfont_canceled(monkeypatch, font_dialog_widget):
    """Tes bahwa getfont() tidak mengubah font jika user membatalkan."""
    original_font = font_dialog_widget.le.font()

    # Simulasikan pembatalan dialog
    monkeypatch.setattr("qfontdialog.QFontDialog.getFont", lambda *args, **kwargs: (QFont("Times", 16), False))

    font_dialog_widget.getfont()

    # Font tidak berubah karena ok == False
    current_font = font_dialog_widget.le.font()
    assert current_font.family() == original_font.family()
    assert current_font.pointSize() == original_font.pointSize()