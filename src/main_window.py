import logging

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from views.scenarios_view import ScenariosView
from views.roof_pitch_component import RoofPitch

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LivingSpace Toolkit")

        self.scenarios = ScenariosView()
        self.roof_pitch = RoofPitch("Pitch")

        # central: QWidget = QWidget()

        layout: QVBoxLayout = QVBoxLayout()

        layout.addWidget(self.scenarios)
        # central.setLayout(layout)
        self.setLayout(layout)

        self.setCentralWidget(self.scenarios)