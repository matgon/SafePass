# SafePass 🚧 *(En desarrollo)*

Gestor de contraseñas seguro y sencillo, desarrollado en Python con Flask.  
Permite generar contraseñas robustas automáticamente y almacenar entradas con sitio, usuario y contraseña.

---

## 🚀 Tecnologías usadas

- Python 3.11 + Flask  
- Docker  
- Kubernetes (minikube)  
- SQLite (base de datos ligera integrada)  

---

## 📁 Estructura del proyecto

```
/SafePass
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── db.py
│   ├── utils.py
│   └── ...
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── requirements.txt
├── run.py
└── README.md
```

---

## ⚙️ Instalación y ejecución

### Requisitos previos

- Python 3.11+  
- Docker  
- Minikube (Kubernetes local)  

---

### Ejecución local sin contenedores

```bash
pip install -r requirements.txt
python run.py
```

Accede a la API en `http://localhost:5000`

---

### Uso con Docker

Construir la imagen Docker:

```bash
docker build -t safepass .
```

Ejecutar contenedor:

```bash
docker run -p 5000:5000 safepass
```

---

### Despliegue con Kubernetes

1. Iniciar minikube (si no está corriendo):

```bash
minikube start
```

2. Aplicar despliegue y servicio:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

3. Abrir servicio a otros dispositivos en la red:

```bash
minikube tunnel
kubectl get services
```

Conéctate a la IP externa en el puerto 5000 desde tu dispositivo.

---

## 🛠️ API endpoints principales

| Método | Endpoint          | Descripción                                |
|--------|-------------------|--------------------------------------------|
| GET    | `/generate?length=x`       | Genera una contraseña segura. Parámetro opcional `length` para el tamaño de la contraseña |
| POST   | `/db`             | Añade una entrada al gestor. JSON con `site`, `username`, `password` (opcional). |
| -   | -             | Más posibilidades en desarrollo |

---

## 🔒 Seguridad

- Las contraseñas se generan aleatoriamente.  
- Recomendable usar HTTPS en despliegue real.
- En proceso de desarrollo para la encriptacion en la base de datos.
