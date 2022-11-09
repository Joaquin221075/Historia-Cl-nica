import tkinter as tk
from paciente.gui import Frame
def main():
    root = tk.TK()
    root.title("HISTORIA CLÍNICA")
    root.resizable(0,0)

    Frame = Frame(root)
    Frame.mainloop

if __name__ == "__main__":
    main()