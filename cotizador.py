# cotizador.py
import sqlite3
import random
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
    QComboBox, QMessageBox, QFormLayout, QSpinBox, QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta


class Cotizador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cotizador")
        self.setGeometry(100, 100, 600, 700)

        # Crear la base de datos si no existe
        self.crear_base_datos()

        # Diseño principal
        self.layout_principal = QVBoxLayout()

        # Número de cotización (correlativo automático)
        self.num_cotizacion = self.generar_numero_cotizacion()
        self.label_num_cotizacion = QLabel(f"Número de Cotización: {self.num_cotizacion}")
        self.layout_principal.addWidget(self.label_num_cotizacion)

        # Formulario para ingresar datos del producto
        self.formulario_layout = QFormLayout()

        # Campos del formulario
        self.input_nombre_producto = QLineEdit()
        self.input_tipo_producto = QComboBox()
        self.input_tipo_producto.addItems(["Tipo A", "Tipo B", "Tipo C",])  # Agrega más tipos según necesidad
        self.input_tiempo_validez = QSpinBox()
        self.input_tiempo_validez.setValue(30)  # Valor predeterminado: 30 días

        self.formulario_layout.addRow("Nombre del Producto:", self.input_nombre_producto)
        self.formulario_layout.addRow("Tipo de Producto:", self.input_tipo_producto)
        self.formulario_layout.addRow("Tiempo de Validez (días):", self.input_tiempo_validez)

        # Preguntar por materias primas
        self.label_materias_primas = QLabel("¿Cuántas materias primas contiene el producto?")
        self.input_num_materias_primas = QSpinBox()
        self.input_num_materias_primas.valueChanged.connect(self.actualizar_materias_primas)
        self.formulario_layout.addRow(self.label_materias_primas, self.input_num_materias_primas)

        # Tabla para mostrar las materias primas
        self.tabla_materias_primas = QTableWidget()
        self.tabla_materias_primas.setColumnCount(2)
        self.tabla_materias_primas.setHorizontalHeaderLabels(["Nombre", "Unidad de Medida"])
        self.tabla_materias_primas.horizontalHeader().setStretchLastSection(True)

        # Campos adicionales
        self.input_costo_producto = QLineEdit()
        self.input_precio_venta = QLineEdit()
        self.formulario_layout.addRow("Costo del Producto ($):", self.input_costo_producto)
        self.formulario_layout.addRow("Precio de Venta ($):", self.input_precio_venta)

        # Agregar el formulario y tabla al diseño principal
        self.layout_principal.addLayout(self.formulario_layout)
        self.layout_principal.addWidget(self.tabla_materias_primas)

        # Botón para guardar cotización
        self.boton_guardar = QPushButton("Guardar Cotización")
        self.boton_guardar.clicked.connect(self.guardar_cotizacion)
        self.layout_principal.addWidget(self.boton_guardar)

        self.setLayout(self.layout_principal)

    def crear_base_datos(self):
        """
        Crear la base de datos para guardar las cotizaciones si no existe.
        """
        conexion = sqlite3.connect("productos_cotizados.db")
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cotizaciones (
                numero_cotizacion TEXT PRIMARY KEY,
                nombre_producto TEXT,
                tipo_producto TEXT,
                tiempo_validez INTEGER,
                materias_primas TEXT,
                costo_producto REAL,
                precio_venta REAL,
                margen_bruto REAL,
                fecha_cotizacion TEXT
            )
        """)
        conexion.commit()
        conexion.close()

    def generar_numero_cotizacion(self):
        """
        Generar un número de cotización único.
        """
        return f"COT-{random.randint(1000, 9999)}"

    def actualizar_materias_primas(self):
        """
        Actualizar la tabla según el número de materias primas.
        """
        num_materias = self.input_num_materias_primas.value()
        self.tabla_materias_primas.setRowCount(num_materias)
        for i in range(num_materias):
            # Columna 1: Nombre de la materia prima (menú desplegable)
            combo_materia = QComboBox()
            combo_materia.addItems(["Materia Prima A", "Materia Prima B", "Materia Prima C"])  # Agrega más según necesidad
            self.tabla_materias_primas.setCellWidget(i, 0, combo_materia)

            # Columna 2: Unidad de medida
            combo_unidad = QComboBox()
            combo_unidad.addItems(["Pulgadas", "Centímetros", "Litros", "Estándar"])
            self.tabla_materias_primas.setCellWidget(i, 1, combo_unidad)

    def guardar_cotizacion(self):
        """
        Guardar la cotización en la base de datos.
        """
        nombre_producto = self.input_nombre_producto.text()
        tipo_producto = self.input_tipo_producto.currentText()
        tiempo_validez = self.input_tiempo_validez.value()
        costo_producto = float(self.input_costo_producto.text())
        precio_venta = float(self.input_precio_venta.text())
        margen_bruto = precio_venta - costo_producto
        fecha_cotizacion = datetime.now().strftime("%Y-%m-%d")

        # Obtener materias primas
        num_materias = self.input_num_materias_primas.value()
        materias_primas = []
        for i in range(num_materias):
            combo_materia = self.tabla_materias_primas.cellWidget(i, 0)
            combo_unidad = self.tabla_materias_primas.cellWidget(i, 1)
            materia = combo_materia.currentText() if combo_materia else ""
            unidad = combo_unidad.currentText() if combo_unidad else ""
            materias_primas.append(f"{materia} ({unidad})")
        materias_primas_str = "; ".join(materias_primas)

        # Guardar en la base de datos
        conexion = sqlite3.connect("productos_cotizados.db")
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO cotizaciones (
                numero_cotizacion, nombre_producto, tipo_producto, tiempo_validez, 
                materias_primas, costo_producto, precio_venta, margen_bruto, fecha_cotizacion
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.num_cotizacion, nombre_producto, tipo_producto, tiempo_validez, materias_primas_str, costo_producto, precio_venta, margen_bruto, fecha_cotizacion))
        conexion.commit()
        conexion.close()

        QMessageBox.information(self, "Cotización Guardada", "La cotización se ha guardado correctamente.")
        self.close()
