from modelos import Libro, Usuario, NotificadorEmail, NotificadorWhatsapp
from sistema import Biblioteca

#* --- cargar_datos_de_prueba() ---
def cargar_datos_de_prueba(catalogo, registro):
    """ 
    Crear instancias de prueba de Libros y Usuarios 
    """
    libro1 = Libro("COD001", "Cien Años de Soledad", "García Márquez", "Novela")
    libro2 = Libro("COD002", "Los Pilares de la tierra", "Ken Follett", "Novela historica")
    usuario1 = Usuario("U001", "Ana", "García", "Calle Falsa 123", "555-1234", "ana.g@mail.com", "555-9876")
    usuario2 = Usuario("U002", "Pedro", "Chotin", "Calle Lejana 123", "555-1234", "pedro.g@mail.com", "555-9876")

    # 3. Insertar objetos en los Repositorios
    catalogo[libro1.codigo] = libro1
    catalogo[libro2.codigo] = libro2
    registro[usuario1.clave] = usuario1
    registro[usuario2.clave] = usuario2
    
#* --- Inicialización de Repositorios y Objetos ---
def inicializar_sistema():
    """ 
    ininicaliza Repositorios
    implementa abstraccion
    crea instancias de prueba
    inserta objetos en los repositorios
    crea biblioteca e inyecta dependencias
    """
    # Repositorios (Diccionarios vacíos)
    catalogo_libros = {}
    registro_usuarios = {}

    # 1. Crear e Insertar la Implementación Concreta de la Abstracción
    notificador_email = NotificadorEmail()
    notificador_whatsapp = NotificadorWhatsapp()

    # Craga datos de prueba
    cargar_datos_de_prueba(catalogo_libros, registro_usuarios)


    # 4. Inyectar dependencias y crear la Biblioteca
    biblioteca = Biblioteca(
        catalogo_libros,
        registro_usuarios,
        notificador=notificador_whatsapp # ¡La inyección de dependencias!
    )
    return biblioteca

