import logging

from PySide6.QtWidgets import QTabWidget

from livingspacetoolkit.views.results_view import Results

logger = logging.getLogger(__name__)


class ResultsController:
    def __init__(self, view: Results, main_window: QTabWidget):
        self.view = view
        self.main_window = main_window

        # Connect signals
        self.view.calculate_button.clicked.connect(self.handle_button_click)


    def handle_button_click(self):
        self.view.update_text(f"Button Pressed on tab {self.main_window.currentIndex()}")