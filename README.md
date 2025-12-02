# PeopleOps Vacation Console

---

## 👤 Información del Estudiante

| Nombre completo                | Documento | Clan   |
|--------------------------------|----------|--------|
| Hector Hernan Rios Rodriguez   | N/A      | Turing |

---

## 📝 Descripción General

**PeopleOps Vacation Console** es una aplicación de consola desarrollada en Python para el área de People Operations de RIWI.  

Permite:

- Gestionar información de empleados y sus solicitudes de vacaciones.
- Calcular correctamente los días de vacaciones acumulados.
- Validar reglas oficiales de la empresa.
- Registrar solicitudes con estado PENDIENTE, APROBADA o RECHAZADA.
- Visualizar historial completo de vacaciones por empleado.
- Exportar reportes de solicitudes por mes y año.

Esta herramienta facilita a los administradores controlar y visualizar la información de manera clara y organizada.

---

## 🚀 Cómo Ejecutar el Programa

### Requisitos:

| Requisito              | Detalle                                             |
|------------------------|----------------------------------------------------|
| Python                 | Versión 3.10 o superior                            |
| Archivos CSV necesarios| `usuarios.csv`, `employees.csv`, `vacations.csv`  |

### Pasos para ejecutar:

1. Abrir una terminal y navegar a la carpeta del proyecto.
2. Ejecutar el archivo principal:

    ```bash
    python main.py

3. Ingresar las credenciales del administrador.

4. Acceder al menú principal para gestionar empleados y solicitudes de vacaciones.

### 📁 Estructura del Proyecto

| Archivo       | Propósito                                                                 |
|---------------|--------------------------------------------------------------------------|
| `main.py`     | Punto de entrada; gestiona el menú principal y el flujo del programa.    |
| `employees.py`| Funciones para registrar, listar y consultar empleados.                  |
| `vacations.py`| Funciones para solicitar, aprobar, rechazar vacaciones y ver historiales.|
| `usuarios.csv`| Contiene las credenciales del administrador.                             |
| `employees.csv`| Almacena la información de los empleados.                               |
| `vacations.csv`| Guarda las solicitudes de vacaciones y su estado.                        |
| `README.md`   | Documentación del proyecto.                                              |

---

### 📏 Reglas de Cálculo de Vacaciones

| Regla                   | Descripción                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Acumulación de días       | Cada empleado acumula **1.5 días** de vacaciones por mes completo trabajado.|
| Tiempo mínimo             | El empleado debe tener **al menos 6 meses completos** de trabajo.           |
| Cálculo de días           | **No se cuentan los domingos** al calcular la duración de la solicitud.     |
| Días disponibles          | `Días disponibles = (Meses trabajados × 1.5) - Días ya aprobados`.         |

---

### ⚠ Limitaciones y Mejoras Futuras

| Limitación / Mejora        | Detalle                                                                 |
|----------------------------|------------------------------------------------------------------------|
| Usuarios                   | Actualmente solo hay un administrador; se podría agregar soporte multiusuario. |
| Persistencia               | Se utilizan archivos CSV; implementar base de datos mejoraría rendimiento y seguridad. |
| Reportes                   | Actualmente son básicos; se podrían generar en PDF o Excel.            |
| Validación de fechas       | Se podrían implementar selectores de calendario o interfaz gráfica.    |
| Notificaciones             | No hay alertas automáticas de solicitudes pendientes; se puede agregar en futuras versiones. |
