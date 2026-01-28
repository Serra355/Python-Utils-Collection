# Python-Utils-Collection
A collection of Python scripts demonstrating modular programming, secure random generation, and input validation logic.

# 🐍 Python Utility Scripts

Este repositorio contiene una colección de herramientas de consola desarrolladas en Python, diseñadas siguiendo principios de **Clean Code**, **Modularidad** y **Seguridad**.

## 📂 Proyectos Incluidos

### 1. Secure Password Generator (CSPRNG)
Generador de contraseñas de alta entropía diseñado para ciberseguridad.
- **Tecnología:** Utiliza la librería `secrets` (Cryptographically Secure Pseudo-Random Number Generator) en lugar de `random` para evitar predicciones deterministas.
- **Lógica:** Implementación de pool unificado de caracteres para asegurar una distribución estadística uniforme.
- **Seguridad:** Validación robusta de inputs para asegurar longitudes mínimas seguras.

### 2. Modular Calculator
Calculadora aritmética de consola estructurada en funciones independientes.
- **Arquitectura:** Diseño modular para facilitar la escalabilidad y mantenimiento.
- **UX:** Formateo de salida inteligente (enteros vs floats) y bucle de ejecución continuo.
- **Robustez:** Manejo de excepciones (`try-except`) para prevenir cierres inesperados por `ValueError`.

## 🚀 Cómo ejecutar
Asegúrate de tener Python 3.14.2 instalado.

```bash
# Para el generador de contraseñas
python Password-Generator/main.py

# Para la calculadora
python Calculator/main.py
