# Punto de venta

## Creacion de entorno virtual
``` bash
$ python -m virtualenv venv
```

## Activacion de entorno virtual
``` bash
$ venv\Scripts\activate.bat
```

## Instalacion de dependencias
Antes de ejecutar la aplicacion es conveniente instalar las dependencias, dado que se pueden haber agregado nuevas.

``` bash
(venv) $ pip install -r requirements.txt
```

NOTA: Recordar siempre que se agregue una dependencia nueva ejecutar:
```bash
(venv) $ pip freeze > requirements.txt
```

## Ejecucion
### 1. Primero asegurarse de tener las migraciones realizadas.
```bash
(venv) $ python manage.py makemigrations
No changes detected

(venv) $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, clientes, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

### 2. Iniciar server
```bash
(venv) $ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 02, 2023 - 14:31:37
Django version 4.2.4, using settings 'PuntoVenta.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```