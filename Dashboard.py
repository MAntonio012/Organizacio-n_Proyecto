import os
import subprocess

class Dashboard:
    """
    Dashboard para gestionar prácticas de Programación Orientada a Objetos
    Autor: TU NOMBRE AQUÍ
    """

    def __init__(self):
        self.ruta_base = os.path.dirname(__file__)
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    def mostrar_info(self):
        print("\n==============================")
        print(" Dashboard POO ")
        print("==============================")
        print("Curso: Programación Orientada a Objetos")
        print("Autor: TU NOMBRE")
        print("Repositorio de prácticas")
        print("==============================\n")

    def mostrar_codigo(self, ruta_script):
        try:
            with open(ruta_script, 'r', encoding='utf-8') as archivo:
                codigo = archivo.read()
                print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
                print(codigo)
                return codigo
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

    def ejecutar_codigo(self, ruta_script):
        try:
            if os.name == 'nt':
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Error al ejecutar el script: {e}")

    def menu_principal(self):
        while True:
            self.mostrar_info()
            for key, unidad in self.unidades.items():
                print(f"{key} - {unidad}")
            print("0 - Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '0':
                print("Saliendo del Dashboard...")
                break
            elif opcion in self.unidades:
                ruta_unidad = os.path.join(self.ruta_base, self.unidades[opcion])
                self.menu_subcarpetas(ruta_unidad)
            else:
                print("Opción no válida.")

    def menu_subcarpetas(self, ruta_unidad):
        if not os.path.exists(ruta_unidad):
            print("La unidad no existe.")
            return

        carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        if not carpetas:
            print("No hay subcarpetas disponibles.")
            return

        while True:
            print("\n--- Subcarpetas ---")
            for i, carpeta in enumerate(carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar")

            opcion = input("Seleccione una subcarpeta: ")

            if opcion == '0':
                break
            try:
                idx = int(opcion) - 1
                if 0 <= idx < len(carpetas):
                    self.menu_scripts(os.path.join(ruta_unidad, carpetas[idx]))
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingrese un número válido.")

    def menu_scripts(self, ruta_sub):
        scripts = [f.name for f in os.scandir(ruta_sub) if f.is_file() and f.name.endswith('.py')]

        if not scripts:
            print("No hay scripts en esta carpeta.")
            return

        while True:
            print("\n--- Scripts disponibles ---")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar")

            opcion = input("Seleccione un script: ")

            if opcion == '0':
                break
            try:
                idx = int(opcion) - 1
                if 0 <= idx < len(scripts):
                    ruta_script = os.path.join(ruta_sub, scripts[idx])
                    self.mostrar_codigo(ruta_script)
                    ejecutar = input("\n¿Desea ejecutar el script? (1=Sí / 0=No): ")
                    if ejecutar == '1':
                        self.ejecutar_codigo(ruta_script)
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingrese un número válido.")


if __name__ == "__main__":
    app = Dashboard()
    app.menu_principal()