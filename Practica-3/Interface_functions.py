from tkinter import *
from tkinter import ttk
from Functions import *
from GenReport import *

def addDevice():
    # Parametros de la ventana
    # window = Tk()
    window = Toplevel()
    window.geometry('500x300')
    window.config(bg = 'lightgreen')
    window.resizable(width = False, height = False)
    window.title('Practica 1 - Agregar dispositivo')

    # Etiquetas de texto
    lbl_community = Label(window, text = 'Comunidad', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_community.place(x = 30, y = 20)

    lbl_version = Label(window, text = 'Versión SNMP', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_version.place(x = 30, y = 60)

    lbl_port = Label(window, text = 'Puerto', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_port.place(x = 30, y = 100)

    lbl_ip = Label(window, text = 'IP', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_ip.place(x = 30, y = 140)

    # Cuadros de texto
    txt_community = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_community.place(x = 155, y = 20)

    txt_version = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_version.place(x = 155, y = 60)

    txt_port = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_port.place(x = 155, y = 100)

    txt_ip = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_ip.place(x = 155, y = 140)

    # Botones
    btn_add = Button(window, text = 'Agregar', font = ('Verdana, 11'), bg = 'lightgray', command = lambda:[ addAgent(txt_community.get(), txt_version.get(), txt_port.get(), txt_ip.get()), messagebox.showinfo(message = "Agente guardado exitosamente!!"), window.destroy()])
    btn_add.config(width = 15, height = 1)
    btn_add.place(x = 170, y = 180)

    window.mainloop()

def changeDevice():
    agts = showAgents()

    # Parametros de la ventana
    window = Tk()
    window.geometry('500x300')
    window.config(bg = 'lightgreen')
    window.resizable(width = False, height = False)
    window.title('Practica 1 - Cambiar información de dispositivo')

    # Etiquetas de texto
    lbl_change = Label(window, text = 'Seleccione la comunidad a modificar', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_change.place(x = 30, y = 20)

    lbl_community = Label(window, text = 'Comunidad', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_community.place(x = 30, y = 90)

    lbl_version = Label(window, text = 'Versión SNMP', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_version.place(x = 30, y = 130)

    lbl_port = Label(window, text = 'Puerto', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_port.place(x = 30, y = 170)

    lbl_ip = Label(window, text = 'IP', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_ip.place(x = 30, y = 210)

    # Cuadros de texto
    txt_community = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_community.place(x = 155, y = 90)

    txt_version = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_version.place(x = 155, y = 130)

    txt_port = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_port.place(x = 155, y = 170)

    txt_ip = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 35)
    txt_ip.place(x = 155, y = 210)
 
    # Combobox
    cmb_agent = ttk.Combobox(window, values = agts, state = 'readonly', width = 35, font = ('Verdana, 12'))
    cmb_agent.place(x = 30, y = 50)
    cmb_agent.current(0)
    
    # Mostramos los valores del dispositivo en los cuadros de texto
    def setValAgent(event):
        txt_community.delete(0, END)
        txt_version.delete(0, END)
        txt_port.delete(0, END)
        txt_ip.delete(0, END)
        agt = getAgent(cmb_agent.get())
        txt_community.insert(0, agt[0])
        txt_version.insert(0, agt[1])
        txt_port.insert(0, agt[2])
        txt_ip.insert(0, agt[3])

    cmb_agent.bind('<<ComboboxSelected>>', setValAgent)

    # Botones
    btn_add = Button(window, text = 'Cambiar', font = ('Verdana, 11'), bg = 'lightgray', command = lambda: [changeAgent(cmb_agent.get(), txt_community.get(), txt_version.get(), txt_port.get(), txt_ip.get()), messagebox.showinfo(message = "Agente modificado exitosamente!!"), window.destroy()])
    btn_add.config(width = 15, height = 1)
    btn_add.place(x = 170, y = 250)

    window.mainloop()

def deleteDevice():
    agts = showAgents()

    # Parametros de la ventana
    window = Toplevel()
    window.geometry('500x300')
    window.config(bg = 'lightgreen')
    window.resizable(width = False, height = False)
    window.title('Practica 1 - Generar reporte')

    # Etiquetas de texto
    lbl_sl = Label(window, text = 'Seleccione un dispositivo para eliminar', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_sl.place(x = 30, y = 20)

    # Combobox
    cmb_agent = ttk.Combobox(window, values = agts, state = 'readonly', width = 35, font = ('Verdana, 12'))
    cmb_agent.place(x = 30, y = 50)
    cmb_agent.current(0)

    # Botones
    btn_add = Button(window, text = 'Eliminar dispositivo', font = ('Verdana, 11'), bg = 'lightgray', command = lambda: [deleteAgent(cmb_agent.get()), messagebox.showinfo(message = "Agente eliminado exitosamente!!"), window.destroy()])
    btn_add.config(width = 15, height = 1)
    btn_add.place(x = 30, y = 100)

    window.mainloop()

def generateReport():
    agts = showAgents()

    # Parametros de la ventana
    window = Toplevel()
    window.geometry('500x300')
    window.config(bg = 'lightgreen')
    window.resizable(width = False, height = False)
    window.title('Practica 1 - Generar reporte')

    # Etiquetas de texto
    lbl_sl = Label(window, text = 'Seleccione un dispositivo', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_sl.place(x = 30, y = 20)

    # Combobox
    cmb_agent = ttk.Combobox(window, values = agts, state = 'readonly', width = 35, font = ('Verdana, 12'))
    cmb_agent.place(x = 30, y = 50)
    cmb_agent.current(0)

    # Botones
    btn_add = Button(window, text = 'Generar reporte', font = ('Verdana, 11'), bg = 'lightgray', command = lambda: [report(cmb_agent.get()), window.destroy()])
    btn_add.config(width = 15, height = 1)
    btn_add.place(x = 30, y = 100)

    window.mainloop()

def generateContReport():
    agts = showAgents()

    # Parametros de la ventana
    window = Toplevel()
    window.geometry('500x300')
    window.config(bg = 'lightgreen')
    window.resizable(width = False, height = False)
    window.title('Practica 2 - Generar reporte de contabilidad')

    # Etiquetas de texto
    lbl_sl = Label(window, text = 'Seleccione un dispositivo', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_sl.place(x = 30, y = 20)

    lbl_FI = Label(window, text = 'Fecha inicial', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_FI.place(x = 30, y = 80)

    lbl_FF = Label(window, text = 'Fecha final', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_FF.place(x = 30, y = 128)

    # Cuadros de texto
    txt_FI = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 20)
    txt_FI.place(x = 30, y = 105)

    txt_FF = Entry(window, fg = 'black', font = ('Verdana, 11'), width = 20)
    txt_FF.place(x = 30, y = 150)

    # Combobox
    cmb_agent = ttk.Combobox(window, values = agts, state = 'readonly', width = 35, font = ('Verdana, 12'))
    cmb_agent.place(x = 30, y = 50)
    cmb_agent.current(0)

    # Botones
    btn_add = Button(window, text = 'Generar reporte', font = ('Verdana, 11'), bg = 'lightgray', command = lambda: [accounting(cmb_agent.get(), txt_FI.get(), txt_FF.get()), window.destroy()])
    btn_add.config(width = 15, height = 1)
    btn_add.place(x = 30, y = 200)

    # Botones
    btn_add = Button(window, text = 'Iniciar Update', font = ('Verdana, 11'), bg = 'lightgray', command = lambda: [updateAccounting(cmb_agent.get()), messagebox.showinfo(message = "Update ejecutandose en segundo plano!!")])
    btn_add.config(width = 15, height = 1)
    btn_add.place(x = 200, y = 200)

    window.mainloop()

def generatePerformance():
    agts = showAgents()

    # Parametros de la ventana
    window = Toplevel()
    window.geometry('500x300')
    window.config(bg = 'lightgreen')
    window.resizable(width = False, height = False)
    window.title('Practica 3 - Administración de rendimiento')

    # Etiquetas de texto
    lbl_sl = Label(window, text = 'Seleccione un dispositivo', fg = 'black', font = ('Verdana, 12'), bg = 'lightgreen')
    lbl_sl.place(x = 30, y = 20)

    # Combobox
    cmb_agent = ttk.Combobox(window, values = agts, state = 'readonly', width = 35, font = ('Verdana, 12'))
    cmb_agent.place(x = 30, y = 50)
    cmb_agent.current(0)

    # Botones
    btn_upt = Button(window, text = 'Generar Updates', font = ('Verdana, 11'), bg = 'lightgray', command = lambda: [updatePerformance(cmb_agent.get()), messagebox.showinfo(message = "Update ejecutandose en segundo plano!!")])
    btn_upt.config(width = 15, height = 1)
    btn_upt.place(x = 30, y = 100)

    btn_mail = Button(window, text = 'Monitorear', font = ('Verdana, 11'), bg = 'lightgray', command = lambda: [mailPerformance(cmb_agent.get()), messagebox.showinfo(message = "Monitoreando en segundo plano!!"), window.destroy()])
    btn_mail.config(width = 15, height = 1)
    btn_mail.place(x = 30, y = 150)

    window.mainloop()

