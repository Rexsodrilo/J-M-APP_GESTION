# ingreso_productos.py
import sqlite3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox


class IngresoProductos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Productos")
        self.setGeometry(100, 100, 600, 400)

        # Crear la base de datos si no existe
        self.crear_base_productos()

        # Crear el formulario de ingreso de productos
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.input_nombre_producto = QLineEdit()
        self.input_tipo_producto = QLineEdit()
        self.input_precio_producto = QLineEdit()
        self.input_descripcion_producto = QLineEdit()

        self.form_layout.addRow("Nombre del Producto:", self.input_nombre_producto)
        self.form_layout.addRow("Tipo de Producto:", self.input_tipo_producto)
        self.form_layout.addRow("Precio Unitario:", self.input_precio_producto)
        self.form_layout.addRow("Descripción:", self.input_descripcion_producto)

        # Botón para guardar el producto
        self.boton_guardar = QPushButton("Guardar Producto")
        self.boton_guardar.clicked.connect(self.guardar_producto)

        # Agregar al layout principal
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.boton_guardar)
        self.setLayout(self.layout)

    def crear_base_productos(self):
        """
        Crear la base de datos `productos.db` y la tabla `productos` si no existe.
        """
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            tipo TEXT,
            precio REAL,
            descripcion TEXT
        )
        """)
        conexion.commit()
        conexion.close()

    def guardar_producto(self):
        """
        Guardar un nuevo producto en la base de datos `productos.db`.
        """
        nombre = self.input_nombre_producto.text()
        tipo = self.input_tipo_producto.text()
        try:
            precio = float(self.input_precio_producto.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "El precio debe ser un número válido.")
            return
        descripcion = self.input_descripcion_producto.text()

        if not nombre or not tipo or not precio:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos obligatorios.")
            return

        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        cursor.execute("""
        INSERT INTO productos (nombre, tipo, precio, descripcion)
        VALUES (?, ?, ?, ?)
        """, (nombre, tipo, precio, descripcion))
        conexion.commit()
        conexion.close()

        QMessageBox.information(self, "Éxito", "Producto guardado correctamente.")
        self.input_nombre_producto.clear()
        self.input_tipo_producto.clear()
        self.input_precio_producto.clear()
        self.input_descripcion_producto.clear()
