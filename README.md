# Hotel Management System

Este proyecto es un sistema de gestión hotelera desarrollado en Python. Utiliza programación asincrónica para manejar reservas, clientes, habitaciones y pagos de manera eficiente.

## Funcionalidades del Proyecto

1. **Gestión de Habitaciones**  
   - Agregar habitaciones con detalles como número, tipo y precio.
   - Verificar la disponibilidad de habitaciones.

2. **Gestión de Clientes**  
   - Agregar clientes con información básica como nombre e email.
   - Almacenar y gestionar la información de los clientes.

3. **Sistema de Reservas**  
   - Crear reservas para clientes específicos, asignando habitaciones disponibles.
   - Registrar fechas de check-in y check-out.

4. **Procesamiento de Pagos**  
   - Realizar pagos de manera asincrónica para mayor eficiencia.

## Tecnologías Utilizadas
   - Python: Lenguaje de programación principal.
   - asyncio: Para manejar tareas asincrónicas.
   - datetime: Para gestionar fechas de reservas.

## Módulos personalizados:
   - hotel_management.reservations: Manejo de reservas.
   - hotel_management.customers: Gestión de clientes.
   - hotel_management.rooms: Gestión de habitaciones.
   - hotel_management.payments: Procesamiento de pagos.

## Estructura del proyecto: 
```plaintext
hotel_management_system/
│
├── hotel_management/
│   ├── __init__.py               # Inicializa el paquete
│   ├── reservations.py           # Módulo para manejar reservas
│   ├── customers.py              # Módulo para gestionar clientes
│   ├── rooms.py                  # Módulo para manejar habitaciones
│   ├── payments.py               # Módulo para procesar pagos
│
├── main.py                       # Archivo principal para ejecutar el sistema
├── README.md                     # Documentación del proyecto
```
## Ejecución del Proyecto

Sigue estos pasos para ejecutar el proyecto:

1. Clona este repositorio:
```plaintext
   git clone https://github.com/deivispuertas/hotel_py.git
```
2. Accede al repositorio clonado:
   - cd hotel_py
   - Puedes poner este comando en tu terminal cuando accedas a tu archivo
     
   ```plaintext
   code .
   ```
3. Ejecuta el programa:

   main.py

4. Resultados :
   
<div align="center">
   
![image](https://github.com/user-attachments/assets/67101321-4cee-4d5a-9a0e-363009aa77f7)

</div>



