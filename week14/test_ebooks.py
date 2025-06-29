import os
import shutil
import sqlite3
import pytest
from datetime import datetime

from app_ebooks import EbookManager


@pytest.fixture(scope="function")
def app_fixture(qtbot):
    """Initialize the EbookManager app safely using qtbot (creates QApplication)."""
    # Setup paths
    test_db = "test_ebooks.db"
    test_pdf_dir = os.path.join(os.getcwd(), "test_pdf_files")
    os.makedirs(test_pdf_dir, exist_ok=True)

    # Create the app window (requires QApplication from qtbot)
    app = EbookManager()
    qtbot.addWidget(app)

    # Patch with test database and folder
    app.conn.close()
    app.conn = sqlite3.connect(test_db)
    app.pdf_folder = test_pdf_dir
    app.initDatabase()

    yield app

    # Teardown
    app.conn.close()
    if os.path.exists(test_db):
        os.remove(test_db)
    if os.path.exists(test_pdf_dir):
        shutil.rmtree(test_pdf_dir)


def test_database_initialization(app_fixture):
    """Test that the ebooks table is created properly."""
    cur = app_fixture.conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ebooks'")
    result = cur.fetchone()
    assert result is not None
    assert result[0] == "ebooks"


def test_insert_ebook_record(app_fixture):
    """Test inserting an ebook record into the database."""
    cur = app_fixture.conn.cursor()
    title = "Test Ebook"
    author = "Tester"
    genre = "Fiction"
    rating = 8
    pages = 123
    file_path = os.path.join(app_fixture.pdf_folder, "test_ebook.pdf")

    with open(file_path, "w") as f:
        f.write("Dummy PDF content")

    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
        INSERT INTO ebooks (title, author, genre, rating, pages, file_path, date_added)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (title, author, genre, rating, pages, file_path, date_added))
    app_fixture.conn.commit()

    cur.execute("SELECT * FROM ebooks WHERE title=?", (title,))
    result = cur.fetchone()
    assert result is not None
    assert result[1] == title
    assert result[2] == author


def test_pdf_folder_creation(app_fixture):
    """Test that the PDF folder is created and writable."""
    test_path = os.path.join(app_fixture.pdf_folder, "sample.pdf")
    with open(test_path, "w") as f:
        f.write("Test content")
    assert os.path.exists(test_path)


def test_load_ebooks_method_runs(app_fixture):
    """Ensure loadEbooks() executes without error."""
    try:
        app_fixture.loadEbooks()
    except Exception as e:
        pytest.fail(f"loadEbooks raised an error: {e}")