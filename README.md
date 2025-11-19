# UbicaditOS – Backend (FastAPI)

## Requisitos

- Python 3.10+
    
- PostgreSQL 16
    
- Virtualenv (opcional)
    
- requirements.txt ya incluido
    

## Instalación

```bash
git clone https://github.com/<user>/ubicaditos-backend.git
cd ubicaditos-backend

python3 -m venv venv
source venv/bin/activate   # Linux/macOS

pip install -r requirements.txt
```

Configura el archivo `.env`:

```
DATABASE_URL=postgresql://user:password@localhost:5432/ubicaditos
JWT_SECRET=secret123
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=120
```

Ejecuta el servidor:

```bash
uvicorn app.main:app --reload
```

Abre en el navegador:

```
http://localhost:8000/docs
```

