import logging

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QPixmap, QIcon

import livingspacetoolkit.Resource.resources_rc

from livingspacetoolkit.views.scenarios_view import ScenariosView
from livingspacetoolkit.views.roof_pitch_component import RoofPitch
from livingspacetoolkit.views.roofing_type_component import RoofingType
from livingspacetoolkit.views.roof_end_cuts_component import RoofEndCuts
from livingspacetoolkit.views.floor_plan_component import FloorPlan

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()

        self.setWindowTitle("LivingSpace Toolkit")
        self.setWindowIcon(QIcon(":/LivingSpace/LivingSpace_Icon"))

        self.logo: QLabel = QLabel()
        logo_image: QPixmap = QPixmap(":/LivingSpace/LivingSpace_Logo")
        self.logo.setPixmap(logo_image)

        self.scenarios = ScenariosView()
        self.roof_pitch = RoofPitch("Pitch")
        self.roofing_type = RoofingType()
        self.roof_end_cuts = RoofEndCuts()
        self.floor_plan = FloorPlan()

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self.logo)
        layout.addWidget(self.scenarios)
        layout.addWidget(self.roof_end_cuts)
        layout.addWidget(self.floor_plan)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        self.setMaximumSize(QSize(950, 1000))
        self.setMinimumSize(QSize(950, 1000))