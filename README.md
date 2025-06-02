# TALLER_4api
# API con Flask – Métodos HTTP
Este proyecto es una demostración de los principales métodos HTTP utilizando Python y el framework Flask. La API es sencilla y está pensada para mostrar cómo funciona cada tipo de petición.

//Requisitos://

 -Python instalado 

 -visual studio code 

 -Flask

Puedes instalar Flask con:

 # pip install flask

//Cómo ejecutar la API//

-Descarga o clona este proyecto.

-Abre una terminal dentro de la carpeta del proyecto.

-Ejecuta el siguiente comando:

   # python app.py

//Esto levantará la API en://

 # http://127.0.0.1:5000

//Rutas disponibles//
Todas las rutas usan /usuario como endpoint:

*GET /usuario → Obtiene el usuario (mock) actual

*POST /usuario → Crea un nuevo usuario (enviar JSON)

*PUT /usuario → Reemplaza completamente el usuario

*PATCH /usuario → Actualiza parcialmente los datos del usuario

*DELETE /usuario → Elimina el usuario actual

*HEAD /usuario → Retorna solo los encabezados (sin cuerpo)

*OPTIONS /usuario → Muestra los métodos HTTP permitidos

Pruebas
Puedes probar cada método usando herramientas como:

-Postman

-Insomnia

-curl (en la terminal)

Ejemplo para POST con Postman:

Método: POST

URL: http://127.0.0.1:5000/usuario

Body (JSON):

json

{
  "nombre": "Carla",
  "email": "carla@mail.com"
}

Nota final
Este proyecto fue creado con fines educativos, como parte de una investigación sobre los métodos HTTP y su uso en APIs REST.
