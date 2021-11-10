const mongoose = require('mongoose')

// dirección BD
URI = ('mongodb://localhost:27017/prueba')

mongoose.connect(URI, {
    useNewUrlParser:true,
    useUnifiedTopology: true,
    //useCreateIndex:true,
    //useFindAndModify:false
}).then(db => console.log('La base de datos está conectada'))
  .catch(error => console.log(error))

module.exports = mongoose