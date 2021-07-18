var http = require("http");

var manejador = function(solicitud, respuesta){
    console.log("Hola que tal, Eleacer!!");
    respuesta.end("Hola Mundo");
};

var servidor = http.createServer(manejador);

servidor.listen(8080);