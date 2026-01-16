# Django API Suite

Este proyecto es un Backend desarrollado con **Django** y **Django Rest Framework (DRF)** que actúa como una suite de servicios API. Incluye demostraciones de operaciones CRUD en memoria y una implementación robusta de pasarela (Gateway) para interactuar con **Firebase Realtime Database**.

El proyecto ha sido desplegado exitosamente en **PythonAnywhere**.

## 🚀 Características Principales

### 1. Demo REST API (`demo_rest_api`)
Un módulo de demostración para entender el ciclo de vida de una API RESTful.
- **CRUD Completo:** Creación, Lectura, Actualización (Total y Parcial) y Eliminación.
- **Simulación de DB:** Uso de almacenamiento en memoria con listas de Python.
- **Lógica de Negocio:**
  - Filtrado de usuarios activos (`is_active=True`).
  - Eliminación lógica (Soft Delete).
  - Validaciones de campos obligatorios.
  - Generación de UUIDs.

### 2. Landing API (`landing_api`) - Integración Firebase
Un módulo que conecta el backend de Django con la nube de Google.
- **Firebase Admin SDK:** Conexión segura mediante credenciales de servicio (Service Account).
- **Persistencia en Nube:** Lectura y escritura en **Firebase Realtime Database**.
- **Formato de Datos:** Procesamiento de fechas con formato personalizado (ej. *dd/mm/yyyy, hh:mm:ss a. m./p. m.*).

---

## 🛠 Tech Stack

* **Lenguaje:** Python 3.10+
* **Framework Web:** Django 5.x
* **API Toolkit:** Django Rest Framework (DRF)
* **Base de Datos NoSQL:** Firebase Realtime Database
* **Librería Cloud:** Firebase Admin Python SDK
* **Despliegue:** PythonAnywhere (PaaS)

---

## ⚙️ Instalación y Configuración Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/DanRCM/django_api_suite.git
cd django_api_suite
```

### 2. Crear y activar entorno virtual
```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Secretos (Importante)
Este proyecto requiere una clave privada de Firebase que no está incluida en el repositorio por seguridad.

- Crea una carpeta llamada secrets en la raíz del proyecto.

- Coloca tu archivo de credenciales de Firebase (landing-key.json) dentro de esa carpeta.

### La estructura debe verse así:
```bash
django_api_suite/
├── backend_data_server/
├── demo_rest_api/
├── landing_api/
├── secrets/
│   └── landing-key.json  <-- AQUÍ
├── manage.py
└── ...
```

### 5. Ejecutar el servidor
```bash
python manage.py runserver
```

## 🔗 Endpoints de la API

Una vez que el servidor esté corriendo (localmente en `http://127.0.0.1:8000` o en tu dominio de producción), puedes interactuar con los siguientes recursos:

### 📦 Módulo Demo (`/demo/rest/api/`)
Este módulo utiliza una lista en memoria para simular una base de datos.

| Método | Endpoint | Acción | Descripción |
| :--- | :--- | :--- | :--- |
| **GET** | `/index/` | **Listar** | Obtiene la lista de usuarios que tienen `is_active=True`. |
| **POST** | `/index/` | **Crear** | Crea un usuario nuevo. Requiere JSON con `name` y `email`. |
| **PUT** | `/<id>/` | **Reemplazar** | Reemplaza totalmente un usuario. Requiere todos los campos. |
| **PATCH** | `/<id>/` | **Actualizar** | Actualiza parcialmente los campos enviados (ej. solo el nombre). |
| **DELETE** | `/<id>/` | **Borrar** | Realiza un borrado lógico (establece `is_active=False`). |

> **Nota:** El `<id>` es un UUID generado automáticamente (ej: `550e8400-e29b...`).

### 🔥 Módulo Landing Firebase (`/landing/api/`)
Este módulo actúa como pasarela (Gateway) hacia Firebase Realtime Database.

| Método | Endpoint | Acción | Descripción |
| :--- | :--- | :--- | :--- |
| **GET** | `/index/` | **Listar Todo** | Obtiene todos los registros almacenados en la colección de Firebase. |
| **POST** | `/index/` | **Guardar** | Guarda un objeto JSON en Firebase y le adjunta automáticamente un `timestamp` con formato personalizado (ej. "a. m./p. m."). |

---

## ☁️ Despliegue en PythonAnywhere

El proyecto ha sido desplegado exitosamente en la nube utilizando la plataforma **PythonAnywhere**.

**Detalles de Configuración:**
- **Entorno Virtual:** Python 3.10
- **Archivos Estáticos:** Recolectados en la carpeta `assets/` mediante `collectstatic`.
- **Seguridad:** - `ALLOWED_HOSTS` configurado con el dominio de producción.
  - Credenciales de Firebase (`secrets/landing-key.json`) subidas manualmente al servidor (no expuestas en el repositorio).
- **WSGI:** Configuración manual para servir la aplicación Django.

**URL de Producción:**
`http://<TU-USUARIO-PYTHONANYWHERE>.pythonanywhere.com/`

---

## 📝 Autores y Créditos

- **Desarrollador:** Daniel Cortez y Sofía Izaguirre
- **Tecnologías:** Django, Django Rest Framework, Firebase Admin SDK.
- **Despliegue:** PythonAnywhere.
