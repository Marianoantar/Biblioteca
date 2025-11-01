# Biblioteca - Python

Biblioteca es una práctica en python de un sistema de gestion de libros. En el mismo uso POO y los principios SOLID buscando las buenas prácticas para poder profesionalizar mis estudios.

El mismo consta de:

## main.py

El modulo main solamente de escarga de cargar los modulos inicializar_sistema() desde datal_loader y cargar menu_principal y guardar_sistema() desde el modulo interfaz.

## interfaz.py

Contiene todo el menu y sus funciones.

## data_loader.py

Es el modulo que se encarga de cargar los datos para inicial la biblioteca.
hasta el momento carga solamente los datos desde el codigo mismo como para probar el sistema pero en lo inmediato se cambiará implementando archivos svc.

## modelos.py

Contiene las entidades de negocio del sistema. Aquí se definen las clases básicas que representan los datos y su comportamiento intrínseco.
Este módulo es el pilar de datos del sistema. Su **única responsabilidad** es definir las **clases de las entidades** que representan los objetos físicos y lógicos de la biblioteca, así como el comportamiento básico inherente a cada uno.

**Contiene:**

* **`Libro`**: Define los atributos del libro (código, título, escritor) y sus métodos internos (`prestar()`, `devolver()`).
* **`Usuario`**: Define los datos del usuario y gestiona la lista de libros que tiene prestados.
* **`Notificador` (Abstracción)**: Define la interfaz para el envío de mensajes (como `NotificadorEmail` y `NotificadorWhatsapp`).

## sistema.py

Contiene la clase central Biblioteca, que actúa como el coordinador o capa de lógica de negocio (Business Logic Layer). Es responsable de gestionar las transacciones, aplicar las reglas de negocio y coordinar las interacciones entre Libro y Usuario.

Este módulo contiene la clase **`Biblioteca`**, que funciona como el corazón del sistema. Su responsabilidad es **coordinar** las acciones, aplicar las reglas de negocio y manejar las transacciones complejas.

**Funciones Clave:**

1. **Reglas de Negocio:** Contiene métodos como `prestar_libro()` y `devolver_libro()`, que verifican el estado del libro/usuario antes de permitir la transacción.
2. **Inyección de Dependencias:** Recibe los diccionarios de repositorios (`catalogo_libros`, `registro_usuarios`) y el objeto `Notificador` en su constructor, desacoplando la lógica de la implementación de la comunicación.
