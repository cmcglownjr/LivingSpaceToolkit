import logging

from typing import Dict
from livingspacetoolkit.models.toolkit_state_model import ToolkitStateModel
from livingspacetoolkit.lib.toolkit_enums import PitchType, SunroomType, RoofingType, EndCutType, Scenario

logger = logging.getLogger(name="livingspacetoolkit")


class RoofModel:
    def __init__(self, toolkit_state_model: ToolkitStateModel):
        self.toolkit_state_model = toolkit_state_model

    @staticmethod
    def set_thickness_combo_dict(roof_type: RoofingType) -> Dict[str, str]:
        combo_item_dict: Dict = {}
        match roof_type:
            case RoofingType.ALUMINUM:
                combo_item_dict.update(
                    {
                        '3"': '3"',
                        '6"': '6"'
                    }
                )
            case RoofingType.ECO_GREEN:
                combo_item_dict.update(
                    {
                        '6"': '6"',
                        '8"': '8 1/4"',
                        '10"': '10 1/4"',
                        '12"': '12 1/4"'
                    } # Need to use fractions to get regex to work.
                )
        return combo_item_dict