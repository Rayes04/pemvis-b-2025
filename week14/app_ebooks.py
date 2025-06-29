import os
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt

class EbookManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ebook Manager")
        self.setGeometry(100, 100, 600, 400)

        # Inisialisasi folder PDF dan koneksi DB
        self.pdf_folder = os.path.join(os.getcwd(), "pdf_files")
        os.makedirs(self.pdf_folder, exist_ok=True)

        self.conn = sqlite3.connect("ebooks.db")
        self.initDatabase()

        # Komponen UI
        self.label = QLabel("Welcome to Ebook Manager")
        self.load_button = QPushButton("Load Ebooks")
        self.load_button.clicked.connect(self.showEbooks)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "ID", "Title", "Author", "Genre", "Rating", "Pages", "Added"
        ])

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def initDatabase(self):
        """Membuat tabel ebooks jika belum ada."""
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ebooks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                genre TEXT,
                rating INTEGER,
                pages INTEGER,
                file_path TEXT,
                date_added TEXT
            )
        """)
        self.conn.commit()

    def loadEbooks(self):
        """Ambil semua data dari tabel ebooks."""
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, author, genre, rating, pages, date_added FROM ebooks")
        return cur.fetchall()

    def showEbooks(self):
        """Tampilkan isi database ke tabel GUI."""
        data = self.loadEbooks()
        self.label.setText(f"{len(data)} ebooks loaded")
        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

# Untuk menjalankan aplikasi
if __name__ == "__main__":
    app = QApplication([])
    window = EbookManager()
    window.show()
    app.exec_()
