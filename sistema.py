

from modelos import Notificador, Usuario, Libro

class Biblioteca:
    def __init__(self, catalogo_libros: dict[Libro], registro_usuarios: dict[Usuario], notificador: Notificador):
        self.catalogo_libros = catalogo_libros
        self.registro_usuarios = registro_usuarios
        self.notificador = notificador
        
    #* ----------------------------------------------------------------------
    def prestar_libro(self, clave_usuario: str, codigo_libro: str) -> bool:
        """
        Logica para prestar libro
        
        """
        
        if clave_usuario not in self.registro_usuarios:
            print(f"Error: El usuario con clave {clave_usuario} no está registrado.")
            return False
        
        if codigo_libro not in self.catalogo_libros:
            print(f"Error: El libro con código {codigo_libro} no existe.")
            return False
        
        # Asignar objetos a variables libro y usuario para facilitar código
        libro = self.catalogo_libros [codigo_libro]
        usuario = self.registro_usuarios [clave_usuario]
        
        # 2. Verificación de Disponibilidad
        if not libro.disponible:
            print(f"Error: El libro '{libro.titulo}' ya está prestado.")
            return False
        
        print(f"El libro '{libro.titulo}' está Disponible.")
            
    
        # Llamar a libro.prestar()
        libro.prestar() 
        print(f'Gestionando Prestamo ')
        
        # Agregar libro prestado al usuario
        usuario.libros_prestados[libro.codigo] = libro
        
        
        # Enviar mensaje con self.notificador
        mensaje = f'Tu peticion para sacar el libro "{libro.titulo}" ha finalizado Exitosamente'
        self.notificador.enviar_mensaje(usuario, mensaje)
        
        return True
    
    #* ----------------------------------------------------------------------
    def devolver_libro(self, clave_usuario: str, codigo_libro: str) -> bool:
        """
        Logica para DEVOLVER libro
        
        """
        
        if clave_usuario not in self.registro_usuarios:
            print(f"Error: El usuario con clave {clave_usuario} no está registrado.")
            return False
        
        if codigo_libro not in self.catalogo_libros:
            print(f"Error: El libro con código {codigo_libro} no existe.")
            return False
        
        # Asignar objetos a variables libro y usuario para facilitar código
        libro = self.catalogo_libros [codigo_libro]
        usuario = self.registro_usuarios [clave_usuario]
        
        # Chequear si libro esta prestado al usuario
        if libro.disponible:
            print(f'Error: El libro {libro.titulo} figura como disponible')
            return False
        if codigo_libro not in usuario.libros_prestados:
            print(f'Error: No figura que el usuario {usuario.nombre} haya sacado el libro {libro.titulo}')
            return False
        
        # Llamar a libro.devolver()
        libro.devolver()
        
        # Quitar libro de usuario.libros_prestados
        usuario.libros_prestados.pop(codigo_libro)
       
        mensaje = f'Has devuelto el libro "{libro.titulo}" exitosamente!!!'
        self.notificador.enviar_mensaje(usuario, mensaje)
        return True
       
        
        
            
        