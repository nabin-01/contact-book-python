import tkinter as tk
import tkinter.font as tkf
import tkinter.ttk as ttk
import tkinter.messagebox as tkm

class Main:
    def __init__(self, master):
        # Defining title and resize behavior of our Tkinter mainWindow
        master.title("Contact Book")
        master.resizable(True, True)

        # Defining GUI attributes
        self.arialRegular = tkf.Font(family="Arial", size=10, weight="normal")
        self.arialBold = tkf.Font(family="Arial", size=10, weight="bold")

        self.labelName = tk.Label(master, font=self.arialBold, text="Name")
        self.labelEmail = tk.Label(master, font=self.arialBold, text="Email")
        self.labelPhone = tk.Label(master, font=self.arialBold, text="Phone")
        self.labelAddress = tk.Label(master, font=self.arialBold, text="Address")

        self.entryName = tk.Entry(master, font=self.arialRegular, width=20)
        self.entryEmail = tk.Entry(master, font=self.arialRegular, width=20)
        self.entryPhone = tk.Entry(master, font=self.arialRegular, width=20)
        self.entryAddress = tk.Entry(master, font=self.arialRegular, width=20)

        self.buttonAdd = tk.Button(master, font=self.arialBold, text="Add", command=self.add)
        self.buttonDelete = tk.Button(master, font=self.arialBold, text="Del", command=self.delete)

        self.treeContacts = ttk.Treeview(master)
        self.treeContacts["columns"]=("name","email","phone","address")
        self.treeContacts.column("#0", width=100, minwidth=100, stretch=tk.NO)
        self.treeContacts.column("name", width=100, minwidth=100, stretch=tk.YES)
        self.treeContacts.column("email", width=100, minwidth=100, stretch=tk.YES)
        self.treeContacts.column("phone", width=100, minwidth=100, stretch=tk.YES)
        self.treeContacts.column("address", width=100, minwidth=100, stretch=tk.YES)
        self.treeContacts.heading("#0",text="ID",anchor=tk.W)
        self.treeContacts.heading("name", text="Name",anchor=tk.W)
        self.treeContacts.heading("email", text="Email",anchor=tk.W)
        self.treeContacts.heading("phone", text="Phone",anchor=tk.W)
        self.treeContacts.heading("address", text="Address",anchor=tk.W)

        # Drawing GUI with .grid
        self.treeContacts.grid(row=0, column=0, rowspan=9)
        self.labelName.grid(row=0, column=1, columnspan=2)
        self.entryName.grid(row=1, column=1, columnspan=2)
        self.labelEmail.grid(row=2, column=1, columnspan=2)
        self.entryEmail.grid(row=3, column=1, columnspan=2)
        self.labelPhone.grid(row=4, column=1, columnspan=2)
        self.entryPhone.grid(row=5, column=1, columnspan=2)
        self.labelAddress.grid(row=6, column=1, columnspan=2)
        self.entryAddress.grid(row=7, column=1, columnspan=2)
        self.buttonAdd.grid(row=8, column=1)
        self.buttonDelete.grid(row=8, column=2)
    
    # Method that is called by the "buttonAdd" 
    def add(self):
        # Check that no entry fields are empty
        if self.entryName.get() == "" or self.entryEmail.get() == "" or self.entryPhone.get() == "" or self.entryAddress.get() == "":
            tkm.showinfo()
        # Check that entryEmail contains @-symbol and entryPhone is only numbers
        elif "@" in self.entryEmail.get() == False or self.entryPhone.get().isdigit() == False:
            tkm.showerror()
        else:
            # TODO: Send information from entry fields to database function
            pass

    # Method that is called by the "buttonDelete"
    def delete():
        # Check that entryName isn't empty & only contains numbers
        if self.entryName.get() == "" or self.entryName.get().isdigit() == False:
            tkm.showwarning()
        else:
            # TODO: Send information from entryName to database function
            pass

# This blocks the code inside from being ran if this class is imported
if __name__ == "__main__":
    root = tk.Tk()
    Main(root)
    root.mainloop()