# **Comandos escenciales**


Correr el servidor desde esta direccion de `ubicaditos-backend`

```bash
uvicorn app.main:app --reload --port 800
```

Generar migraciones de los modelos

```bash
alembic revision --autogenerate -m "Mensagito"
```

Correr las migraciones

```bash
alembic upgrade head
```

Verificar las migraciones en PostgreSQL

```bash
sudo -u postgres psql -d ubicaditos_db
```
