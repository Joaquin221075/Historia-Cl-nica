import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel
from tkinter import messagebox
from modelo.pacienteDAO import Persona, guardarDatoPaciente, listar, listarCondicion, editarDatoPaciente, eliminarPaciente
import calendar as tc
from calendar import *
from calendar import Calendar
from datetime import datetime, date

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack
        self.config(background="#0b05df")
        self.idPersona = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()

    def camposPaciente(self):

        #LABELS
        self.lblnumeroHistoriaClinica = tk.Label(self, text= "Número de Historia Clínica: ")
        self.lblnumeroHistoriaClinica.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblnumeroHistoriaClinica.grid(column=0, row=0, padx=10, pady=5)
        
        self.lblnombre = tk.Label(self, text= "Nombre: ")
        self.lblnombre.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblnombre.grid(column=0, row=1, padx=10, pady=5)

        self.lblapellidoPaterno = tk.Label(self, text= "Apellido Paterno: ")
        self.lblapellidoPaterno.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblapellidoPaterno.grid(column=0, row=2, padx=10, pady=5)

        self.lblapellidoMaterno = tk.Label(self, text= "Apellido MAterno: ")
        self.lblapellidoMaterno.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblapellidoMaterno.grid(column=0, row=3, padx=10, pady=5)

        self.lbllugarNacimiento = tk.Label(self, text= "Lugar de Nacimiento: ")
        self.lbllugarNacimiento.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lbllugarNacimiento.grid(column=0, row=4, padx=10, pady=5)

        self.lblci = tk.Label(self, text= "Cédula de Identidad: ")
        self.lblci.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblci.grid(column=0, row=5, padx=10, pady=5)

        self.lblfechaNacimiento = tk.Label(self, text= "Fecha de Nacimiento: ")
        self.lblfechaNacimiento.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblfechaNacimiento.grid(column=0, row=6, padx=10, pady=5)

        self.lbledad = tk.Label(self, text= "Edad: ")
        self.lbledad.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lbledad.grid(column=0, row=7, padx=10, pady=5)

        self.lblestadoCivil = tk.Label(self, text= "Estado Civil: ")
        self.lblestadoCivil.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblestadoCivil.grid(column=0, row=8, padx=10, pady=5)

        self.lblantecedentesPatologicos = tk.Label(self, text= "Antecedentes Patológicos: ")
        self.lblantecedentesPatologicos.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblantecedentesPatologicos.grid(column=0, row=9, padx=10, pady=5)

        self.lblprofesion = tk.Label(self, text= "Profesión/Oficio: ")
        self.lblprofesion.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblprofesion.grid(column=0, row=10, padx=10, pady=5)

        self.lblcorreo = tk.Label(self, text= "Correo Electrónico: ")
        self.lblcorreo.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblcorreo.grid(column=0, row=7, padx=11, pady=5)

        self.lbltelefono = tk.Label(self, text= "Teléfono/Celular: ")
        self.lbltelefono.config(font=("ARIAL", 15, "bold"), background="#0b05df")
        self.lbltelefono.grid(column=0, row=12, padx=10, pady=5)

        #ENTRY
        self.stringvarnumeroHistoriaClinica = tk.StringVar()
        self.entrynumeroHistoriaClinica = tk.Entry(self, textvariable=self.stringvarnumeroHistoriaClinica)
        self.entrynumeroHistoriaClinica.config(width=50, font=("ARIAL", 15))
        self.entrynumeroHistoriaClinica.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.stringvarnombre = tk.StringVar()
        self.entrynombre = tk.Entry(self, textvariable=self.stringvarnombre)
        self.entrynombre.config(width=50, font=("ARIAL", 15))
        self.entrynombre.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.stringvarapellidoPaterno = tk.StringVar()
        self.entryapellidoPaterno = tk.Entry(self, textvariable=self.stringvarapellidoPaterno)
        self.entryapellidoPaterno.config(width=50, font=("ARIAL", 15))
        self.entryapellidoPaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.stringvarapellidoMaterno = tk.StringVar()
        self.entryapellidoMaterno = tk.Entry(self, textvariable=self.stringvarapellidoMaterno)
        self.entryapellidoMaterno.config(width=50, font=("ARIAL", 15))
        self.entryapellidoMaterno.grid(column=1, row=3, padx=10, pady=5, columnspan=2)
        
        self.stringvarlugarNacimiento = tk.StringVar()
        self.entrylugarNacimiento = tk.Entry(self, textvariable=self.stringvarlugarNacimiento)
        self.entrylugarNacimiento.config(width=50, font=("ARIAL", 15))
        self.entrylugarNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.stringvarci = tk.StringVar()
        self.entryci = tk.Entry(self, textvariable=self.stringvarci)
        self.entryci.config(width=50, font=("ARIAL", 15))
        self.entryci.grid(column=1, row=5, padx=10, pady=5)

        self.stringvarfechaNacimiento = tk.StringVar()
        self.entryfechaNacimiento = tk.Entry(self, textvariable=self.stringvarfechaNacimiento)
        self.entryfechaNacimiento.config(width=50, font=("ARIAL", 15))
        self.entryfechaNacimiento.grid(column=1, row=6, padx=10, pady=5,columnspan=2)

        self.stringvaredad = tk.StringVar()
        self.entryedad = tk.Entry(self, textvariable=self.stringvaredad)
        self.entryedad.config(width=50, font=("ARIAL", 15))
        self.entryedad.grid(column=1, row=7, padx=10, pady=5,columnspan=2)

        self.stringvarestadoCivil = tk.StringVar()
        self.entryestadoCivil = tk.Entry(self, textvariable=self.stringvarestadoCivil)
        self.entryestadoCivil.config(width=50, font=("ARIAL", 15))
        self.entryestadoCivil.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        self.stringvarantecedentesPatologicos = tk.StringVar()
        self.entryantecedentesPatologicos = tk.Entry(self, textvariable=self.stringvarantecedentesPatologicos)
        self.entryantecedentesPatologicos.config(width=50, font=("ARIAL", 15))
        self.entryantecedentesPatologicos.grid(column=1, row=9, padx=10, pady=5,columnspan=2)

        self.stringvarprofesion = tk.StringVar()
        self.entryprofesion = tk.Entry(self, textvariable=self.stringvarprofesion)
        self.entryprofesion.config(width=50, font=("ARIAL", 15))
        self.entryprofesion.grid(column=1, row=10, padx=10, pady=5, columnspan=2)

        self.stringvarcorreo = tk.StringVar()
        self.entrycorreo = tk.Entry(self, textvariable=self.stringvarcorreo)
        self.entrycorreo.config(width=50, font=("ARIAL", 15))
        self.entrycorreo.grid(column=1, row=11, padx=10, pady=5,columnspan=2)

        self.stringvartelefono = tk.StringVar()
        self.entrytelefono = tk.Entry(self, textvariable=self.stringvartelefono)
        self.entrytelefono.config(width=50, font=("ARIAL", 15))
        self.entrytelefono.grid(column=1, row=12, padx=10, pady=5,columnspan=2)

        #BUTTONS
        self.buttonNuevo = tk.Button(self, text="NUEVO",command=self.habilitar)
        self.buttonNuevo.config(width=20, font=("ARIAL", 12, "bold"), foreground="#dad5d6", background="#06f60d", cursor="hand2", activebackground="#8af98d")
        self.buttonNuevo.grid(column=0, row=13, padx=10, pady=5)

        self.buttonGuardar = tk.Button(self, text="GUARDAR", command=self.guardarPaciente)
        self.buttonGuardar.config(width=20, font=("ARIAL", 12, "bold"), foreground="#dad5d6", background="#020202", cursor="hand2", activebackground="#a9a9a9")
        self.buttonGuardar.grid(column=1, row=13, padx=10, pady=5)

        self.buttonCancelar = tk.Button(self, text="CANCELAR",command=self.deshabilitar)
        self.buttonCancelar.config(width=20, font=("ARIAL", 12, "bold"), foreground="#dad5d6", background="#fa0606", cursor="hand2", activebackground="#fd8484")
        self.buttonCancelar.grid(column=2, row=13, padx=10, pady=5)
    
        #BUSCADORES DE DATOS
        #LABEL DEL BUSCADOR
        self.lblBuscarci = tk.Label(self, text="BUSCAR C.I.: ")
        self.lblBuscarci.config(ont=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblBuscarci.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarapellidoPaterno = tk.Label(self, text="BUSCAR APELLIDO PATERNO: ")
        self.lblBuscarapellidoPaterno.config(ont=("ARIAL", 15, "bold"), background="#0b05df")
        self.lblBuscarapellidoPaterno.grid(column=3, row=1, padx=10, pady=5)

        #ENTRY BUSCADOR
        self.stringvarBuscarci = tk.StringVar()
        self.entryBuscarci = tk.Entry(self, textvariable=self.stringvarBuscarci)
        self.entryBuscarci.config(width=20, font= ("ARIAL",15))
        self.entryBuscarci.grid(column=4, row=0, padx=10, pady=5)

        self.stringvarBuscarapellidoPaterno = tk.StringVar()
        self.entryBuscarapellidoPaterno = tk.Entry(self, textvariable=self.stringvarBuscarapellidoPaterno)
        self.entryBuscarapellidoPaterno.config(width=20, font= ("ARIAL",15))
        self.entryBuscarapellidoPaterno.grid(column=4, row=1, padx=10, pady=5)

        #BUTTONS BUSCADOR
        self.buttonBuscarCondicion = tk.Button(self, text="BUSCAR", command= self.buscarCondicion)
        self.buttonBuscarCondicion.config(width=20, font=("ARIAL", 12, "bold"), foreground="#8f8f91", background="#6c019f", cursor= "hand2", activebackground="#c25af4")
        self.buttonBuscarCondicion.grid(column=3, row=2, padx=10, pady=5, columnspan=1)

        self.buttonLimpiarBuscador = tk.Button(self, text="LIMPIAR", command= self.limpiarBuscador)
        self.buttonLimpiarBuscador.config(width=20, font=("ARIAL", 12, "bold"), foreground="#8f8f91", background="#6c019f", cursor= "hand2", activebackground="#c25af4")
        self.buttonLimpiarBuscador.grid(column=4, row=2, padx=10, pady=5, columnspan=1)

    def limpiarBuscador(self):
        self.stringvarapellidoPaterno.set(" ")
        self.stringvarBuscarci.set(" ")
        self.tablaPaciente()

        #BUTTON CALENDARIO
        self.buttonCalendario = tk.Button(self, text="CALENDARIO", command= self.vistaCalendario)
        self.buttonCalendario.config(width=12, font=("ARIAL", 12, "bold"), foreground="#8f8f91", background="#6c019f", cursor= "hand2", activebackground="#c25af4")
        self.buttonCalendario.grid(column=3, row=6, padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.calendario = Toplevel
        self.calendario.title("FECHA DE NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(background="#05fa17")

        self.stringvarCalendario = StringVar()
        self.calendar = tc.Calendar(self.calendario, selectmode="day", year=1900, month=1, day=1, locale = "es_US", background= "#777777", foreground = "#ffffff", headerbacground= "#b6ddfe", textvariable= self.stringvarCalendario, cursor= "hand2", date_pattern= "YYmmdd")
        self.calendar.pack(pady=22)
        self.calendar.grid(colum=0, row=1)

        #TRACE ENVIAR FECHA
        self.stringvarCalendario.trace("w", self.enviarFecha)

    def enviarFecha(self, *args):
        self.stringvarfechaNacimiento.set("" + self. stringvarCalendario.get())
        if len(self.calendar.get_date()) > 1:
            self.stringvarCalendario.trace("w", self.calcularEdad)

    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%YYmmdd")

        self.result = self.fechaActual.year - self.conver.year
        self.result -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.stringvaredad.set(self.result)

    def limpiarBuscador(self):
        self.stringvarBuscarapellidoPaterno.set(" ")
        self.stringvarBuscarci.set(" ")
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.stringvarBuscarci.get()) > 0 or len(self.stringvarBuscarapellidoPaterno.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.stringvarBuscarci.get())) > 0:
                where = "WHERE ci = " + self.stringvarBuscarci + " " #WHERE ci = 
            if (len(self.stringvarBuscarapellidoPaterno.get())) > 0:
                where = "WHERE apellidoPaterno LIKE ‘" + self.stringvarBuscarapellidoPaterno.get() + "%’ AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()

    def guardarPaciente(self):
        persona = Persona(
            self.stringvarnombre.get(), self.stringvarapellidoPaterno.get(), self.stringvarapellidoMaterno.get(), self.stringvarci.get(), self.stringvarfechaNacimiento.get(), self.stringvaredad.get(), self.stringvarantecedentesPatologicos.get(), self.stringvarcorreo.get(), self.stringvartelefono.get())

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

        guardarDatoPaciente(persona)
        self.deshabilitar()
        self.tablaPaciente()

    def habilitar(self):

        self.stringvarnumeroHistoriaClinica.set(" ")
        self.stringvarnombre.set(" ")
        self.stringvarapellidoPaterno.set(" ")
        self.stringvarapellidoMaterno.set(" ")
        self.stringvarlugarNacimiento.set(" ")
        self.stringvarci.set(" ")
        self.stringvarfechaNacimiento.set(" ")
        self.stringvaredad.set(" ")
        self.stringvarestadoCivil.set(" ")
        self.stringvarantecedentesPatologicos.set(" ")
        self.stringvarprofesion.set(" ")
        self.stringvarcorreo.set(" ")
        self.stringvartelefono.set(" ")

        self.entrynumeroHistoriaClinica.config(state="normal")
        self.entrynombre.config(state="normal")
        self.entryapellidoPaterno.config(state="normal")
        self.entryapellidoMaterno.config(state="normal")
        self.entrylugarNacimiento.config(state="normal")
        self.entryci.config(state="normal")
        self.entryfechaNacimiento.config(state="normal")
        self.entryedad.config(state="normal")
        self.entryestadoCivil.config(state="normal")
        self.entryantecedentesPatologicos.config(state="normal")
        self.entryprofesion.config(state="normal")
        self.entrycorreo.config(state="normal")
        self.entrytelefono.config(state="normal")

        self.buttonGuardar.config(state="normal")
        self.buttonCancelar.config(state="normal")
        self.buttonCalendario.config(state="normal")

    def deshabilitar(self):

        self.idPersona = None
        self.stringvarnumeroHistoriaClinica.set(" ")
        self.stringvarnombre.set(" ")
        self.stringvarapellidoPaterno.set(" ")
        self.stringvarapellidoMaterno.set(" ")
        self.stringvarlugarNacimiento.set(" ")
        self.stringvarci.set(" ")
        self.stringvarfechaNacimiento.set(" ")
        self.stringvaredad.set(" ")
        self.stringvarestadoCivil.set(" ")
        self.stringvarantecedentesPatologicos.set(" ")
        self.stringvarprofesion.set(" ")
        self.stringvarcorreo.set(" ")
        self.stringvartelefono.set(" ")

        self.entrynumeroHistoriaClinica.config(state="disabled")
        self.entrynombre.config(state="disabled")
        self.entryapellidoPaterno.config(state="disabled")
        self.entryapellidoMaterno.config(state="disabled")
        self.entrylugarNacimiento.config(state="disabled")
        self.entryci.config(state="disabled")
        self.entryfechaNacimiento.config(state="disabled")
        self.entryedad.config(state="disabled")
        self.entryestadoCivil.config(state="disabled")
        self.entryantecedentesPatologicos.config(state="disabled")
        self.entryprofesion.config(state="disabled")
        self.entrycorreo.config(state="disabled")        
        self.entrytelefono.config(state="disabled")

        self.buttonGuardar.config(state="disabled")
        self.buttonCancelar.config(state="disabled")
        self.buttonCalendario.config(state="disabled")
    
    def tablaPaciente(self, where=""):
        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            self.listaPersona.reverse()
        self.tabla = ttk.Treeview(self, column= ("numeroHistoriaClinica", "nombre", "apellidoPaterno", "apellidoMaterno", "lugarNacimiento", "ci", "fechaNacimiento", "lugarNacimiento", "edad", "estadoCivil", "antecedentesPatologicos", "profesion", "correo", "telefono"))
        self.tabla.grid(column=0, row=14, columnspan=14, sticky="nse")
        
        self.scroll = ttk.Scrollbar(self, orient= "vertical", command=self.tabla.yview)
        self.scroll.grid(row=14, column=15, sticky="nse")

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure("evenrow", background="#00fff0")

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Número de Historia Clínica")
        self.tabla.heading("#2", text="Nombre")
        self.tabla.heading("#3", text="Apellido Paterno")
        self.tabla.heading("#4", text="Apellido Materno")
        self.tabla.heading("#5", text="Lugar de Nacimiento")
        self.tabla.heading("#6", text="C.I.")
        self.tabla.heading("#7", text="Fecha de Nacimiento")
        self.tabla.heading("#8", text="Edad")
        self.tabla.heading("#9", text="Estado Civil")
        self.tabla.heading("#10", text="Antecedentes Patológicos")
        self.tabla.heading("#11", text="Profesión/Oficio")
        self.tabla.heading("#12", text="Correo Electrónico")
        self.tabla.heading("#13", text="Teléfono/Celular")

        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=100)
        self.tabla.column("#2", anchor=W, width=150)
        self.tabla.column("#3", anchor=W, width=150)
        self.tabla.column("#4", anchor=W, width=150)
        self.tabla.column("#5", anchor=W, width=300)
        self.tabla.column("#6", anchor=W, width=80)
        self.tabla.column("#7", anchor=W, width=50)
        self.tabla.column("#8", anchor=W, width=50)
        self.tabla.column("#9", anchor=W, width=100)
        self.tabla.column("#10", anchor=W, width=300)
        self.tabla.column("#11", anchor=W, width=150)
        self.tabla.column("#12", anchor=W, width=250)
        self.tabla.column("#13", anchor=W, width=150)

        for p in self.listaPersona:
            self.tabla.insert(" ", 0, text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13]), tags=("evenrow",))

        self.buttonEditarPaciente = tk.Button(self, text="EDITAR PACIENTE", command=self.editarPaciente)
        self.buttonEditarPaciente.config(width=20, font=("ARIAL", 15, "bold"), foreground="#9a9896", background="#ec7804", activebackground="#f7cf7f", cursor="hand2")
        self.buttonEditarPaciente.grid(column=0, row=15, padx=10, pady=5)

        self.buttonEliminarPaciente = tk.Button(self, text="ELIMINAR PACIENTE", command=self.eliminarDatoPaciente)
        self.buttonEliminarPaciente.config(width=20, font=("ARIAL", 15, "bold"), foreground="#9a9896", background="#fc0202", activebackground="#f96161", cursor="hand2")
        self.buttonEliminarPaciente.grid(column=1, row=15, padx=10, pady=5)

        self.buttonHistoriaClinica = tk.Button(self, text="HISTORIA CLÍNICA")
        self.buttonHistoriaClinica.config(width=20, font=("ARIAL", 15, "bold"), foreground="#9a9896", background="#4d00ff", activebackground="#834efd", cursor="hand2")
        self.buttonHistoriaClinica.grid(column=2, row=15, padx=10, pady=5)

        self.buttonEvolucion = tk.Button(self, text="EVOLUCIÓN PACIENTE")
        self.buttonEvolucion.config(width=20, font=("ARIAL", 15, "bold"), foreground="#9a9896", background="#4d00ff", activebackground="#834efd", cursor="hand2")
        self.buttonEvolucion.grid(column=3, row=15, padx=10, pady=5)

        self.buttonSalir = tk.Button(self, text="SALIR", command= self.root.destroy)
        self.buttonSalir.config(width=20, font=("ARIAL", 15, "bold"), foreground="#9a9896", background="#000000", activebackground="#807d7d", cursor="hand2")
        self.buttonSalir.grid(column=4, row=15, padx=10, pady=5)

    def editarPaciente(self):
        
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"] #Trae el ID
            self.numeroHistoriaClinicaPaciente = self.tabla.item(self.tabla.selection())["values"][0]
            self.nombrePaciente = self.tabla.item(self.tabla.selection())["values"][1]
            self.apellidoPaternoPaciente = self.tabla.item(self.tabla.selection())["values"][2]
            self.apellidoMaternoPaciente = self.tabla.item(self.tabla.selection())["values"][3]
            self.lugarNacimientoPaciente = self.tabla.item(self.tabla.selection())["values"][4]
            self.ciPaciente = self.tabla.item(self.tabla.selection())["values"][5]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())["values"][6]
            self.edadPaciente = self.tabla.item(self.tabla.selection())["values"][7]
            self.estadoCivilPaciente = self.tabla.item(self.tabla.selection())["values"][8]
            self.antecedentesPatologicosPaciente = self.tabla.item(self.tabla.selection())["values"][9]
            self.profesionPaciente = self.tabla.item(self.tabla.selection())["values"][10]
            self.correoPaciente = self.tabla.item(self.tabla.selection())["values"][11]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())["values"][12]

            self.habilitar()

            self.entrynombre.insert(0, self.nombrePaciente)
            self.entryapellidoPaterno.insert(0, self.apellidoPaternoPaciente)
            self.entryapellidoMaterno.insert(0, self.apellidoMaternoPaciente)
            self.entrylugarNacimiento.insert(0, self.lugarNacimientoPaciente)
            self.entryci.insert(0, self.ciPaciente)
            self.entryfechaNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryedad.insert(0, self.edadPaciente)
            self.entryestadoCivil.insert(0, self.estadoCivilPaciente)
            self.entryantecedentesPatologicos.insert(0, self.antecedentesPatologicosPaciente)
            self.entryprofesion.insert(0, self.profesionPaciente)
            self.entrycorreo.insert(0, self.correoPaciente)
            self.entrytelefono.insert(0, self.telefonoPaciente)
        except:
            title = "EDITAR PACIENTE"
            mensaje = "ERROR AL EDITAR PACIENTE"
            messagebox.showerror(title, mensaje)
    
    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())["text"]
            eliminarPaciente(self.idPersona)
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = "ELIMINAR PACIENTE"
            mensaje = "NO SE PUDO ELIMINAR PACIENTE"
            messagebox.showinfo(title, mensaje)