Título
API de pagos de servicios.


<!--* hecho -->
Funcionalidades a desarrollar:
Realizar el versionamiento basado en la tarea desarrollada. *
Versión 1: lo desarrollado el viernes 16 de diciembre. *
Versión 2: lo solicitado en el proyecto. *
Creación de API de pagos la cual debe contener los siguientes modelos:
Services  
- Id
- Name
- Description
- Logo
Payment_user
- Id
- User_id
- Service_id
- Amount
- PaymentDate
- ExpirationDate
Expired_payments
- Id
- Pay_user_id
- Penalty_fee_amount
User
- Id
- Email
- Username
- Password 
Para la parte del login deben hacer uso de simpleJWT, y debe contar con las mismas funcionalidades que el login desarrollado en sesiones anteriores.
La API deberá contar con el CRUD para todos los modelos presentados.
La vista creada para el modelo de servicios debe ser estática, por lo que debe contar únicamente con el método GET.
La vista creada para el modelo Expired_payments, sólo debe admitir GET y POST
Añadir Paginación de 100 resultados por página.
Añadir filtro de búsqueda en Payment_user para los campos de fecha de pago y fecha de expiración.
Implementar Throttling para la vista de pagos con 1000 request por día y las demás de 2000 por día. Para las pruebas realizar con 3 y 7 respectivamente.
Generar la documentación de toda su API.


<!--! Falta -->
Deben crear roles para el uso de la API.
Anónimo: No puede acceder a la API
Usuario normal: Puede realizar POST de los pagos y hacer GET de todas las vistas.
Admin: Tiene acceso al CRUD de todas las vistas.

Si la fecha de pago supera a la fecha de expiración, se debe crear un registro automático en Expired_payments.

<h1> Integrantes </h1>
-José Quispe Reyes <br>
-Jelsin Palomino <br>

<h2> Docs Swagger </h2>
https://finalunidad5-production.up.railway.app/api/schema/swagger-ui/<br>
https://finalunidad5-production.up.railway.app/api/schema/redoc/<br>

<h2> Link Railway </h2>
https://finalunidad5-production.up.railway.app/v2/
