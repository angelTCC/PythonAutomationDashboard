# main.py

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QTabWidget, QStatusBar
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AgroOps Dashboard")
        self.setMinimumSize(QSize(1000, 600))
        self.setWindowIcon(QIcon("assets/icons/app_icon.png"))  # Optional icon

        # Set up tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_dashboard_tab(), "Dashboard")
        self.tabs.addTab(self.create_placeholder_tab("Weather Module"), "Weather")
        self.tabs.addTab(self.create_placeholder_tab("Market Prices"), "Prices")
        self.tabs.addTab(self.create_placeholder_tab("Inventory Management"), "Inventory")
        self.tabs.addTab(self.create_placeholder_tab("Field Tasks"), "Tasks")
        self.tabs.addTab(self.create_placeholder_tab("Alerts"), "Alerts")

        self.setCentralWidget(self.tabs)
        self.setStatusBar(QStatusBar())

    def create_dashboard_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("👋 Welcome to AgroOps Dashboard"))
        layout.addWidget(QLabel("📊 Key daily insights will be shown here."))
        layout.addWidget(QLabel("📊 Key daily insights will be shown here."))
        widget.setLayout(layout)
        return widget

    def create_placeholder_tab(self, text):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"{text} coming soon..."))
        widget.setLayout(layout)
        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
