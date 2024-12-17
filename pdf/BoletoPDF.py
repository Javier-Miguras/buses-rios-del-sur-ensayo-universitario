from fpdf import FPDF
import os
from datetime import datetime

class BoletoPDF(FPDF):
    def __init__(self):
        super().__init__()  # Llamada al constructor de FPDF
        # Título y footer configurados aquí
        self.title = "BOLETO DE VIAJE - BUSES RÍOS DEL SUR"
        self.footer_text = "Gracias por viajar con nosotros. ¡Buen viaje!"

    def generar_pdf(self, ticket_data):
        # Información del boleto
        codigo_venta = ticket_data[1]
        numero_pasaje = ticket_data[0]
        nombre_pasajero = ticket_data[8]
        rut_pasajero  = ticket_data[9]
        origen = ticket_data[6]
        destino = ticket_data[7]
        fecha_venta = ticket_data[3]
        fecha_salida = ticket_data[10]
        fecha_llegada = ticket_data[11]
        patente_bus = ticket_data[12]
        nombre_chofer = ticket_data[13]
        rut_chofer = ticket_data[14]
        subtotal = ticket_data[16]
        iva = ticket_data[17]
        total = ticket_data[18]

        # Ruta de la carpeta donde se guardará el PDF
        ruta_carpeta = "./tickets/"
        dateTime = datetime.now()
        nombre_archivo = f"boleto_viaje_{dateTime.strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
        ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

        # Crear la carpeta si no existe
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            print(f"Carpeta creada: {ruta_carpeta}")

        # Crear el PDF
        self.add_page()

        # Título
        self.set_font("Arial", "B", 16)
        self.set_text_color(25, 50, 150)  # Azul oscuro
        self.cell(0, 10, self.title, border=False, ln=True, align="C")
        self.ln(10)

        # Información del boleto
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, f"Código de Venta: {codigo_venta}", ln=True)
        self.cell(0, 8, f"N° Pasaje: {numero_pasaje}", ln=True)
        self.ln(5)

        # Información del pasajero
        self.set_font("Arial", "", 12)
        self.cell(0, 8, f"Nombre Pasajero: {nombre_pasajero}", ln=True)
        self.cell(0, 8, f"RUT Pasajero: {rut_pasajero}", ln=True)
        self.cell(0, 8, f"Origen: {origen}", ln=True)
        self.cell(0, 8, f"Destino: {destino}", ln=True)
        self.cell(0, 8, f"Fecha Venta: {dateTime.strftime('%Y-%m-%d')}", ln=True)
        self.cell(0, 8, f"Fecha Salida: {fecha_salida}", ln=True)
        self.cell(0, 8, f"Fecha Llegada: {fecha_llegada}", ln=True)
        self.ln(5)

        # Información del bus y chofer
        self.cell(0, 8, f"Patente Bus: {patente_bus}", ln=True)
        self.cell(0, 8, f"Nombre Chofer: {nombre_chofer}", ln=True)
        self.cell(0, 8, f"RUT Chofer: {rut_chofer}", ln=True)
        self.ln(10)

        # Totales y precios
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, f"Subtotal: ${subtotal}", ln=True)
        self.cell(0, 8, f"IVA: ${iva}", ln=True)
        self.cell(0, 8, f"TOTAL: ${total}", ln=True)

        # Pie de página
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.set_text_color(128)
        self.cell(0, 10, self.footer_text, align="C")


        # Guardar el PDF
        self.output(ruta_completa)
        print(f"Boleto generado: {ruta_completa}")
