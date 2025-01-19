# ingreso_clientes.py
import sqlite3
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox


class IngresoClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingreso de Clientes")
        self.setGeometry(100, 100, 600, 400)

        # Crear la base de datos si no existe
        self.crear_base_clientes()

        # Crear el formulario de ingreso de clientes
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.input_nombre_cliente = QLineEdit()
        self.input_direccion_cliente = QLineEdit()
        self.input_telefono_cliente = QLineEdit()
        self.input_email_cliente = QLineEdit()

        self.form_layout.addRow("Nombre del Cliente:", self.input_nombre_cliente)
        self.form_layout.addRow("Dirección:", self.input_direccion_cliente)
        self.form_layout.addRow("Teléfono:", self.input_telefono_cliente)
        self.form_layout.addRow("Email:", self.input_email_cliente)

        # Botón para guardar el cliente
        self.boton_guardar = QPushButton("Guardar Cliente")
        self.boton_guardar.clicked.connect(self.guardar_cliente)

        # Agregar al layout principal
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.boton_guardar)
        self.setLayout(self.layout)

    def crear_base_clientes(self):
        """
        Crear la base de datos `clientes.db` y la tabla `clientes` si no existe.
        """
        try:
            conexion = sqlite3.connect("clientes.db")
            cursor = conexion.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """)
            conexion.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo crear la base de datos: {e}")
        finally:
            conexion.close()

    def guardar_cliente(self):
        """
        Guardar un nuevo cliente en la base de datos `clientes.db`.
        """
        nombre = self.input_nombre_cliente.text()
        direccion = self.input_direccion_cliente.text()
        telefono = self.input_telefono_cliente.text()
        email = self.input_email_cliente.text()

        if not nombre or not direccion or not telefono or not email:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")
            return

        try:
            conexion = sqlite3.connect("clientes.db")
            cursor = conexion.cursor()
            cursor.execute("""
            INSERT INTO clientes (nombre, direccion, telefono, email)
            VALUES (?, ?, ?, ?)
            """, (nombre, direccion, telefono, email))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Cliente guardado correctamente.")
            self.input_nombre_cliente.clear()
            self.input_direccion_cliente.clear()
            self.input_telefono_cliente.clear()
            self.input_email_cliente.clear()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar el cliente: {e}")
        finally:
            conexion.close()
