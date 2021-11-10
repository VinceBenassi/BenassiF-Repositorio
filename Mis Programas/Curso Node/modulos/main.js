// CARGA DE MÓDULO
// let dato = require('./datos');
// dato('Hola que tal Eleacer?');


// FUNCIONES DEL SISTEMA
// console.log(__filename);
// console.log(__dirname);


// MÓDULO PATH
// const path = require('path');
// const ObPath = path.parse(__filename);
// console.log(ObPath.ext);


// MÓDULO OS
// const os = require('os');
// let memoriaDisp = os.freemem();
// let memoriaTotal = os. totalmem();
// console.log(`Memoria Disponible: ${memoriaDisp}`);
// console.log(`Memoria Total del Sistema: ${memoriaTotal}`);


// MÓDULO FILE SYSTEM
// Síncrona
// const fs = require('fs');
// const archivos = fs.readdirSync('./');

// console.log(archivos);

// // Asíncrona
// fs.readdir('./', function(error, files){
//     if(error) console.log('Error', error);
//     else console.log('Resultado', files);
// })


// MÓDULO DE EVENTOS

// const EventEmitter = require('events');
// const emitter = new EventEmitter();

// // Registrar el Listener (la acción)
// emitter.on('mensajeLoger', arg => console.log('Llamado al Listener...', arg))

// // Registrar el Evento
// emitter.emit('mensajeLoger', {id:01, url:'http://benassi.org' });


// MÓDULO HTTP, el módulo mas utilizado para crear servidores web
const http = require('http');
const servidor = http.createServer((req, res) => {
    if(req.url == '/'){
        res.write('Hola Mundo');
        res.end();
    }

    if(req.url == 'api/instrumentos'){
        res.write(JSON.stringify(['guitarra', 'piano', 'bateria']));
        res.end();
    }
});

//servidor.on('connection', puerto => console.log('Nueva conexión...'))

servidor.listen(3000);
console.log('Escuchando el servidor en el puerto 3000...');