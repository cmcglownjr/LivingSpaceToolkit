import pytest

from livingspacetoolkit.lib.toolkit_enums import SunroomType


class TestFascia:

    @pytest.mark.gui
    @pytest.mark.integration
    def test_studio_fascia(self, main_window):
        # Arrange: Set tab to studio and scenario to WALL_HEIGHT_PITCH.
        main_window.tabs_view.setCurrentIndex(0)
        main_window.scenarios_view.radio1.click()
        # Select roofing type to enable fascia
        main_window.tabs_view.studio_view.sunroom_roof.roofing_type.radio_eco.click()

        assert main_window.tabs_view.studio_view.sunroom_roof.fascia.isChecked() == True
        assert main_window.toolkit_state.sunroom_type == SunroomType.STUDIO
        assert main_window.toolkit_state.fascia == True
        # Uncheck fascia
        main_window.tabs_view.studio_view.sunroom_roof.fascia.click()
        assert main_window.tabs_view.studio_view.sunroom_roof.fascia.isChecked() == False
        assert main_window.toolkit_state.fascia == False

    @pytest.mark.gui
    @pytest.mark.integration
    def test_cathedral_fascia(self, main_window):
        # Arrange: Set tab to cathedral and scenario to WALL_HEIGHT_PITCH.
        main_window.tabs_view.setCurrentIndex(1)
        main_window.scenarios_view.radio1.click()
        # Select roofing type to enable fascia
        main_window.tabs_view.cathedral_view.sunroom_roof.roofing_type.radio_eco.click()

        assert main_window.tabs_view.cathedral_view.sunroom_roof.fascia.isChecked() == True
        assert main_window.toolkit_state.sunroom_type == SunroomType.CATHEDRAL
        assert main_window.toolkit_state.fascia == True
        # Uncheck fascia
        main_window.tabs_view.cathedral_view.sunroom_roof.fascia.click()
        assert main_window.tabs_view.cathedral_view.sunroom_roof.fascia.isChecked() == False
        assert main_window.toolkit_state.fascia == False