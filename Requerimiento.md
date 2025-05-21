Funcionalidades PrincipalesRegistrar Gasto:
1. Permite al usuario ingresar un nuevo gasto, especificando la cantidad, categoría (como comida, transporte, etc.) y una breve descripción opcional.
2. Guarda esta información en un archivo JSON para conservar el registro entre sesiones.

Listar Gastos:

1. Muestra todos los gastos registrados, con detalles como fecha, categoría, cantidad, y descripción.
    1.1 crear gastos
    1.2 modificar gastos 
    1.3 visualizar gastos
    1.4 eliminar gastos
2. Filtra los gastos por categoría o rango de fechas (por ejemplo, para ver solo los gastos de "transporte" o solo los del "último mes").
3. Calcular Gastos Totales y por Categoría:
4. Calcula el total de gastos diarios, semanales o mensuales, y permite ver el gasto acumulado en cada categoría.
5. Proporciona un desglose por categorías para identificar en qué áreas se gasta más.

Generar Reporte:

1. Genera un resumen o reporte de gastos en formato texto, detallando los totales diarios, semanales o mensuales, y los gastos en cada categoría.
2. El reporte puede guardarse en un archivo JSON o mostrarse en pantalla, según la preferencia del usuario.

Guardar y Cargar Datos:

1. Guarda automáticamente los registros en un archivo JSON cada vez que se registra o actualiza un gasto.
2. Carga los datos del archivo JSON al iniciar el programa, permitiendo al usuario retomar desde donde quedó en la última sesión.

Resultado esperado

Archivo principal de ejecución basado en Python.
Archivos modularizados que den funcionalidad al programa principal de Python.
Archivo JSON que almacene la información del programa en sí.