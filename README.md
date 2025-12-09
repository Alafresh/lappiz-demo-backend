# Lappiz Demo Backend

Backend minimalista para el demo de registro de interesados en Lappiz LowCode.  
Está construido con FastAPI y usa persistencia en memoria para un MVP.

## Demo en producción

Backend desplegado en Render:  
[demo en render](https://lappiz-demo-backend.onrender.com/)

[Frontend desplegado en Vercel](https://lappiz-demo-frontend.vercel.app/)

## Installation

1. Clona el repositorio:

```bash
$ git clone https://github.com/Alafresh/lappiz-demo-backend.git
```

2. Crea y Activa un entorno virtual:
```bash
$ python -m venv .venv

$ source .venv/Scripts/activate
```

3. Instalar dependencias
```bash
$ pip install -r requirements.txt
```
4. Ejecuta el servidor desde afuera de la carpeta `/app`
```bash
$ uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## URLs utiles

* [API](https://lappiz-demo-backend.onrender.com/)
* [Swagger](https://lappiz-demo-backend.onrender.com/docs)
* [OpenAPI JSON](https://lappiz-demo-backend.onrender.com/openapi.json)
