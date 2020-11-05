# WASS - Sistema de asesorías académicas

## Configuración de Python
```bash
python3 -m venv env

source env/bin/activate

pip install -r requirements.txt
```

## Crear base de datos con postgresql

```bash
# Conectar con base de datos
psql postgres
create database wass;
\q 

# Vertablas

\c
\dt
```
