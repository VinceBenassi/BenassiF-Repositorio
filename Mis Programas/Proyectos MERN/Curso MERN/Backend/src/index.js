const express = require('express')
const app = express()
const morgan = require('morgan')
const cors = require('cors')
const bodyparser = require('body-parser')
require('./database')

app.set('Port', 5000)

app.use(morgan('dev'))
//app.use(cors())
//app.use(bodyparser.urlencoded({extended: true}))
//app.use(bodyparser.json())

//Rutas
app.use('/', require('./routes/prueba.route'))

//start server

app.listen(app.get('Port'), ()=> {
    console.log('Escuchando por el puerto', app.get('Port'))
})

