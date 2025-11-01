# Interfaz
"""
Incluye funciones del menú

"""

from modelos import Libro, Usuario, NotificadorEmail, NotificadorWhatsapp
from sistema import Biblioteca
import os
import time



def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')



#* --- agregar_libro() ---
def agregar_libro(biblioteca: Biblioteca):
    print("\n----- AGREGAR LIBRO -----")
    codigo = input("Código del libro: ").strip()
    titulo = input("Título: ").strip()
    escritor = input("Escritor: ").strip()
    genero = input("Genero: ").strip()
    
    # 1. Crear objeto libro
    nuevo_libro = Libro(codigo, titulo, escritor, genero)
    
    # 2.insertar en el catálogo de la biblioteca
    if codigo in biblioteca.catalogo_libros:
        print ("Error: el código ya existe.") 
    else:
        biblioteca.catalogo_libros[codigo] = nuevo_libro
        print (f"libro {titulo} agregado exitosamente a la biblioteca.")
    
    # pausa 2 segundos
    time.sleep(2)

#* --- gestionar_prestamo() ---
def gestionar_prestamo(biblioteca: Biblioteca):
    print("\n----- GESTIONAR PRESTAMO -----")
    clave = input("Clave de Usuario: ").strip()
    codigo = input("Ingrese Código del Libro: ").strip()
    
    # Llamar al metodo prestar_libro de biblioteca
    prestamo = biblioteca.prestar_libro(clave, codigo)
    
    if prestamo:
        print("Prestamo exitoso!!!!")
        pausa = input("Pulse Enter para seguir...")
    
    return
    
#* --- gestionar_devolucion() ---
def gestionar_devolucion(biblioteca: Biblioteca):
    print("\n----- GESTIONAR DEVOLUCION -----")
    clave = input("Clave de Usuario: ").strip()
    
    # Chequear si existe usuario
    if not clave in biblioteca.registro_usuarios:
        print(f'Error: La clave no existe.')
        return
    
    # Ver libros prestados a usuario
    usuario = biblioteca.registro_usuarios[clave]
    libros = list(usuario.libros_prestados.values())
    titulo = f"Libros Prestados a  {usuario.nombre}"
    
    # Chequear si hay libros, sino retorna
    if len(libros) < 1:
        pausa = input(f"\n{usuario.nombre} no tiene libros para devolver...\n Pulse enter para seguir ")
        return
    
    limpiar_pantalla()
    mostrar_libros(libros, titulo)
    
    # Que libros desea devolver
    while True:
        codigo = input("Que libro deseas devolver?(0 para salir) codigo:").strip()
        if codigo == "0":
            return
        if  not codigo in usuario.libros_prestados:
            print(f"Error: no existe libro con el código {codigo}")
            pausa = input("Pulse enter para volver al menu...")
            continue
        
        # Devolver libro
        devolucion = biblioteca.devolver_libro(clave, codigo)
        if not devolucion:
            pausa = input("Error: algo salio mal. Para voler a intentar pulse enter...")
            continue
        
        # Actualizar lista de libros
        libros = list(usuario.libros_prestados.values())
        
        if len(libros) == 0:
            pausa = input("Ya no quedan libros que devolver.\n Pulse enter para volver al menu...")
            return
        
        # Mostrar Resto de libros
        limpiar_pantalla()
        mostrar_libros(libros, titulo)  
    
    tiempo = input("Pulse una tecla...")    

#* --- mostrar_libros() --- 
def mostrar_libros(coleccion_libros: dict, titulo: str ):
    if len(coleccion_libros) < 1:
        pausa = input("La lista de libros que desea ver está vacia...\n Pulse enter para seguir ")
        return
    
    # 1. Definir los anchos fijos de las columnas (puedes ajustarlos)
    ANCHO_CODIGO = 8
    ANCHO_TITULO = 40 
    ANCHO_ESCRITOR = 25
    ANCHO_GENERO = 17
    ANCHO_ESTADO = 12
    
    espacio_titulo = (105 - len(titulo) + 2) // 2
    # estrellas = f"{'*' * espacio_titulo}"
    
    # Titulo Alineado
    titulo = (f"{'-' * espacio_titulo} {titulo} {'-' * espacio_titulo}")
    print("\n" + titulo)
    
    # 3. Encabezado Alineado
    print("="*105) # Ajusta el ancho total
    encabezado = (
        f"{'CÓDIGO': <{ANCHO_CODIGO}}" + 
        f"{'TÍTULO': <{ANCHO_TITULO}}" + 
        f"{'ESCRITOR': <{ANCHO_ESCRITOR}}" + 
        f"{'GÉNERO': <{ANCHO_GENERO}}" +
        f"{'ESTADO': <{ANCHO_ESTADO}}"
    )
    print(encabezado)
    print("="*105)
    
    # 4. Recorrer el catálogo ordenado e imprimir con formato
    for libro in coleccion_libros:
        
        # Determinar el estado para la última columna
        estado_texto = "En Biblioteca" if libro.disponible else "PRESTADO"
        
        # Generar la fila usando el formato de ancho fijo (:<ancho) para alineación a la izquierda
        fila = (
            f"{libro.codigo: <{ANCHO_CODIGO}}" +
            f"{libro.titulo[:ANCHO_TITULO-1]: <{ANCHO_TITULO}}" + 
            f"{libro.escritor[:ANCHO_ESCRITOR-1]: <{ANCHO_ESCRITOR}}" + 
            f"{libro.genero: <{ANCHO_GENERO}}" +
            f"{estado_texto: <{ANCHO_ESTADO}}"
        )
        print(fila)
        
    print("="*105)
    print(f"Total de libros: {len(coleccion_libros)}")    


#* --- mostrar_catalogo() --- 
def mostrar_catalogo(biblioteca: Biblioteca):
    catalogo = biblioteca.catalogo_libros
    
    # 2. Ordenar los libros antes de imprimirlos (por Título)
    # Usamos .values() para obtener los objetos Libro y sorted para ordenarlos.
    libros_ordenados = sorted(catalogo.values(), key=lambda libro: libro.titulo)
    
    # Llamar a mostras_libros
    mostrar_libros(libros_ordenados, "Libros en Catalogo")
    espera = input("pulse enter para continuar...")
    
    return

     
    
#* --- registrar_nuevo_usuario() ---
def registrar_nuevo_usuario(biblioteca: Biblioteca):
    """
    Captura datos del usuario, crea el objeto Usuario y lo añade al registro
    central de la Biblioteca
    """
    print("\n----- REGISTRAR NUEVO USUARIO -----")
    
    # 1. Capturar datos
    clave = input("Clave de Usuario (ej: U003): ").strip()
    
    if clave in biblioteca.registro_usuarios:
        print(f"Error: La clave de usuario {clave} ya está registrada.")
        time.sleep(2)
        return
    
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    direccion = input("Direccion: ").strip()
    telefono = input("Telefono Fijo: ").strip()
    email = input("Email: ").strip()
    whatsapp = input("Numero de Whatsapp: ").strip()
    
    # 2. Crear objeto usuario
    nuevo_usuario = Usuario(clave, nombre, apellido, direccion, telefono, email, whatsapp)
    
    # 3. Añadir usuario al registro de usuarios
    biblioteca.registro_usuarios[clave] = nuevo_usuario
    print(f"\n¡Éxito! El usuario '{nombre} {apellido}' ha sido registrado con la clave '{clave}'.")
    time.sleep(2)
    return

#* --- menu_principal() ---
def menu_principal(biblioteca: Biblioteca):
    while True:
        limpiar_pantalla()
        print(f"======== Sistema Biblioteca ========")
        print("1. Gestionar Préstamo")
        print("2. Gestionar Devolución")
        print("3. Agregar Libro al Catálogo")
        print("4. Registrar Nuevo Usuario")
        print("5. Mostrar Catálogo Completo")
        print("0. Salir")
        
        opcion = input("Seleccione una Opcion: ").strip()
        
        if opcion == '1':
            gestionar_prestamo(biblioteca)
        elif opcion == '2':
            gestionar_devolucion(biblioteca)
        elif opcion == '3':
            agregar_libro(biblioteca)
        elif opcion == '4':
            registrar_nuevo_usuario(biblioteca)
        elif opcion == '5':
            mostrar_catalogo(biblioteca)
        elif opcion == '0':
            print(f"\nSaliendo del Sistema!")
            print("----- Sistema Cerrado -----")
            break
        else:
            print("Opcion no Válida. Intente de nuevo.")

#* --- guardar_sistema() ---
def guardar_sistema(biblioteca: Biblioteca):
    """
    Función marcador de posición para la lógica de guardado.
    En el futuro, llamará a persistencia.guardar_datos().
    """
    print("\nGuardando estado del sistema...")
    # Por ahora, solo imprime y pausa
    time.sleep(1)
    print("Datos de prueba perdidos, pero estructura guardada. ¡Adiós!")