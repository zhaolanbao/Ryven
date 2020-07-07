from custom_src.retain import m

from PySide2.QtWidgets import QWidget, QRadioButton, QVBoxLayout
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...


class %INPUT_WIDGET_TITLE%_PortInstanceWidget(QWidget):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(%INPUT_WIDGET_TITLE%_PortInstanceWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setStyleSheet(self.parent_node_instance.get_default_stylesheet()+'''
        QWidget {
            background: transparent;
        }
        QRadioButton {
            color: '''+self.parent_node_instance.parent_node.color.lighter().name()+''';
        }
        ''')

        self.units = 'kelvin'
        
        layout = QVBoxLayout()
        self.units_kelvin = QRadioButton('Kelvin')
        self.units_kelvin.setChecked(True)
        self.units_kelvin.toggled.connect(m(self.set_units_kelvin))
        layout.addWidget(self.units_kelvin)
        self.units_celsius = QRadioButton('Celsius')
        self.units_celsius.toggled.connect(m(self.set_units_celsius))
        layout.addWidget(self.units_celsius)
        self.units_fahrenheit = QRadioButton('Fahrenheit')
        self.units_fahrenheit.toggled.connect(m(self.set_units_fahrenheit))
        layout.addWidget(self.units_fahrenheit)
        self.setLayout(layout)
    
        self.radio_buttons = [self.units_kelvin, self.units_celsius, self.units_fahrenheit]


    def set_units_kelvin(self, checked):
        if checked:
            self.units = 'kelvin'
            self.parent_node_instance.update()

    def set_units_celsius(self, checked):
        if checked:
            self.units = 'celsius'
            self.parent_node_instance.update()

    def set_units_fahrenheit(self, checked):
        if checked:
            self.units = 'fahrenheit'
            self.parent_node_instance.update()

    def get_val(self):
        return self.units


    def get_data(self):
        data = {'units': self.units}
        return data

    def set_data(self, data):
        if data['units'] == 'kelvin':
            self.units_kelvin.setChecked(True)
            self.units_celsius.setChecked(False)
        elif data['units'] == 'celsius':
            self.units_kelvin.setChecked(False)
            self.units_celsius.setChecked(True)
        self.units = data['units']


    # remove logs and stop threads and timers here
    def removing(self):
        pass # ...
