"""
  Taller 2 Python

  Realizado el 15 de febrero del 2024
  Desarrollador: Carlos Yazid Padilla
  Topico: Clases y objetos
"""
class Asiento:

  #  Constructor
  def __init__(self, color: str, precio : int, registro : int) -> None:
    self.color = color.lower()
    self.precio = precio
    self.registro = registro

  #  Metodos de instancia
  def cambiarColor(self, color: str) -> None:
    match color:
      case "amarillo":
        self.color = "amarillo"
      case "rojo":
        self.color = "rojo"
      case "negro":
        self.color = "negro"
      case "blanco":
        self.color = "blanco"
      case "verde":
        self.color = "verde"
  
  pass

class Motor:

  #  Constructor
  def __init__(self, numeroCilindros: int, tipo: str, registro : int) -> None:
    self.numeroCilindros = numeroCilindros
    self.tipo = tipo.lower()
    self.registro = registro

  #  Metodos de instancia
  def cambiarRegistro(self, registro: int) -> None:
    self.registro = registro

  def asignarTipo(self, tipo: str) -> None:
    if (tipo.lower() == "gasolina"):
      self.tipo = "gasolina"
    elif (tipo.lower() == "electrico"):
      self.tipo = "electrico"
  
  pass

class Auto:

  #  Atributos de clase
  cantidadCreados = 0

  #  Constructor
  def __init__(self, modelo : str, precio : int, asientos : list, marca : str, motor : Motor, registro : int) -> None:
    self.modelo = modelo
    self.precio = precio
    self.asientos = asientos
    self.marca = marca
    self.motor = motor
    self.registro = registro
    Auto.cantidadCreados += 1

  #  Metodos de instancia
  def cantidadAsientos(self) -> int:
    return len(list(filter(lambda x: not(x is None), self.asientos)))

  def verificarIntegridad(self) -> str:
    if (self.registro == self.motor.registro):
      for i in self.asientos:
        if (i is None):
            continue
        else:
          if (i.registro != self.registro):
            return "Las piezas no son originales"
      return "Auto original"
    return "Las piezas no son originales"
  
  pass
#   Anti - copy: Creado por Carlos Yazid Padilla
