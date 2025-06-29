import pytest
from PyQt5.QtWidgets import QFileDialog
from qfiledialog import filedialogdemo


@pytest.fixture
def file_dialog_widget(qtbot):
    widget = filedialogdemo()
    qtbot.addWidget(widget)
    return widget


def test_getfile_sets_label_pixmap(monkeypatch, file_dialog_widget):
    monkeypatch.setattr("qfiledialog.QFileDialog.getOpenFileName",
                        lambda *args, **kwargs: ("/path/to/image.jpg", ""))

    monkeypatch.setattr(file_dialog_widget.le, "setPixmap",
                        lambda pixmap: setattr(file_dialog_widget.le, "_pixmap_set", True))

    file_dialog_widget.getfile()
    assert hasattr(file_dialog_widget.le, "_pixmap_set")


def test_getfiles_sets_text(monkeypatch, tmp_path, file_dialog_widget):
    test_file = tmp_path / "dummy.txt"
    expected_text = "This is sample file content."
    test_file.write_text(expected_text)

    # 🧪 Subclass QFileDialog so we don’t override the whole class
    class FakeDialog(QFileDialog):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def exec_(self):
            return True

        def selectedFiles(self):
            return [str(test_file)]

    monkeypatch.setattr("qfiledialog.QFileDialog", FakeDialog)

    file_dialog_widget.getfiles()
    assert file_dialog_widget.contents.toPlainText() == expected_text