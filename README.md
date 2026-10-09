# Proyecto de Automatización de Pruebas

## Propósito del proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales de una aplicación web usando Selenium y pytest. Se enfoca en validar escenarios clave del flujo de compra, como el inicio de sesión y la interacción con el carrito de compras.

## Tecnologías utilizadas

- Python 3
- Selenium
- pytest
- pytest-html
- Git
- Github
- WebDriver para Microsoft Edge

## Instalación de dependencias

1. Clonar el repositorio y entra en la carpeta del proyecto.
2. Crear y activa un entorno virtual (opcional):

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En macOS/Linux:

```bash
source .venv/bin/activate
```

3. Instalar las dependencias necesarias:

```bash
pip install selenium pytest pytest-html
```

Si en el futuro agregás un archivo `requirements.txt`, podés usar:

```bash
pip install -r requirements.txt
```

## Ejecutar las pruebas

Desde la raíz del proyecto, ejecutar:

    pytest

## Estructura del proyecto

```text
.
├── pytest.ini
├── reports/
├── tests/
│   ├── test_cart.py
│   ├── test_inventory.py
│   └── test_login.py
└── README.md
```
## Casos de prueba
- Login exitoso
- Agregar producto al carrito
- Verificar producto en el carrito


## Nota

Asegúrate de tener el WebDriver de Edge instalado y accesible en el sistema para que Selenium pueda abrir el navegador correctamente.
