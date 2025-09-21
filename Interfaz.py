import tkinter as tk
import webbrowser
import mysql.connector
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from tabulate import tabulate

root = tk.Tk()
root.geometry('800x550')
root.title("Northwind Management")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)


# Añadir las pestañas al Notebook
notebook.add(tab1, text="Propiedades")
notebook.add(tab2, text="Agentes")
notebook.add(tab3, text="Clientes")
notebook.add(tab4, text="Ventas")
notebook.add(tab5, text="Ofifinas")


# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

#Funciones
def Guardar():
    messagebox.showinfo("Guardado","Haz guardado correctamente los datos")
def Actualizar():
    messagebox.showinfo("Actualizado","Haz actualizado los datos")
def Eliminar():
    messagebox.showinfo("Eliminado","Haz elminado correctamente los datos")
def Limpiar():
    messagebox.showinfo("Limpiado","Haz limpiado la información de los campos")
def abrir():
    webbrowser.open_new("https://www.youtube.com/watch?v=NGbUsgG_48k&list=RDNGbUsgG_48k&start_radio=1&pp=ygUIbWFtYSBjcnmgBwE%3D")

# CONTENIDO DE LA PESTAÑA 1 (PRODUCTS)
# Título
titulo = tk.Label(tab1,
                  text="Gestiòn de Propiedades",
                  font=("Times New Roman", 16, "bold"),
                  fg="black")
titulo.pack(pady=20)

# Frame para contener el formulario
form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: ProductID
tk.Label(form_frame, text="PropertyID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: ProductName
tk.Label(form_frame, text="Adress:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
ProductName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ProductName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: SupplierID
tk.Label(form_frame, text="Price:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
SupplierID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
SupplierID.grid(row=3, column=1, sticky="w", pady=10)

# Frame para botones
button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=Guardar)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10,command=Actualizar)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10,command=Eliminar)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10,command=Limpiar)
btn_clear.pack(side=tk.LEFT, padx=5)

# CONTENIDO DE LA PESTAÑA 2 (CUSTOMERS)
titulo2 = tk.Label(tab2, text="Gestiòn de agentes", font=("Arial", 16, "bold"), fg="green")
titulo2.pack(pady=20)

form_frame = tk.Frame(tab2)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1: CustomerID
tk.Label(form_frame, text="AgentID :", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: CustomerName
tk.Label(form_frame, text="Name:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: ContactName
tk.Label(form_frame, text="Phone:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
ContactName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
ContactName.grid(row=3, column=1, sticky="w", pady=10)

button_frame = tk.Frame(tab2)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10,command=Guardar)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10,command=Actualizar)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10,command=Eliminar)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10,command=Limpiar)
btn_clear.pack(side=tk.LEFT, padx=5)

# PESTAÑA 3 (EMPLOYEES)
titulo3 = tk.Label(tab3, text="Gestiòn de clientes", font=("Arial", 16, "bold"), fg="red")
titulo3.pack(pady=20)

form_frame = tk.Frame(tab3)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1:
tk.Label(form_frame, text="ClientID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2:
tk.Label(form_frame, text="Name:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="Phone:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=3, column=1, sticky="w", pady=10)


button_frame = tk.Frame(tab3)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)



#PESTAÑA 4 ()
titulo4 = tk.Label(tab4, text="Gestiòn de ventas", font=("Times New Roman",16,"bold"),fg="black")
titulo4.pack(pady=20)

form_frame = tk.Frame(tab4)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1:
tk.Label(form_frame, text="SaleID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2:
tk.Label(form_frame, text="PropertyID:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3:
tk.Label(form_frame, text="ClientID:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=3, column=1, sticky="w", pady=10)

button_frame = tk.Frame(tab4)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)

#PESTAÑA 5 ()
titulo5 = tk.Label(tab5, text="Gestiòn de oficinas", font=("Times New Roman", 16,"bold"), fg="black")
titulo5.pack(pady=20)

form_frame = tk.Frame(tab5)
form_frame.pack(pady=20, anchor="w", padx=50)

# Fila 1:
tk.Label(form_frame, text="OfficeID:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerID = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerID.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2:
tk.Label(form_frame, text="Location:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=2, column=1, sticky="w", pady=10)

tk.Label(form_frame, text="Phone:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
CustomerName = tk.Entry(form_frame, width=25, font=("Arial", 12), relief="solid", bd=1)
CustomerName.grid(row=3, column=1, sticky="w", pady=10)

button_frame = tk.Frame(tab5)
button_frame.pack(pady=20)

# Botones de acción
btn_save = tk.Button(button_frame, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(button_frame, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear.pack(side=tk.LEFT, padx=5)

root.mainloop()



