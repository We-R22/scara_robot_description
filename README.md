# Simulación de robot tipo SCARA en Gazebo

Este paquete ROS permite simular la dinámica y el control de un robot tipo SCARA de tres grados de liberdad. Cada articulación tiene acoplado un controlador PID, que recibe comandos de posición y calcula el torque o fuerza que sebe ser aplicado para alcanzar la referenciia.
Las ganancias de control PID pueden ser ajustadas de forma independiente.

https://github.com/user-attachments/assets/322b1300-0807-4919-aeff-3ea02069a2e2

En el video se muestra el proceso de sintonización automática de las ganancias de control PID asociadas a coada controlador del robot, utilizando el paquete PID_tunig, para el seguimiento de trayectorias.
