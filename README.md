📝 Gestor de Listas de Tareas - Django Full Stack
Este proyecto es una aplicación web funcional desarrollada con Django que permite la gestión integral de listas de tareas. 
Implementa una arquitectura cliente-servidor y sigue principios de diseño de bases de datos relacionales.

Funcionalidades
Gestión de Listas
- Crear: Generar nuevas listas de categorías (ej: Trabajo, Compra, DAW).
- Visualizar: Listado dinámico de todas las carpetas existentes.
- Eliminar: Borrado de listas con eliminación en cascada de sus tareas asociadas.

Gestión de Tareas
- Añadir: Insertar tareas dentro de una lista específica.
- Estado: Marcar tareas como completadas o pendientes (simulación de método PATCH).
- Eliminar: Quitar tareas individuales de forma permanente.

API REST - Rutas y Métodos HTTP
Se han implementado las rutas siguiendo el estándar solicitado en el proyecto:

Listas de tareas
- `GET /lists/`: Obtener todas las listas.
- `POST /lists/`: Crear una nueva lista.
- `DELETE /lists/<id>/`: Eliminar una lista.

Tareas
- `GET /lists/<id>/tasks/`: Obtener tareas de una lista.
- `POST /lists/<id>/tasks/`: Añadir tarea a la lista.
- `PATCH /lists/<id>/tasks/<id>/`: Alternar estado completada/pendiente.
- `DELETE /lists/<id>/tasks/<id>/`: Eliminar una tarea.

Tecnologías utilizadas

- Backend: Python, Django.
- Frontend: HTML5, CSS3.

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone [https://github.com/tu-usuario/nombre-repo.git](https://github.com/tu-usuario/nombre-repo.git)
   cd nombre-repo
