import logging

from PySide6.QtWidgets import QGroupBox, QRadioButton, QVBoxLayout, QButtonGroup
from livingspacetoolkit.utils.helpers import temporary_change

logger = logging.getLogger(__name__)


class RoofingType(QGroupBox):
    def __init__(self):
        super().__init__()

        self.setTitle("Roofing Type")
        self.radio_group: QButtonGroup = QButtonGroup()

        self.radio_eco: QRadioButton = QRadioButton()
        self.radio_eco.setObjectName("radio_eco")
        self.radio_eco.setChecked(False)
        self.radio_eco.setEnabled(True)
        self.radio_eco.setText("EcoGreen")
        self.radio_group.addButton(self.radio_eco)

        self.radio_al: QRadioButton = QRadioButton()
        self.radio_al.setObjectName("radio_al")
        self.radio_al.setChecked(False)
        self.radio_al.setEnabled(True)
        self.radio_al.setText("Aluminum")
        self.radio_group.addButton(self.radio_al)

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self.radio_eco)
        layout.addWidget(self.radio_al)

        self.setLayout(layout)

    @temporary_change('radio_group', 'setExclusive', False, True)
    def default_state(self):
        logger.debug("Setting roofing type to default state.")
        self.radio_eco.setChecked(False)
        self.radio_al.setChecked(False)
        self.setEnabled(False)