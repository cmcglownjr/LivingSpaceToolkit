import pytest
from PySide6.QtCore import Qt


class TestResultsView:

    @pytest.mark.gui
    @pytest.mark.integration
    def test_studio_results(self, qtbot, main_window):
        # Arrange: Set tab to studio and scenario to WALL_HEIGHT_PITCH and input data.
        main_window.tabs_view.setCurrentIndex(0)
        main_window.scenarios_view.radio1.click()
        main_window.tabs_view.studio_view.sunroom_roof.roofing_type.radio_eco.click()
        # Fill in line edits while leaving the rest as default settings
        # Input pitch input
        qtbot.keyClicks(main_window.tabs_view.studio_view.sunroom_roof.pitch.pitch_input, '5')
        qtbot.keyClick(main_window.tabs_view.studio_view.sunroom_roof.pitch.pitch_input, Qt.Key.Key_Return)
        # Input overhang
        qtbot.keyClicks(main_window.tabs_view.studio_view.sunroom_roof.overhang_edit, '10')
        qtbot.keyClick(main_window.tabs_view.studio_view.sunroom_roof.overhang_edit, Qt.Key.Key_Return)
        # Input B Wall
        qtbot.keyClicks(main_window.tabs_view.studio_view.sunroom_wall.b_wall_height_edit, "10'")
        qtbot.keyClick(main_window.tabs_view.studio_view.sunroom_wall.b_wall_height_edit, Qt.Key.Key_Return)
        # Input floor plan
        qtbot.keyClicks(main_window.tabs_view.studio_view.sunroom_floor.wall_a, "12'")
        qtbot.keyClick(main_window.tabs_view.studio_view.sunroom_floor.wall_a, Qt.Key.Key_Return)
        qtbot.keyClicks(main_window.tabs_view.studio_view.sunroom_floor.wall_b, "15'")
        qtbot.keyClick(main_window.tabs_view.studio_view.sunroom_floor.wall_b, Qt.Key.Key_Return)
        qtbot.keyClicks(main_window.tabs_view.studio_view.sunroom_floor.wall_c, "12'")
        qtbot.keyClick(main_window.tabs_view.studio_view.sunroom_floor.wall_c, Qt.Key.Key_Return)
        # Expected
        expected = """Now listing results.
        *===================*
        Given B wall height and pitch...
        The pitch is: 5.0/12.
        The peak height is 180 in.
        The soffit height is 115.8125 in.
        The drip edge is at 121.375 in.
        The maximum height is 186.5 in.
        The A and C Wall heights are 120 in.
        The B Wall height is 120 in.
        This configuration will need 7 roof panels.
        The length of each panel should be 168 in.
        The roof sq. ft. is 262 ft^2.
        You will need 8 boxes of Armstrong Ceiling Panels.
        The overhang on B Wall is 10 in.
        The overhang on A and C Walls are 22 in.
        There are 2 pairs of hang rails at 112 in. each.
        They were divided in half because the original length was longer than 216 in.
        There are 2 pieces of Fascia at 118 in. each for the B wall
        Their original length was more than 216 in. so they were cut in half.
        There is one piece of Fascia at 174 in. for the A Wall and one piece at 174 in for the C wall."""
        # Act
        main_window.results_view.calculate_button.click()

        assert main_window.results_view.results_view.toPlainText() == expected

    @pytest.mark.gui
    @pytest.mark.integration
    def test_cathedral_results(self, qtbot, main_window):
        # Arrange: Set tab to cathedral and scenario to WALL_HEIGHT_PITCH and input data.
        main_window.tabs_view.setCurrentIndex(1)
        main_window.scenarios_view.radio1.click()
        main_window.tabs_view.cathedral_view.sunroom_roof.roofing_type.radio_eco.click()
        # Fill in line edits while leaving the rest as default settings
        # Input A side pitch input
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_roof.pitch_a.pitch_input, '5')
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_roof.pitch_a.pitch_input, Qt.Key.Key_Return)
        # Input C side pitch input
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_roof.pitch_c.pitch_input, '5')
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_roof.pitch_c.pitch_input, Qt.Key.Key_Return)
        # Input overhang
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_roof.overhang_edit, '10')
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_roof.overhang_edit, Qt.Key.Key_Return)
        # Input A Wall
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_wall.a_wall_height_edit, "10'")
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_wall.a_wall_height_edit, Qt.Key.Key_Return)
        # Input C Wall
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_wall.c_wall_height_edit, "10'")
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_wall.c_wall_height_edit, Qt.Key.Key_Return)
        # Input floor plan
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_floor.wall_a, "12'")
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_floor.wall_a, Qt.Key.Key_Return)
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_floor.wall_b, "15'")
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_floor.wall_b, Qt.Key.Key_Return)
        qtbot.keyClicks(main_window.tabs_view.cathedral_view.sunroom_floor.wall_c, "12'")
        qtbot.keyClick(main_window.tabs_view.cathedral_view.sunroom_floor.wall_c, Qt.Key.Key_Return)
        # Expected
        expected = """Now listing results.
        *===================*
        Given wall height and pitch...
        The A side pitch is: 5.0/12.
        The C side pitch is: 5.0/12.
        The peak height is 156.8125 in.
        The A Wall height is 120 in.
        The C Wall height is 120 in.
        The A side soffit height is 115.8125 in.
        The C side soffit height is 115.8125 in.
        The A side drip edge is at 121.375 in.
        The C side drip edge is at 121.375 in.
        The maximum height is 164 in.
        This configuration will need 5 A side roof panels.
        The length of each A side panel should be 108 in.
        This configuration will need 5 C side roof panels.
        The length of each C side panel should be 108 in.
        The C side panels are 1 in. beyond the nearest foot! They should be within the manufacturer's tolerance.
        The total number of roof panels is 10.
        The Total roof sq. ft. is 240 ft^2.
        You will need 8 boxes of Armstrong Ceiling Panels.
        The overhang on A Wall is 10 in.
        The overhang on C Wall is 10 in.
        The overhang on B Wall is 10 in.
        There is 1 pair of hang rails at 108 in on the A wall
        There is 1 pair of hang rails at 108 in on the C wall
        There is 1 pieces of Fascia at 166 in for the A wall
        There is 1 pieces of Fascia at 166 in for the C wall
        There is 1 pieces of Fascia for the A side B Wall at 114 in
        There is 1 pieces of Fascia for the C side B Wall at 114 in"""
        # Act
        main_window.results_view.calculate_button.click()

        assert main_window.results_view.results_view.toPlainText() == expected