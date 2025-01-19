import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QMessageBox
from cotizador import Cotizador  # Importar el módulo del Cotizador
from ingreso_productos import IngresoProductos # Importar el módulo de Ingresocls (clientes)
from ingreso_clientes import IngresoClientes # Importar el módulo de Ingreso (productos)
   
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión J&M")
        self.setGeometry(100, 100, 800, 600)

        # Configurar el menú principal
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Menú de Ventas
        ventas_menu = self.menu_bar.addMenu("Ventas")

        # Submenús de Clientes
        clientes_menu = QMenu("Clientes", self)
        ingreso_clientes_action = QAction("Ingreso de Clientes", self)
        ingreso_clientes_action.triggered.connect(self.abrir_ingreso_clientes)

        busqueda_clientes_action = QAction("Búsqueda de Clientes", self)
        busqueda_clientes_action.triggered.connect(self.abrir_busqueda_clientes)

        clientes_menu.addAction(ingreso_clientes_action)
        clientes_menu.addAction(busqueda_clientes_action)

        # Agregar "Clientes" al menú "Ventas"
        ventas_menu.addMenu(clientes_menu)

        # Submenú del Cotizador
        cotizador_action = QAction("Cotizador", self)
        cotizador_action.triggered.connect(self.abrir_cotizador)
        ventas_menu.addAction(cotizador_action)

        # Menú de Logística 
        logistica_menu = self.menu_bar.addMenu("Logística")
        logistica_action = QAction("invenario", self)
        logistica_action.triggered.connect(self.abrir_logistica)
        logistica_menu.addAction(logistica_action)
        
        # Menú de  Finanzas
        finanzas_menu = self.menu_bar.addMenu("Finanzas")
        finanzas_action = QAction("Finanzas", self)
        finanzas_action.triggered.connect(self.abrir_finanzas)
        finanzas_menu.addAction(finanzas_action)

        # Menú de Producción
        produccion_menu = self.menu_bar.addMenu("Producción")

        # Submenús de Producción
        ingreso_productos_action = QAction("Ingreso de Productos", self)
        ingreso_productos_action.triggered.connect(self.abrir_ingreso_productos)

        creacion_productos_action = QAction("Creación de Productos", self)
        creacion_productos_action.triggered.connect(self.abrir_creacion_productos)

        vizualizacion_exportacion_action = QAction("Visualización y Exportación", self)
        vizualizacion_exportacion_action.triggered.connect(self.abrir_visualizacion_exportacion)

        produccion_menu.addAction(ingreso_productos_action)
        produccion_menu.addAction(creacion_productos_action)
        produccion_menu.addAction(vizualizacion_exportacion_action)

    # Métodos para los submenús de Ventas
    def abrir_ingreso_clientes(self):
        """
        Acción para abrir el ingreso de clientes.
        """
        self.ingreso_clientes_window = IngresoClientes()
        self.ingreso_clientes_window.setWindowTitle("Ingreso de Clientes")
        self.ingreso_clientes_window.show()

    def abrir_busqueda_clientes(self):
        """
        Acción para abrir la búsqueda de clientes.
        """
        QMessageBox.information(self, "Búsqueda de Clientes", "Aquí se implementará la búsqueda de clientes.")

    def abrir_cotizador(self):
        """
        Acción para abrir el Cotizador.
        """
        self.cotizador_window = Cotizador()
        self.cotizador_window.show()

    # Métodos para el menú de Logística y Finanzas
    def abrir_finanzas(self):
        """
        Acción para abrir el módulo de Finanzas (marcador).
        """
        QMessageBox.information(self, "Finanzas", "Aquí se implementará la funcionalidad de Finanzas.")

    # Métodos para el menú de Producción
    def abrir_ingreso_productos(self):
        """
        Acción para abrir el ingreso de productos.
        """
        self.ingreso_productos_window = IngresoProductos()
        self.ingreso_productos_window.setWindowTitle("Ingreso de Productos")
        self.ingreso_productos_window.show()

    def abrir_creacion_productos(self):
        """
        Acción para abrir la creación de productos.
        """
        QMessageBox.information(self, "Creación de Productos", "Aquí se implementará la creación de productos.")

    def abrir_visualizacion_exportacion(self):
        """
        Acción para abrir la visualización y exportación de información.
        """
        QMessageBox.information(self, "Visualización y Exportación", "Aquí se implementará la exportación de información.")
    
    def abrir_logistica(self):
        """
        Acción para abrir el módulo de Logística (marcador).
        """
        QMessageBox.information(self, "Logística", "Aquí se implementará la funcionalidad de Logística.")
    
    def abrir_ingreso_productos(self):
        self.ingreso_productos_window = IngresoProductos()
        self.ingreso_productos_window.show()

    def abrir_ingreso_clientes(self):
        self.ingreso_clientes_window = IngresoClientes()
        self.ingreso_clientes_window.show()
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())
