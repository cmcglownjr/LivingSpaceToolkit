import logging

from livingspacetoolkit.views.cathedral_view import CathedralView
from livingspacetoolkit.models.toolkit_state_model import ToolkitState
from livingspacetoolkit.lib.livingspacetoolkit_enums import PitchType, SunroomType, RoofingType, EndCutType, Scenario

logger = logging.getLogger(__name__)


class CathedralController:
    def __init__(self, view: CathedralView, toolkit_state: ToolkitState):
        self.view = view
        self.toolkit_state = toolkit_state
