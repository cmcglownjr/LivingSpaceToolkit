import logging

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy

from livingspacetoolkit.views import CathedralRoofView, CathedralWallHeightView, FloorPlanView

logger = logging.getLogger(__name__)


class CathedralView(QWidget):
    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()
        layout_sub: QVBoxLayout = QVBoxLayout()
        spacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.sunroom_roof: CathedralRoofView = CathedralRoofView()
        self.sunroom_wall: CathedralWallHeightView = CathedralWallHeightView()
        self.sunroom_floor: FloorPlanView = FloorPlanView()

        layout_sub.addWidget(self.sunroom_wall)
        layout_sub.addSpacerItem(spacer)
        layout_sub.addWidget(self.sunroom_floor)

        layout.addWidget(self.sunroom_roof)
        layout.addLayout(layout_sub)

        self.setLayout(layout)