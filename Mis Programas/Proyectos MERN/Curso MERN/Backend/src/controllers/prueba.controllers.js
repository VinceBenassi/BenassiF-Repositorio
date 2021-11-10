const PruebaCtrl = {}
const Empleado = require('../models/prueba.model')

PruebaCtrl.obtener = (req, res) => {
    res.send('Está funcionando desde get')
}

PruebaCtrl.crear = async(req, res) => {
    const {nombre, apellido, salario} = req.body
    const NuevoRegistro = new Empleado({
        nombre,
        apellido,
        salario
    })
    await NuevoRegistro.save()
    res.json({
        mensaje: 'Empleado Guardado'
    })
}

PruebaCtrl.actualizar = (req, res) => {
    res.send('La actualización funciona desde put')
}

PruebaCtrl.eliminar = (req, res) => {
    res.send('Se ha eliminado correctamente desde delete')
}

module.exports = PruebaCtrl