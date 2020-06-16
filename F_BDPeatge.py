from tkinter import *

raiz=Tk()
raiz.title("Mi Base de Datos")
#raiz.resizable(True,True)
#raiz.config(width="600",height="300")
miFrame=Frame(raiz,width="1200",height="600")
miFrame.pack()

L_Codigo=Label(miFrame,text="CODIGO",padx=5,pady=5)
L_Codigo.grid(row=0, column=0,padx=5,pady=5)
E_Codigo=Entry(miFrame)
E_Codigo.grid(row=1,column=0,padx=5,pady=5)

L_Revisado=Label(miFrame, text="REVISADO EL:",padx=5,pady=5)
L_Revisado.grid(row=2,column=0)
E_Revisado=Entry(miFrame)
E_Revisado.grid(row=2,column=1,padx=5,pady=5)

L_CAlmacen=Label(miFrame, text="CODIGO ALMACEN:",padx=5,pady=5)
L_CAlmacen.grid(row=3,column=0)
E_CAlmacen=Entry(miFrame)
E_CAlmacen.grid(row=3,column=1,padx=5,pady=5)

L_CFabrica=Label(miFrame, text="COD. FABRICA:",padx=5,pady=5)
L_CFabrica.grid(row=4,column=0,padx=5,pady=5)
E_CFabrica=Entry(miFrame)
E_CFabrica.grid(row=4,column=1,columnspan=2,padx=5,pady=5)

L_PComanda=Label(miFrame, text="PUNTO DE COMANDA:",padx=5,pady=5)
L_PComanda.grid(row=5,column=0,padx=5,pady=5)
E_PComanda=Entry(miFrame)
E_PComanda.grid(row=5,column=1,columnspan=2,padx=5,pady=5)

L_Stock=Label(miFrame, text="STOCK:",padx=5,pady=5)
L_Stock.grid(row=6,column=0,padx=5,pady=5)

L_Calderas=Label(miFrame, text="CALDERAS:",padx=5,pady=5)
L_Calderas.grid(row=7,column=0,padx=5,pady=5)
E_Calderas=Entry(miFrame)
E_Calderas.grid(row=7,column=1,columnspan=2,padx=5,pady=5)

L_Almacen=Label(miFrame, text="ALMACEN:",padx=5,pady=5)
L_Almacen.grid(row=8,column=0,padx=5,pady=5)
E_Almacen=Entry(miFrame)
E_Almacen.grid(row=8,column=1,columnspan=2,padx=5,pady=5)

L_Washinton=Label(miFrame, text="WASHINTON:",padx=5,pady=5)
L_Washinton.grid(row=9,column=0,padx=5,pady=5)
E_Washinton=Entry(miFrame)
E_Washinton.grid(row=9,column=1,columnspan=2,padx=5,pady=5)

L_Total=Label(miFrame, text="TOTAL:",padx=5,pady=5)
L_Total.grid(row=10,column=0,padx=5,pady=5)
E_Total=Entry(miFrame)
E_Total.grid(row=10,column=1,columnspan=2,padx=5,pady=5)

L_Observaciones=Label(miFrame, text="OBSERVACIONES:",padx=5,pady=5)
L_Observaciones.grid(row=11,column=0,padx=5,pady=5)
E_Observaciones=Entry(miFrame)
E_Observaciones.grid(row=12,column=0,padx=5,pady=5)

B_Tabla=Button(miFrame, text="TABLA", width=5, height=5)
B_Tabla.grid(row=12,column=2,padx=5,pady=5)

B_Salir=Button(miFrame, text="SALIR", width=5, height=5)
B_Salir.grid(row=12,column=3,padx=5,pady=5)

raiz.mainloop()