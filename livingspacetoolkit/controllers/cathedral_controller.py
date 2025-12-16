import logging

from livingspacetoolkit.views.cathedral_view import CathedralView
from livingspacetoolkit.models import ToolkitStateModel, RoofModel
from livingspacetoolkit.lib.livingspacetoolkit_enums import PitchType, SunroomType, RoofingType, EndCutType, Scenario
from livingspacetoolkit.utils.helpers import set_strikethrough
from .base_sunroom_controller import BaseSunroomController

logger = logging.getLogger(__name__)


class CathedralController(BaseSunroomController):
    def __init__(self, view: CathedralView, toolkit_state: ToolkitStateModel):
        self.toolkit_state = toolkit_state
        self.roof_model: RoofModel = RoofModel(toolkit_state)

        self.sunroom_roof = view.sunroom_roof
        self.sunroom_wall = view.sunroom_wall
        self.sunroom_floor = view.sunroom_floor


    def update_to_scenario(self):
        self.set_to_default()
        self.sunroom_roof.enable_except_pitch()
        match self.toolkit_state.scenario:
            case Scenario.WALL_HEIGHT_PITCH:
                self.sunroom_roof.pitch_a.enabled_state(self.toolkit_state.sunroom_type)
                self.sunroom_roof.pitch_c.enabled_state(self.toolkit_state.sunroom_type)
                set_strikethrough(self.sunroom_wall.a_wall_height_label, False)
                self.sunroom_wall.a_wall_height_edit.setEnabled(True)
                set_strikethrough(self.sunroom_wall.c_wall_height_label, False)
                self.sunroom_wall.c_wall_height_edit.setEnabled(True)
            case Scenario.WALL_HEIGHT_PEAK_HEIGHT:
                set_strikethrough(self.sunroom_wall.peak_height_label, False)
                self.sunroom_wall.peak_height_edit.setEnabled(True)
                set_strikethrough(self.sunroom_wall.a_wall_height_label, False)
                self.sunroom_wall.a_wall_height_edit.setEnabled(True)
                set_strikethrough(self.sunroom_wall.c_wall_height_label, False)
                self.sunroom_wall.c_wall_height_edit.setEnabled(True)
            case Scenario.MAX_HEIGHT_PITCH:
                self.sunroom_roof.pitch_a.enabled_state(self.toolkit_state.sunroom_type)
                self.sunroom_roof.pitch_c.enabled_state(self.toolkit_state.sunroom_type)
                set_strikethrough(self.sunroom_wall.max_height_label, False)
                self.sunroom_wall.max_height_edit.setEnabled(True)
            case Scenario.SOFFIT_HEIGHT_PEAK_HEIGHT:
                set_strikethrough(self.sunroom_wall.peak_height_label, False)
                self.sunroom_wall.peak_height_edit.setEnabled(True)
                set_strikethrough(self.sunroom_wall.soffit_height_a_label, False)
                self.sunroom_wall.soffit_height_a_edit.setEnabled(True)
                set_strikethrough(self.sunroom_wall.soffit_height_c_label, False)
                self.sunroom_wall.soffit_height_c_edit.setEnabled(True)
            case Scenario.SOFFIT_HEIGHT_PITCH:
                self.sunroom_roof.pitch_a.enabled_state(self.toolkit_state.sunroom_type)
                self.sunroom_roof.pitch_c.enabled_state(self.toolkit_state.sunroom_type)
                set_strikethrough(self.sunroom_wall.soffit_height_a_label, False)
                self.sunroom_wall.soffit_height_a_edit.setEnabled(True)
                set_strikethrough(self.sunroom_wall.soffit_height_c_label, False)
                self.sunroom_wall.soffit_height_c_edit.setEnabled(True)
            case Scenario.DRIP_EDGE_PEAK_HEIGHT:
                set_strikethrough(self.sunroom_wall.peak_height_label, False)
                self.sunroom_wall.peak_height_edit.setEnabled(True)
                set_strikethrough(self.sunroom_wall.drip_edge_height_label, False)
                self.sunroom_wall.drip_edge_height_edit.setEnabled(True)
            case Scenario.DRIP_EDGE_PITCH:
                self.sunroom_roof.pitch_a.enabled_state(self.toolkit_state.sunroom_type)
                self.sunroom_roof.pitch_c.enabled_state(self.toolkit_state.sunroom_type)
                set_strikethrough(self.sunroom_wall.drip_edge_height_label, False)
                self.sunroom_wall.drip_edge_height_edit.setEnabled(True)
