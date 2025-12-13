import logging

from livingspacetoolkit.views.results_view import Results
from livingspacetoolkit.models.toolkit_state_model import ToolkitState

logger = logging.getLogger(__name__)


class ResultsController:
    def __init__(self,view: Results, toolkit_state: ToolkitState):
        self.view = view
        self.toolkit_state = toolkit_state

        # Connect signals
        self.view.calculate_button.clicked.connect(self.handle_button_click)


    def handle_button_click(self):
        self.view.update_text("Button Pressed")
