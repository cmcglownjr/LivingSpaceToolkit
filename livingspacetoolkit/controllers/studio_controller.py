import logging

from livingspacetoolkit.views.studio_view import Studio
from livingspacetoolkit.models.toolkit_state_model import ToolkitState
from livingspacetoolkit.lib.livingspacetoolkit_enums import PitchType, SunroomType, RoofingType, EndCutType, Scenario

logger = logging.getLogger(__name__)


class StudioController:
    def __init__(self, view: Studio, toolkit_state: ToolkitState):
        self.toolkit_state = toolkit_state
        self.sunroom_roof = view.sunroom_roof
        self.sunroom_wall = view.sunroom_wall
        self.sunroom_floor = view.sunroom_floor

        # Connect signals
        self.sunroom_roof.pitch.radio_ratio.clicked.connect(
            lambda: self.handle_pitch_type_click(PitchType.RATIO, SunroomType.STUDIO))
        self.sunroom_roof.pitch.radio_angle.clicked.connect(
            lambda: self.handle_pitch_type_click(PitchType.ANGLE, SunroomType.STUDIO))
        self.sunroom_roof.roofing_type.radio_al.clicked.connect(
            lambda: self.handle_roofing_type_click(RoofingType.ALUMINUM))
        self.sunroom_roof.roofing_type.radio_eco.clicked.connect(
            lambda: self.handle_roofing_type_click(RoofingType.ECO_GREEN))
        self.sunroom_roof.thickness_combo.currentIndexChanged.connect(self.handle_thickness_combo_index_change)

    def handle_pitch_type_click(self, pitch_type: PitchType, sunroom: SunroomType):
        logger.debug(f"{sunroom.name} pitch radio button clicked for type {pitch_type.name}.")
        self.sunroom_roof.pitch.update_pitch_text(pitch_type, sunroom)

    def handle_roofing_type_click(self, roof_type: RoofingType) -> None:
        logger.debug(f"Studio roofing type set to {roof_type.name}.")
        self.toolkit_state.roofing_type = roof_type
        logger.info(f"Populating studio thickness combo box for {roof_type.name} roofing type.")
        self.sunroom_roof.populate_thickness_combo(roof_type)

    def handle_thickness_combo_index_change(self):
        thickness_index = self.sunroom_roof.thickness_combo.currentIndex()
        thickness_item = self.sunroom_roof.thickness_combo.itemData(thickness_index)
        thickness_text = self.sunroom_roof.thickness_combo.itemText(thickness_index)
        self.toolkit_state.thickness = thickness_item
        if thickness_item is not None:
            logger.info(f"Setting thickness to {thickness_text}.")
