# 💸 Proyecto Python: 
## Simulador de Gastos Diarios

Este proyecto es una aplicación de consola desarrollada en Python que permite a los usuarios gestionar sus gastos personales. Permite registrar, visualizar, filtrar, calcular totales y generar reportes. Los datos se almacenan de forma persistente en archivos JSON.

> Proyecto individual presentado como parte del entrenamiento en Python.

---

## 📑 Tabla de Contenidos

- [📋 Explicacion del Proyecto](#-explicacion-del-proyecto)
- [🧩 Funcionalidades Principales](#-funcionalidades-principales)
- [🛠️ Instalación y Configuración](#️-instalación-y-configuración)



---
## 📋 Explicación del Proyecto

- El programa inicia en la consola mostrando un menú interactivo.
- El usuario puede registrar un gasto con información como monto, categoría, cantidad y una descripción opcional.
- Todos los gastos se guardan automáticamente en un archivo JSON para asegurar la persistencia de datos.
- Desde el menú, también es posible listar todos los gastos y filtrarlos por categoría o por un rango de fechas específico.
- Se pueden calcular totales de gastos según el periodo (diario, semanal o mensual), con desglose por categorías.
- El usuario puede generar reportes que resumen sus gastos y optar por guardarlos también en un archivo.
- Todo el código está modularizado en diferentes archivos `.py` organizados dentro de carpetas, siguiendo buenas prácticas de programación.
- Este proyecto es ideal como ejercicio práctico para aprender programación en Python, manejo de archivos JSON, y lógica de control de flujo.



---

## 🧩 Funcionalidades Principales

### ✅ Registrar Gasto
- El usuario puede ingresar:
  - Monto
  - Categoría (comida, transporte, entretenimiento, otros)
  - Cantidad/unidades
  - Descripción (opcional)
- Guarda automáticamente en un archivo `JSON`.

### 📄 Listar Gastos
- Muestra todos los gastos con detalles:
  - Fecha
  - Hora
  - Categoría
  - Cantidad
  - Descripción
- Permite filtrar por:
  - Categoría
  - Rango de fechas

### 📊 Calcular Gastos Totales y por Categoría
- Cálculo automático del total de gastos por:
  - Día
  - Semana
  - Mes
- Desglose de gastos por categoría.

### 🧾 Generar Reporte
- Reporte detallado en consola o archivo `JSON` según la preferencia del usuario.
- Incluye totales diarios, semanales o mensuales por categoría.

### 💾 Guardar y Cargar Datos
- Almacena automáticamente los cambios en un archivo JSON.
- Carga datos previos al iniciar el programa para mantener el historial.

---


## 🛠️ Instalación y Configuración

### 1. Clona el repositorio o descarga los archivos

```bash
git clone https://github.com/angeldavila00/Proyecto_S2_NinoAngel.git
cd Proyecto_S2_NinoAngel
python - python3: Proyecto_Python_NinoAngel.py
pip install tabulate
link para ver el video de la explicación (AÑADE EL LINK DEL VIDEO )
