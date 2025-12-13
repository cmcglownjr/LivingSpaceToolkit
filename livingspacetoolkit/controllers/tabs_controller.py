import logging

from livingspacetoolkit.views.tabs_view import TabsView
from livingspacetoolkit.models.toolkit_state_model import ToolkitState
from livingspacetoolkit.controllers.studio_controller import StudioController
from livingspacetoolkit.controllers.cathedral_controller import CathedralController
from livingspacetoolkit.lib.livingspacetoolkit_enums import SunroomType

logger = logging.getLogger(__name__)


class TabsController:
    def __init__(self, view: TabsView, toolkit_state: ToolkitState):
        self.view = view
        self.toolkit_state = toolkit_state

        self.studio_controller = StudioController(self.view.studio_view, self.toolkit_state)
        self.cathedral_controller = CathedralController(self.view.cathedral_view, self.toolkit_state)

        # Connect signals
        self.view.currentChanged.connect(self.handle_tab_change)

    def handle_tab_change(self):
        self.toolkit_state.sunroom_type = SunroomType(self.view.currentIndex())
        logging.info(f'The sunroom type, {SunroomType(self.view.currentIndex()).name}, has been selected.')