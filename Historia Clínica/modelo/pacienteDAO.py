from tkinter import messagebox

from .conexion import ConexionDB

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB
    sql = f"""UPDATE Persona SET nombre = "{persona.nombre}, apellidoPaterno = "{persona.apellidoPAterno}", apellidoMaterno = "{persona.apellidoMaterno}", lugarNacimiento = {persona.lugarNacimiento}, ci = {persona.ci}, fechaNacimiento = "{persona.fechaNacimiento}", edad = {persona.edad}, estadoCivil = "{persona.estadoCivil}", antecedentesPatologicos = "{persona.antecedentesPatologicos}", profesion = {persona.profesion}, correo = "{persona.correo}", telefono = "{persona.telefono}", activo = 1 WHERE idPersona = {idPersona}"""

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (numeroHistoriaClinica, nombre, apellidoPaterno, apellidoMaterno, lugarNacimiento, ci, fechaNacimiento, edad, estadoCivil, antecedentesPatologicos, profesion, correo, telefono, activo) VALUES ("{persona.numeroHistoriaClinica}", "{persona.nombre}", "{persona.apellidoPaterno}", "{persona.apellidoMaterno}", {persona.lugarNacimiento}, {persona.ci}, "{persona.fechaNacimiento}", {persona.edad}, "{persona.estadoCivil}", "{persona.antecedentesPatologicos}", {persona.profesion}, "{persona.correo}", "{persona.telefono}", 1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "REGISTRAR PACIENTE"
        mensaje = "PACIENTE REGISTRADO EXITOSAMENTE"
        messagebox.showinfo(title, mensaje)
    except:
        title = "REGISTRAR PACIENTE"
        mensaje = "ERROR AL REGISTRAR PACIENTE"
        messagebox.showerror(title, mensaje)

def listar():
    conexion = ConexionDB
    listaPersona = []
    sql = "SELECT * FROM Persona WHERE activo = 1"
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = "DATOS"
        mensaje = "REGISTRO NO EXISTENTE"
        messagebox.showwarning(title, mensaje)
    return listaPersona

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f"SELECT * FROM Persona {where}"
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = "DATOS"
        mensaje = "REGISTRO NO EXISTENTE"
        messagebox.showwarning(title, mensaje)
    return listaPersona

def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "ELIMINAR PACIENTE"
        mensaje = "PACIENTE ELIMINADO EXITOSAMENTE"
        messagebox.showwarning(title, mensaje)
    except:
        title = "ELIMINAR PACIENTE"
        mensaje = "ERROR AL ELIMINAR PACIENTE"
        messagebox.showwarning(title, mensaje)

class Persona:
    def __init__(self, numeroHistoriaClinica, nombre, apellidoPaterno, apellidoMaterno, lugarNacimiento, ci, fechaNacimiento, edad, estadoCivil, antecedentesPatologicos, profesion, correo, telefono):
        self.idPersona = None
        self.numeroHistoriaClinica = numeroHistoriaClinica
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.lugarNacimiento = lugarNacimiento
        self.ci = ci
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.estadoCivil = estadoCivil
        self.antecedentesPatologicos = antecedentesPatologicos
        self.profesion = profesion
        self.correo = correo
        self.telefono = telefono
    def __str__(self):
        return f"Persona[{self.NumeroHistoriaClinica}, {self.nombre}, {self.apellidoPaterno}, {self.apellidoMaterno}, {self.ci}, {self.fechaNacimiento}, {self.edad}, {self.antecedentesPatologicos}, {self.correo}, {self.telefono}]"