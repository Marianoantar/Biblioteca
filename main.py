""" Modulo Main """
# main.py

from data_loader import inicializar_sistema
from interfaz import menu_principal, guardar_sistema

# Inicializar programa
if __name__ == "__main__":
    biblioteca_central = inicializar_sistema()
    menu_principal(biblioteca_central)