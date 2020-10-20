# Sesión 01

## Entorno Virtual

### Creación (solo a inicio de proyecto)

Para Mac OS o Linux:

```command-line
python3 -m venv <nombre_del_entorno>
```

Para Windows

```command-line
python -m venv <nombre_del_entorno>
```

## Activar el entorno virtual

Para Mac OS o Linux:

```command-line
source <nombre_del_entorno>/bin/activate
```

Para Windows

```command-line
<nombre_del_entorno\Scripts\activate
```

## Desactivar el entorno

```command-line
deactivate
```

## Archivo de dependencias

### Para enviar las dependencias instaladas al archivo

```command-line
pip freeze > requirements.txt
```

### Para instalar todas las dependencias de un proyecto a partir de un archivo de dependencias

```command-line
pip install -r requirements.txt
```
