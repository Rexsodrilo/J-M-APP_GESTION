from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ProduccionWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Módulo de Producción"))
        layout.addWidget(QLabel("Productos y Recetario"))
        self.setLayout(layout)