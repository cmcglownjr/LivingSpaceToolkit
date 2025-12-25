import pytest

from livingspacetoolkit.models import ToolkitStateModel
from livingspacetoolkit.lib.toolkit_enums import Scenario, RoofSide, RoofingType, SunroomType, EndCutType
from livingspacetoolkit.lib.toolkit_length import LengthType


class TestToolkitStateModel:

    @pytest.mark.unit
    def test_default_settings(self):
        # Arrange
        toolkit_1 = ToolkitStateModel()
        toolkit_2 = ToolkitStateModel()
        # Act
        toolkit_2.sunroom_type = SunroomType.CATHEDRAL
        toolkit_2.scenario = Scenario.DRIP_EDGE_PITCH
        toolkit_2.pitch[RoofSide.A_SIDE].pitch_value = '5'
        toolkit_2.pitch[RoofSide.B_SIDE].pitch_value = '5'
        toolkit_2.overhang.length = '10'
        toolkit_2.roofing_type = RoofingType.ECO_GREEN
        toolkit_2.thickness.length = '3'
        toolkit_2.end_cuts = EndCutType.UNCUT_TOP_BOTTOM
        toolkit_2.wall_heights[LengthType.DRIP_EDGE_HEIGHT].length = "10'"
        toolkit_2.floor_walls[LengthType.A_WALL_WIDTH].length = "8'"
        toolkit_2.floor_walls[LengthType.B_WALL_WIDTH].length = "10'"
        toolkit_2.floor_walls[LengthType.C_WALL_WIDTH].length = "8'"
        # Assert
        assert toolkit_1 != toolkit_2
        toolkit_2.default_state()
        assert toolkit_1 == toolkit_2