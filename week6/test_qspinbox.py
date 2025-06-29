import pytest
from qspinbox import SpinBox, _nim


@pytest.fixture
def spinbox_widget(qtbot):
    """Fixture to create and return a SpinBox instance."""
    widget = SpinBox()
    qtbot.addWidget(widget)
    return widget


def test_label_initial_text(spinbox_widget):
    """Test that the QLabel shows the correct initial value."""
    assert spinbox_widget.l1.text() == "Nilai: 0"


def test_spinbox_min_max(spinbox_widget):
    """Test that the QSpinBox has correct minimum and maximum values."""
    nim_digits = list(_nim)[3:]
    expected_min = int(min(nim_digits))
    expected_max = int(max(nim_digits))

    assert spinbox_widget.sp.minimum() == expected_min
    assert spinbox_widget.sp.maximum() == expected_max


def test_spinbox_value_updates_label(qtbot, spinbox_widget):
    """Test that changing the spinbox value updates the label."""
    test_value = spinbox_widget.sp.minimum() + 1
    spinbox_widget.sp.setValue(test_value)
    qtbot.wait(100)  # Ensure signal is processed

    assert spinbox_widget.l1.text() == f"Nilai: {test_value}"