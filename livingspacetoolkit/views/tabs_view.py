import logging

from PySide6.QtWidgets import QTabWidget

from livingspacetoolkit.views.studio_view import Studio
from livingspacetoolkit.views.cathedral_view import Cathedral

logger = logging.getLogger(__name__)


class TabsView(QTabWidget):
    def __init__(self):
        super().__init__()

        self.studio_view = Studio()
        self.cathedral_view = Cathedral()

        self.addTab(self.studio_view, "Studio")
        self.addTab(self.cathedral_view, "Cathedral")
        self.setMinimumSize(600, 400)
