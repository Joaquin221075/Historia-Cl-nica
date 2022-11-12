from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f"SELECT h.idHistoriaClinica, p.apellidoPaterno || " " || p.apellidoMaterno AS Apellidos, h.fechaHistoria, h.motivoConsulta, h.examenFisico, h.tratamiento, h.examenesComplementarios FROM historiaClinica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {id.Persona}"
    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = "LISTAR HISTORIA"
        mensaje = "ERROR AL LISTAR HISTORIA"
        messagebox.showerror(title, mensaje)
    return listaHistoria

def eliminarHistoria(idHistoriaClinica):
    conexion = ConexionDB()
    sql = f"DELETE FROM historiaClinica WHERE idHistroiaClinica = {idHistoriaClinica}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion
        title = "ELIMINAR HISTORIA CLÍNICA"
        mensaje = "HISTORIA CLÍNICA ELIMINADA CORRECTAMENTE"
        messagebox.showinfo(title, mensaje)
    except:
        title = "ELIMINAR HISTORIA CLÍNICA"
        mensaje = "ERROR AL HISTORIA CLÍNICA"
        messagebox.showerror(title, mensaje)
    
def guardarHistoria(idNumeroHistoriaClinica, idPersona, fechaHistoria, motivoConsulta, examenFisico, tratamiento, examenesComplementarios):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaClinica (idNumeroHistoriaClinica, idPersona, fechaHistoria, motivoConsulta, examenFisico,tratamiento, examenesComplementarios) VALUES ({idNumeroHistoriaClinica}, {idPersona}, "{fechaHistoria}", "{motivoConsulta}", "{examenFisico}", "{tratamiento}", "{examenesComplementarios}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = "REGISTRO DE HISTORIA CLÍNICA"
        mensaje = "HISTORIA CLÍNICA RESGISTRADA EXITOSAMENTE"
        messagebox.showinfo(title, mensaje)
    except:
        title = "REGISTRO DE HISTORIA CLÍNICA"
        mensaje = "ERROR AL REGISTRAR HISTORIA CLÍNICA"
        messagebox.showerror(title, mensaje)

def editarHistoriaClinica(fechaHistoria, motivoConsulta, examenFisico, tratamiento, examenesComplementarios, idHistoriaClinica):
       conexion = ConexionDB()
       sql = f"""UPDATE historiaClinica SET fechaHistoria = "{fechaHistoria}", motivoConsulta = "{motivoConsulta}", examenFisico = "{examenFisico}", tratamiento = "{tratamiento}", examenesComplementarios = "{examenesComplementarios}" WHERE idHistoriaClinica = {idHistoriaClinica}"""
       try:
           conexion.cursor.execute(sql)
           conexion.cerrarConexion
           title = "EDITAR HISTORIA CLÍNICA"
           mensaje = "HISTORIA CLÍNICA EDITADA EXITOSAMENTE"
           messagebox.showinfo(title, mensaje)
       except:
           title = "EDITAR HISTORIA CLÍNICA"
           mensaje = "ERROR AL EDITAR HISTORIA CLÍNICA"
           messagebox.showerror(title, mensaje)
    
class historiaClinica:
    def __init__(self, idNumeroHistoriaClinica, idPersona, fechaHistoria, motivoConsulta, examenFisico, tratamiento, examenesComplementarios):
        self.idHistoriaClinica = None
        self.idNumeroHistoriaClinica = idNumeroHistoriaClinica
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivoConsulta = motivoConsulta
        self.examenFisico = examenFisico
        self.tratamiento = tratamiento
        self.examenesComplementarios = examenesComplementarios

    def __str__(self):
        return f"historiaClinica[{self.idNumeroHistoriaClinica}, {self.idPersona}, {self.fechaHistoria}, {self.motivoConsulta}, {self.examenFisico}, {self.tratamiento}, {self.examenesComplementarios}]"