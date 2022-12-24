<h1>API de pagos de servicios</h1>

Funcionalidades a desarrollar:<br/>
Realizar el versionamiento basado en la tarea desarrollada.<br/>
Versión 1: lo desarrollado el viernes 16 de diciembre.<br/>
Versión 2: lo solicitado en el proyecto.<br/>
Creación de API de pagos la cual debe contener los siguientes modelos:<br/><br/>
Services
<li>Id</li>
<li>Name</li>
<li>Description</li>
<li>Logo</li><br/>
Payment_user
<li>Id</li>
<li>User_id</li>
<li>Service_id</li>
<li>Amount</li>
<li>PaymentDate</li>
<li>ExpirationDate</li><br/>
Expired_payments
<li>Id</li>
<li>Pay_user_id</li>
<li>Penalty_fee_amount</li><br/>
User
<li>Id</li>
<li>Email</li>
<li>Username</li>
<li>Password</li><br/>
<h2>Instrucciones</h2>
Para la parte del login deben hacer uso de simpleJWT, y debe contar con las mismas funcionalidades que el login desarrollado en sesiones anteriores.<br/>
La API deberá contar con el CRUD para todos los modelos presentados.<br/>
La vista creada para el modelo de servicios debe ser estática, por lo que debe contar únicamente con el método GET.<br/>
La vista creada para el modelo Expired_payments, sólo debe admitir GET y POST.<br/>
Añadir Paginación de 100 resultados por página.<br/>
Añadir filtro de búsqueda en Payment_user para los campos de fecha de pago y fecha de expiración.<br/>
Implementar Throttling para la vista de pagos con 1000 request por día y las demás de 2000 por día. Para las pruebas realizar con 3 y 7 respectivamente.<br/>
Generar la documentación de toda su API.<br/>
Deben crear roles para el uso de la API.<br/>
Anónimo: No puede acceder a la API.<br/>
Usuario normal: Puede realizar POST de los pagos y hacer GET de todas las vistas.<br/>
Admin: Tiene acceso al CRUD de todas las vistas.<br/>
Si la fecha de pago supera a la fecha de expiración, se debe crear un registro automático en Expired_payments.<br/>

<h1> Integrantes </h1>
<a href="https://github.com/everyzzz/">José Quispe Reyes</a><br>
<a href="https://github.com/JelsinPalomino/">Jelsin Palomino</a><br>

<h2> Docs Swagger </h2>
https://finalunidad5-production.up.railway.app/api/schema/swagger-ui/<br>
https://finalunidad5-production.up.railway.app/api/schema/redoc/<br>

<h2> Link Railway </h2>
https://finalunidad5-production.up.railway.app/v2/

<h2> Link Login </h2>
https://finalunidad5-production.up.railway.app/users/login/ <br/>
<h2> Credenciales </h2>
<h3>Admin 1</h3>
email: jose@gmail.com<br/>
password: adminadmin<br/>
<h3>Admin 2</h3>
email: jtpalomino@hotmail.com<br/>
password: jelsin12<br/>