from tkinter import *
from Interface_functions import *

# Parametros de la ventana
window = Tk()
window.geometry('550x400')
window.config(bg = 'lightblue')
window.title('Practica - Inicio')
window.resizable(width = False, height = False)

# Etiquetas de texto
ttl = 'Sistema de Administración de Red\nPráctica 4 - Administración de Configuración\nRamirez Benitez Brayan 4CM14 2020630592'
lbl_title = Label(window, text = ttl, fg = 'black', font = ('Verdana, 15'), bg = 'lightblue')
lbl_title.place(x = 45, y = 5)

lbl_opc = Label(window, text = 'Elige una opción', fg = 'black', font = ('Verdana, 12'), bg = 'lightblue')
lbl_opc.place(x = 30, y = 100)

# Botones
btn_add = Button(window, text = 'Agregar dispositivo', font = ('Verdana, 11'), bg = 'lightgray', command = addDevice)
btn_add.config(width = 15, height = 1)
btn_add.place(x = 30, y = 130)

btn_change = Button(window, text = 'Cambiar información de dispositivo', font = ('Verdana, 11'), bg = 'lightgray', command = changeDevice)
btn_change.config(width = 30, height = 1)
btn_change.place(x = 30, y = 165)

btn_delete = Button(window, text = 'Eliminar dispositivo', font = ('Verdana, 11'), bg = 'lightgray', command = deleteDevice)
btn_delete.config(width = 15, height = 1)
btn_delete.place(x = 30, y = 200)

btn_report = Button(window, text = 'Generar reporte', font = ('Verdana, 11'), bg = 'lightgray', command = generateReport)
btn_report.config(width = 15, height = 1)
btn_report.place(x = 30, y = 235)

btn_report = Button(window, text = 'Reporte de contabilidad', font = ('Verdana, 11'), bg = 'lightgray', command = generateContReport)
btn_report.config(width = 20, height = 1)
btn_report.place(x = 30, y = 270)

btn_performance = Button(window, text = 'Administración de rendimiento', font = ('Verdana, 11'), bg = 'lightgray', command = generatePerformance)
btn_performance.config(width = 25, height = 1)
btn_performance.place(x = 30, y = 305)

btn_configu = Button(window, text = 'Administración de configuración', font = ('Verdana, 11'), bg = 'lightgray', command = configManagement)
btn_configu.config(width = 25, height = 1)
btn_configu.place(x = 30, y = 340)

window.mainloop()