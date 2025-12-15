import logging

from PySide6.QtWidgets import QTabWidget

from livingspacetoolkit.views import StudioView, CathedralView

logger = logging.getLogger(__name__)


class TabsView(QTabWidget):
    def __init__(self):
        super().__init__()

        self.studio_view = StudioView()
        self.cathedral_view = CathedralView()

        self.addTab(self.studio_view, "StudioView")
        self.addTab(self.cathedral_view, "CathedralView")
        self.setMinimumSize(600, 400)
