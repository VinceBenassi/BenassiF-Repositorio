// Serie Fibonacci
// 1 1 2 3 5 8 13 21 34...
// suma de los dos numeros anteriores
const fs = require('fs');

let crearSerie = (cantidad) => {
    return new Promise((resolve, reject) => {
        let fibo1 = 1;
        let fibo2 = 1;
        let serie = '';

        serie += `${fibo1}\n`;

        for(let i=2; i<=cantidad; i++){
            serie += `${fibo2}\n`;
            fibo2 = fibo1 + fibo2;
            fibo1 = fibo2 - fibo1;
        }

        // Guardar la serie en un txt mediante file system
        fs.writeFile('fibonacci.txt', serie, (err) => {
            if (err) 
                reject('Error de creación de archivo');
            else 
                resolve('El archivo fue creado con éxito');
        })
    })
}

module.exports = {
    crearSerie
}