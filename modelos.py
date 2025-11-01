"""
modelos.py contiene las entidades basicas asi como tambien las abstractas
"""
from abc import ABC, abstractmethod

#& Clase Libro
class Libro:
    def __init__(self, codigo, titulo, escritor, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.escritor = escritor
        self.genero = genero
        
        # estado por defecto
        self.disponible = True
        
    def __str__(self):
        estado = "Presente" if self.genero else "Prestado"
        return f"Titulo: {self.titulo}, escritor: {self.escritor}, genero: {self.genero} disponible: {estado}"
    
    def prestar(self):
        """ Cambia el estado a No disponible """
        self.disponible = False
    
    def devolver(self):
        """ Cambia el estado a Disponible """
        self.disponible = True
        
#& Clase Usuario
class Usuario:
    def __init__(self, clave, nombre, apellido, direccion, telefono, email, whatsapp):
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.whatsapp = whatsapp
        
        # La propiedad Libros_prestados es un diccionario {clave: libro.clave, valor: Libro}
        self.libros_prestados = {}
        
    def __str__(self):
        return f"{self.nombre} {self.apellido} (Clave: {self.clave})"
    
    def mostrar_libros(self):
        # if not self.libros_prestados:
        #     print(f"El usuario {self.nombre} {self.apellido} no tiene libros prestados")
        # else:
        #     for libro in self.libros_prestados:
        #         print(f".{libro.codigo} {libro.titulo}")
        if not self.libros_prestados:
            print(f"El usuario {self.nombre} {self.apellido} no tiene libros prestados")
        else:
            print(f"\n--- Bitácora de {self.nombre} ---")
            for clave,libro in self.libros_prestados.items():
                print(f".{clave} {libro.titulo}")

class Notificador(ABC):
    """Abstracción para cualquier servicio de notificación."""  
      
    @abstractmethod
    def enviar_mensaje(self, usuario: Usuario, mensaje: str) -> bool:
        """Contrato: Envía un mensaje a un usuario, sin especificar el canal."""
        pass

class NotificadorEmail(Notificador):
    def enviar_mensaje(self, usuario, mensaje):
        print(f'----- El mensaje "{mensaje}" ha sido enviado al email {usuario.email} -----')
        return True
    
class NotificadorWhatsapp(Notificador):
    def enviar_mensaje(self, usuario, mensaje):
        print(f'----- El mensaje "{mensaje}" ha sido enviado al Whatsapp de  {usuario.nombre} {usuario.apellido} -----')
        return True