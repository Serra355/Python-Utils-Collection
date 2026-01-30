# 🐍 Python Utility Scripts

Este repositorio contiene una colección de herramientas de consola desarrolladas en Python, diseñadas siguiendo principios de **Ingeniería de Software**, **Clean Code** y **Arquitectura Modular**.

El objetivo de este proyecto es demostrar la implementación de algoritmos lógicos, manejo de persistencia de datos y prácticas de seguridad en scripts funcionales.

## 📂 Proyectos Incluidos

### 1. 🏎️ F1 Fuel Strategy Calculator
Herramienta de simulación de estrategia de carrera para calcular la carga óptima de combustible en Fórmula 1.
- **Data-Driven:** Carga datos de telemetría (consumo por vuelta y probabilidad de Safety Car) desde una base de datos externa JSON (`circuitos.json`), desacoplando la lógica de los datos.
- **Risk Assessment:** Algoritmo que ajusta la carga de combustible basándose en modelos probabilísticos (Probabilidad de Safety Car > 50% activa estrategia de ahorro).
- **Compliance:** Incorpora automáticamente el margen obligatorio de +1.0kg para la muestra de la FIA tras la carrera.
- **Robustez:** Sistema de rutas relativas (`os.path`) para garantizar la lectura de datos en cualquier entorno de ejecución.

### 2. 🔐 Secure Password Generator (CSPRNG)
Generador de credenciales diseñado con estándares de ciberseguridad.
- **Criptografía:** Utiliza la librería `secrets` (Cryptographically Secure Pseudo-Random Number Generator) en lugar de `random` para evitar predicciones deterministas y aumentar la entropía.
- **Estadística Uniforme:** Implementación de un "pool" unificado de caracteres para eliminar sesgos de selección y garantizar la misma probabilidad para símbolos, números y letras.
- **Validación:** Control de input robusto para asegurar longitudes de contraseña seguras.

### 3. 🧮 Modular Calculator
Calculadora aritmética de consola estructurada en funciones independientes.
- **Arquitectura:** Diseño modular que separa la lógica de operación de la interfaz de usuario (Input/Output).
- **UX (Experiencia de Usuario):** Formateo inteligente de resultados para diferenciar enteros de decimales flotantes (`:g` formatting).
- **Error Handling:** Uso de bloques `try-except` para capturar excepciones de valor (`ValueError`) y prevenir cierres inesperados del programa.

---

## 🚀 Instalación y Ejecución

Asegúrate de tener **Python 3.12+** instalado en tu sistema.

1. Clona este repositorio o descarga los archivos.
2. Ejecuta los scripts desde la terminal raíz del proyecto:

```bash
# Ejecutar la Estrategia de F1
python F1-Strategy/F1-Fuel-Strategy.py

# Ejecutar el Generador de Contraseñas
python Password_Generator/main.py

# Ejecutar la Calculadora
python Calculator/main.py
```
