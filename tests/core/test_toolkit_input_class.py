import pytest

from livingspacetoolkit.lib.toolkit_input_class import ToolkitLength, ToolkitPitch
from livingspacetoolkit.lib.toolkit_enums import LengthType, PitchType, RoofSide


class TestToolkitLength:

    def test_equality(self):
        length_1 = ToolkitLength(LengthType.THICKNESS)
        length_1.length = "12'"

        length_2 = ToolkitLength(LengthType.THICKNESS)
        length_2.length = "12'"

        assert length_1 == length_2