package main
import ("fmt")

func main() {
  var edad int
  fmt.Print("Digita tu edad: ")
  fmt.Scanln(&edad)
  
  if edad <= 17 {
    fmt.Println("Eres Menor de Edad!!")
  } else if edad >= 18 && edad <= 28{
    fmt.Println("Eres un Adulto Joven!!")
  } else if edad >= 28 && edad <= 60{
    fmt.Println("Eres un Adulto!!")
  } else {
    fmt.Println("Eres un Adulto Mayor!!!")
  }

  t := 3
  r := 9

  for t < r {
    t += 1
    fmt.Println("Chuck Shurley es Dios!!")
  }

  var nombre string

  fmt.Println("Hola, cual es su nombre?")
  fmt.Print("Escriba su nombre: ")
  fmt.Scanln(&nombre)
  fmt.Println("Bienvenido a Go", nombre)
}