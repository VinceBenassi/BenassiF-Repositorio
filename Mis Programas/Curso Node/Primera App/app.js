function saludar(numero1, numero2){
    console.log(numero1 * numero2);
}

saludar(16, 4);

nombre = "Javier";
console.log(nombre);

// const crea variables utilizadas para el uso 
// de solo lectura, no se puede mutar/cambiar de valor
const nombre2 = "Andrés";

// let es como usar var pero actualizado
let edad = 21;
console.log(nombre2);
console.log(edad);

// Funciones Flecha
// Funciones en ES5
const años = [1999, 2006, 2011];

var edad5 = años.map(function(valor){
    return 2021 - valor;
});
console.log(edad5);

// Funciones Flecha en ES6
let edad6 = años.map(valor => 2021 - valor);
console.log(edad6);

// Funciones Callback
function Multiplicar(num1, num2, callback){
    let resultado = num1 * num2;
    callback(resultado);
}

function Resultado(res){
    console.log(res);
}

Multiplicar(4, 5, Resultado);

// Promesas
const AdvertenciaDelay = new Promise((resolve, reject) => {
    setTimeout(() => {
        if(true)
            resolve('Esto se ejecutará después de 3 segundos')
        else
            reject("Hubo un error");
    }, 3000);
});

AdvertenciaDelay
    .then( mensaje => {
        console.log(mensaje);
    })
    .catch(error => {
        console.log(error);
    })

// Funciones Async y Await
// Async: función asíncrona; await: espera

function Advertencia(){
    return new Promise((resolve, reject)=> {
        setTimeout(() => {
            if(true)
                resolve('Esto se ejecutará después de 4 segundos')
            else
                reject("Hubo un error");
        }, 4000);
    });
}

// la función async devuelve una promesa
async function llamadaAsincrona(){
    console.log("Llamando... ");
    const resultado = await Advertencia();
    console.log(resultado);
}

llamadaAsincrona();