const serie = require('./serie');

let argv = process.argv;
valor = argv[2].split('=')[1];
console.log(valor);

let cantidad = valor;

serie.crearSerie(cantidad).then(mensaje => console.log(mensaje));