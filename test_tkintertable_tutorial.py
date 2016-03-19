import tkinter as tk
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

root = tk.Tk()
tframe = tk.Frame(root)
tframe.pack()

table = TableCanvas(tframe)
table.createTableFrame()

root.mainloop()
