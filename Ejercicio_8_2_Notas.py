
import tkinter as tk
from tkinter import messagebox
import math


class Notas:
    def __init__(self):
        self.listaNotas = []

    def establecerNotas(self, listaNotas):
        self.listaNotas = listaNotas

    def calcularPromedio(self):
        return sum(self.listaNotas) / len(self.listaNotas)

    def calcularDesviacion(self):
        promedio = self.calcularPromedio()
        suma = 0

        for nota in self.listaNotas:
            suma += (nota - promedio) ** 2

        return math.sqrt(suma / len(self.listaNotas))

    def calcularMenor(self):
        return min(self.listaNotas)

    def calcularMayor(self):
        return max(self.listaNotas)


class VentanaPrincipal:
    def __init__(self):
        self.notas = Notas()

        self.ventana = tk.Tk()
        self.ventana.title("Notas")
        self.ventana.geometry("400x380")
        self.ventana.resizable(False, False)

        self.camposNota = []
        self.resultados = {}

        self.crearInterfaz()

        self.ventana.mainloop()

    def crearInterfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="Cálculo de notas",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        frameNotas = tk.Frame(self.ventana)
        frameNotas.pack(pady=5)

        for i in range(5):
            etiqueta = tk.Label(
                frameNotas,
                text=f"Nota {i + 1}:",
                width=10,
                anchor="e"
            )
            etiqueta.grid(row=i, column=0, padx=5, pady=4)

            campo = tk.Entry(frameNotas, width=20)
            campo.grid(row=i, column=1, padx=5, pady=4)

            self.camposNota.append(campo)

        frameBotones = tk.Frame(self.ventana)
        frameBotones.pack(pady=10)

        botonCalcular = tk.Button(
            frameBotones,
            text="Calcular",
            width=12,
            command=self.calcular
        )
        botonCalcular.grid(row=0, column=0, padx=5)

        botonLimpiar = tk.Button(
            frameBotones,
            text="Limpiar",
            width=12,
            command=self.limpiar
        )
        botonLimpiar.grid(row=0, column=1, padx=5)

        frameResultados = tk.LabelFrame(
            self.ventana,
            text="Resultados",
            padx=10,
            pady=8
        )
        frameResultados.pack(padx=15, pady=10, fill="x")

        nombres = [
            "Promedio",
            "Desviación estándar",
            "Nota mayor",
            "Nota menor"
        ]

        for i, nombre in enumerate(nombres):
            etiqueta = tk.Label(
                frameResultados,
                text=f"{nombre}:"
            )
            etiqueta.grid(row=i, column=0, sticky="w", pady=3)

            resultado = tk.Label(
                frameResultados,
                text="—",
                width=15,
                anchor="w"
            )
            resultado.grid(row=i, column=1, sticky="w", padx=10)

            self.resultados[nombre] = resultado

    def validarNotas(self):
        lista = []

        for i, campo in enumerate(self.camposNota):
            texto = campo.get().strip()

            if texto == "":
                messagebox.showwarning(
                    "Campo vacío",
                    f"Debe ingresar la Nota {i + 1}."
                )
                campo.focus()
                return None

            try:
                nota = float(texto)
            except ValueError:
                messagebox.showerror(
                    "Dato no válido",
                    f"La Nota {i + 1} debe ser un número."
                )
                campo.focus()
                return None

            lista.append(nota)

        return lista

    def calcular(self):
        lista = self.validarNotas()

        if lista is None:
            return

        self.notas.establecerNotas(lista)

        promedio = self.notas.calcularPromedio()
        desviacion = self.notas.calcularDesviacion()
        mayor = self.notas.calcularMayor()
        menor = self.notas.calcularMenor()

        self.resultados["Promedio"].config(
            text=f"{promedio:.2f}"
        )

        self.resultados["Desviación estándar"].config(
            text=f"{desviacion:.2f}"
        )

        self.resultados["Nota mayor"].config(
            text=f"{mayor:.2f}"
        )

        self.resultados["Nota menor"].config(
            text=f"{menor:.2f}"
        )

    def limpiar(self):
        for campo in self.camposNota:
            campo.delete(0, tk.END)

        for resultado in self.resultados.values():
            resultado.config(text="—")

        self.camposNota[0].focus()


class Principal:
    @staticmethod
    def main():
        VentanaPrincipal()


if __name__ == "__main__":
    Principal.main()
