from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class VentasWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Módulo de Ventas"))
        layout.addWidget(QLabel("Clientes y Cotizador"))
        self.setLayout(layout)
