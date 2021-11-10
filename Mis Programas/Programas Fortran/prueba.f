      program prueba
      
      integer tiempo
      integer minutos
      integer segundos

      minutos = 2
      segundos = 4

      if (minutos == segundos) then
            write(*,*) 'Es verdadero'
      else
            write(*,*) 'La condición es falsa'
      endif

      stop
      end