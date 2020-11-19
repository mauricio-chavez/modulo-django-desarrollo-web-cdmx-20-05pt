# Tests scripts

## Correr pruebas sin coverage

```bash
$ python test.py
```

## Correr pruebas con coverage

```bash
$ pip install coverage
$ coverage run test.py
```

## Reporte de coverage

```bash
$ coverage run test.py
$ coverage report
```

## Reporte de coverage con statements faltantes

```bash
$ coverage run test.py
$ coverage report -m
```

## Reporte de coverage en HTML

```bash
$ coverage run test.py
$ coverage html
```
