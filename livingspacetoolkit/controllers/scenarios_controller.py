import logging

from livingspacetoolkit.views.scenarios_view import ScenariosView

from livingspacetoolkit.models.toolkit_state_model import ToolkitState

logger = logging.getLogger(__name__)


class ScenarioController:
    def __init__(self,
                 view: ScenariosView,
                 toolkit_state: ToolkitState):
        self.view = view
        self.toolkit_state = toolkit_state

        # Connect signals
        self.view.radio_group.buttonToggled.connect(self.handle_scenario_selected)


    def handle_scenario_selected(self):
        for button in self.view.scenario_dict.keys():
            if button.isChecked():
                self.toolkit_state.scenario = self.view.scenario_dict[button]
                logger.info(f"{self.view.scenario_dict[button].name} has been selected as the scenario.")