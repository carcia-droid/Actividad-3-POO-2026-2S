
import tkinter as tk
from tkinter import messagebox
import math


# =========================================================
# CLASE BASE
# =========================================================

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def getVolumen(self):
        return self.volumen

    def getSuperficie(self):
        return self.superficie


# =========================================================
# CLASE CILINDRO
# =========================================================

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura

        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcularSuperficie(self):
        return (
            2 * math.pi * self.radio * self.altura
            + 2 * math.pi * self.radio ** 2
        )


# =========================================================
# CLASE ESFERA
# =========================================================

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcularSuperficie(self):
        return 4 * math.pi * self.radio ** 2


# =========================================================
# CLASE PIRAMIDE
# Se considera una pirámide de base cuadrada.
# =========================================================

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcularSuperficie(self):
        areaBase = self.base ** 2
        areaLateral = 2 * self.base * self.apotema

        return areaBase + areaLateral


# =========================================================
# CLASE CUBO
# =========================================================

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return self.lado ** 3

    def calcularSuperficie(self):
        return 6 * self.lado ** 2


# =========================================================
# CLASE PRISMA RECTANGULAR
# =========================================================

class PrismaRectangular(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

        self.volumen = self.calcularVolumen()
        self.superficie = self.calcularSuperficie()

    def calcularVolumen(self):
        return self.largo * self.ancho * self.altura

    def calcularSuperficie(self):
        return 2 * (
            self.largo * self.ancho
            + self.largo * self.altura
            + self.ancho * self.altura
        )


# =========================================================
# VENTANA BASE PARA LAS FIGURAS
# =========================================================

class VentanaFigura:
    def __init__(self, titulo, campos):
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        self.ventana.geometry("400x430")
        self.ventana.resizable(False, False)

        self.campos = {}
        self.resultadoVolumen = None
        self.resultadoSuperficie = None

        self.crearInterfaz(campos)

    def crearInterfaz(self, campos):
        titulo = tk.Label(
            self.ventana,
            text=self.ventana.title(),
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=8)

        # Imagen gráfica de la figura
        self.canvas = tk.Canvas(
            self.ventana,
            width=180,
            height=110,
            bg="white"
        )
        self.canvas.pack(pady=5)

        self.dibujarFigura()

        # Campos de entrada
        frameCampos = tk.Frame(self.ventana)
        frameCampos.pack(pady=5)

        for i, nombre in enumerate(campos):
            etiqueta = tk.Label(
                frameCampos,
                text=f"{nombre}:",
                width=12,
                anchor="e"
            )
            etiqueta.grid(row=i, column=0, padx=5, pady=4)

            campo = tk.Entry(frameCampos, width=18)
            campo.grid(row=i, column=1, padx=5, pady=4)

            self.campos[nombre] = campo

        # Botón calcular
        botonCalcular = tk.Button(
            self.ventana,
            text="Calcular",
            width=15,
            command=self.calcular
        )
        botonCalcular.pack(pady=8)

        # Resultados
        frameResultados = tk.LabelFrame(
            self.ventana,
            text="Resultados",
            padx=10,
            pady=8
        )
        frameResultados.pack(padx=20, pady=5, fill="x")

        tk.Label(
            frameResultados,
            text="Volumen (cm³):"
        ).grid(row=0, column=0, sticky="w", pady=3)

        self.resultadoVolumen = tk.Label(
            frameResultados,
            text="—"
        )
        self.resultadoVolumen.grid(
            row=0, column=1, padx=10
        )

        tk.Label(
            frameResultados,
            text="Superficie (cm²):"
        ).grid(row=1, column=0, sticky="w", pady=3)

        self.resultadoSuperficie = tk.Label(
            frameResultados,
            text="—"
        )
        self.resultadoSuperficie.grid(
            row=1, column=1, padx=10
        )

    def dibujarFigura(self):
        # Este método se redefine en cada ventana.
        pass

    def obtenerValores(self):
        valores = []

        for nombre, campo in self.campos.items():
            texto = campo.get().strip()

            if texto == "":
                messagebox.showwarning(
                    "Campo vacío",
                    f"Debe ingresar el valor de {nombre}."
                )
                campo.focus()
                return None

            try:
                valor = float(texto)
            except ValueError:
                messagebox.showerror(
                    "Dato no válido",
                    f"El valor de {nombre} debe ser numérico."
                )
                campo.focus()
                return None

            if valor <= 0:
                messagebox.showwarning(
                    "Valor no válido",
                    f"El valor de {nombre} debe ser mayor que cero."
                )
                campo.focus()
                return None

            valores.append(valor)

        return valores

    def mostrarResultados(self, figura):
        self.resultadoVolumen.config(
            text=f"{figura.getVolumen():.2f}"
        )

        self.resultadoSuperficie.config(
            text=f"{figura.getSuperficie():.2f}"
        )


# =========================================================
# VENTANA CILINDRO
# =========================================================

class VentanaCilindro(VentanaFigura):
    def __init__(self):
        super().__init__(
            "Cilindro",
            ["Radio (cm)", "Altura (cm)"]
        )

    def dibujarFigura(self):
        c = self.canvas

        c.create_oval(
            45, 15, 135, 45,
            outline="black",
            width=2
        )

        c.create_line(45, 30, 45, 85, width=2)
        c.create_line(135, 30, 135, 85, width=2)

        c.create_arc(
            45, 70, 135, 100,
            start=0, extent=180,
            style=tk.ARC,
            width=2
        )

        c.create_arc(
            45, 70, 135, 100,
            start=180, extent=180,
            style=tk.ARC,
            width=2,
            dash=(4, 3)
        )

        c.create_oval(
            45, 70, 135, 100,
            outline="black",
            width=2
        )

    def calcular(self):
        valores = self.obtenerValores()

        if valores is None:
            return

        radio, altura = valores

        figura = Cilindro(radio, altura)
        self.mostrarResultados(figura)


# =========================================================
# VENTANA ESFERA
# =========================================================

class VentanaEsfera(VentanaFigura):
    def __init__(self):
        super().__init__(
            "Esfera",
            ["Radio (cm)"]
        )

    def dibujarFigura(self):
        c = self.canvas

        c.create_oval(
            40, 10, 140, 110,
            outline="black",
            width=2
        )

        c.create_oval(
            40, 40, 140, 80,
            outline="black",
            width=1
        )

        c.create_arc(
            40, 10, 140, 110,
            start=0, extent=180,
            style=tk.ARC,
            width=2
        )

        c.create_arc(
            40, 10, 140, 110,
            start=180, extent=180,
            style=tk.ARC,
            width=2,
            dash=(4, 3)
        )

    def calcular(self):
        valores = self.obtenerValores()

        if valores is None:
            return

        radio = valores[0]

        figura = Esfera(radio)
        self.mostrarResultados(figura)


# =========================================================
# VENTANA PIRAMIDE
# =========================================================

class VentanaPiramide(VentanaFigura):
    def __init__(self):
        super().__init__(
            "Pirámide",
            ["Base (cm)", "Altura (cm)", "Apotema (cm)"]
        )

    def dibujarFigura(self):
        c = self.canvas

        c.create_polygon(
            90, 10,
            25, 85,
            155, 85,
            outline="black",
            fill="white",
            width=2
        )

        c.create_line(90, 10, 90, 85, width=1)
        c.create_line(25, 85, 90, 65, width=1)
        c.create_line(90, 65, 155, 85, width=1)

        c.create_line(
            25, 85, 90, 65,
            dash=(4, 3)
        )

    def calcular(self):
        valores = self.obtenerValores()

        if valores is None:
            return

        base, altura, apotema = valores

        figura = Piramide(base, altura, apotema)
        self.mostrarResultados(figura)


# =========================================================
# VENTANA CUBO
# =========================================================

class VentanaCubo(VentanaFigura):
    def __init__(self):
        super().__init__(
            "Cubo",
            ["Lado (cm)"]
        )

    def dibujarFigura(self):
        c = self.canvas

        c.create_polygon(
            45, 40,
            105, 40,
            135, 15,
            75, 15,
            outline="black",
            fill="white",
            width=2
        )

        c.create_polygon(
            45, 40,
            45, 95,
            105, 95,
            105, 40,
            outline="black",
            fill="white",
            width=2
        )

        c.create_polygon(
            105, 40,
            135, 15,
            135, 70,
            105, 95,
            outline="black",
            fill="white",
            width=2
        )

    def calcular(self):
        valores = self.obtenerValores()

        if valores is None:
            return

        lado = valores[0]

        figura = Cubo(lado)
        self.mostrarResultados(figura)


# =========================================================
# VENTANA PRISMA RECTANGULAR
# =========================================================

class VentanaPrisma(VentanaFigura):
    def __init__(self):
        super().__init__(
            "Prisma rectangular",
            ["Largo (cm)", "Ancho (cm)", "Altura (cm)"]
        )

    def dibujarFigura(self):
        c = self.canvas

        c.create_polygon(
            35, 40,
            105, 40,
            140, 20,
            70, 20,
            outline="black",
            fill="white",
            width=2
        )

        c.create_polygon(
            35, 40,
            35, 90,
            105, 90,
            105, 40,
            outline="black",
            fill="white",
            width=2
        )

        c.create_polygon(
            105, 40,
            140, 20,
            140, 70,
            105, 90,
            outline="black",
            fill="white",
            width=2
        )

    def calcular(self):
        valores = self.obtenerValores()

        if valores is None:
            return

        largo, ancho, altura = valores

        figura = PrismaRectangular(
            largo,
            ancho,
            altura
        )

        self.mostrarResultados(figura)


# =========================================================
# VENTANA PRINCIPAL
# =========================================================

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Figuras geométricas")
        self.ventana.geometry("350x350")
        self.ventana.resizable(False, False)

        self.crearInterfaz()

        self.ventana.mainloop()

    def crearInterfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="Figuras geométricas",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        texto = tk.Label(
            self.ventana,
            text="Seleccione una figura para calcular:"
        )
        texto.pack(pady=5)

        figuras = [
            ("Cilindro", VentanaCilindro),
            ("Esfera", VentanaEsfera),
            ("Pirámide", VentanaPiramide),
            ("Cubo", VentanaCubo),
            ("Prisma rectangular", VentanaPrisma)
        ]

        for nombre, ventanaFigura in figuras:
            boton = tk.Button(
                self.ventana,
                text=nombre,
                width=22,
                command=ventanaFigura
            )
            boton.pack(pady=4)


# =========================================================
# CLASE PRINCIPAL
# =========================================================

class Principal:
    @staticmethod
    def main():
        VentanaPrincipal()


if __name__ == "__main__":
    Principal.main()
