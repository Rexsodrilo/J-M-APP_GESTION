from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class LogisticaWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Módulo de Logística"))
        layout.addWidget(QLabel("Inventario en Tránsito, In Situ, Comodato"))
        self.setLayout(layout)
