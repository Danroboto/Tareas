import tkinter as tk
from tkinter import ttk, messagebox
from tareas import agregar_estado, marcar_completado

# Colores
COLOR_FONDO = "#e8f0fe"
COLOR_LISTA = "#ffffff"
COLOR_COMPLETADO_BG = "#d4edda"
COLOR_COMPLETADO_TXT = "#155724"
COLOR_TEXTO = "#333333"

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Lista de Tareas")
        self.root.geometry("600x600")
        self.root.minsize(300, 300)
        self.root.maxsize(800, 600)
        self.root.configure(bg=COLOR_FONDO)

        self._estilos()
        self._crear_widgets()

    def _estilos(self):
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("TButton", font=("Segoe UI", 10), padding=6)
        self.style.configure("TFrame", background=COLOR_FONDO)
        self.style.configure("TLabel", background=COLOR_FONDO, foreground=COLOR_TEXTO)

    def _crear_widgets(self):
        # Botones
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=15)

        ttk.Button(button_frame, text="➕ Agregar Tarea", command=self.agregar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🗑️ Eliminar", command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="✅ Completado", command=self.marcar_completado).pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        list_frame = ttk.Frame(self.root)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas = tk.Listbox(
            list_frame,
            selectmode=tk.SINGLE,
            font=("Segoe UI", 11),
            width=50,
            height=20,
            yscrollcommand=self.scrollbar.set,
            selectbackground="#cce5ff",
            bg=COLOR_LISTA,
            bd=0,
            relief=tk.FLAT
        )
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.lista_tareas.yview)

    def agregar_tarea(self):
        nueva_ventana = tk.Toplevel(self.root)
        nueva_ventana.title("Nueva Tarea")
        nueva_ventana.geometry("350x150")
        nueva_ventana.configure(bg=COLOR_FONDO)

        ttk.Label(nueva_ventana, text="Escribe tu tarea:").pack(pady=10)
        entrada = ttk.Entry(nueva_ventana, width=40)
        entrada.pack(pady=5)

        def guardar():
            texto = entrada.get().strip()
            if texto:
                tarea = agregar_estado(texto)
                self.lista_tareas.insert(tk.END, tarea)
                nueva_ventana.destroy()
            else:
                messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

        ttk.Button(nueva_ventana, text="Guardar", command=guardar).pack(pady=10)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion)
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

    def marcar_completado(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista_tareas.get(index)
            nueva = marcar_completado(tarea)

            self.lista_tareas.delete(index)
            self.lista_tareas.insert(index, nueva)

            # Cambia colores según el emoji
            if nueva.startswith("✅"):
                self.lista_tareas.itemconfig(index, {'bg': COLOR_COMPLETADO_BG, 'fg': COLOR_COMPLETADO_TXT})
            else:
                self.lista_tareas.itemconfig(index, {'bg': COLOR_LISTA, 'fg': COLOR_TEXTO})
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para marcar como completada.")


