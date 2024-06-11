import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

class MathApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Matematika")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self)

        self.linear_eq_frame = tk.Frame(tab_control)
        self.gauss_frame = tk.Frame(tab_control)
        self.matrix_op_frame = tk.Frame(tab_control)
        self.vector_op_frame = tk.Frame(tab_control)

        tab_control.add(self.linear_eq_frame, text="Persamaan Linier")
        tab_control.add(self.gauss_frame, text="Eliminasi Gauss")
        tab_control.add(self.matrix_op_frame, text="Operasi Matriks")
        tab_control.add(self.vector_op_frame, text="Operasi Vektor")
        
        tab_control.pack(expand=1, fill='both')

        self.create_linear_eq_widgets()
        self.create_gauss_widgets()
        self.create_matrix_op_widgets()
        self.create_vector_op_widgets()

    def create_linear_eq_widgets(self):
        tk.Label(self.linear_eq_frame, text="Masukkan koefisien dan konstanta (a1x + b1y = c1, a2x + b2y = c2):").grid(row=0, columnspan=4)
        
        self.a1 = tk.Entry(self.linear_eq_frame, width=5)
        self.a1.grid(row=1, column=0)
        self.b1 = tk.Entry(self.linear_eq_frame, width=5)
        self.b1.grid(row=1, column=1)
        self.c1 = tk.Entry(self.linear_eq_frame, width=5)
        self.c1.grid(row=1, column=2)

        self.a2 = tk.Entry(self.linear_eq_frame, width=5)
        self.a2.grid(row=2, column=0)
        self.b2 = tk.Entry(self.linear_eq_frame, width=5)
        self.b2.grid(row=2, column=1)
        self.c2 = tk.Entry(self.linear_eq_frame, width=5)
        self.c2.grid(row=2, column=2)

        tk.Button(self.linear_eq_frame, text="Hitung", command=self.solve_linear_eq).grid(row=3, columnspan=3)

    def create_gauss_widgets(self):
        tk.Label(self.gauss_frame, text="Masukkan matriks augmented untuk eliminasi Gauss/Gauss-Jordan:").grid(row=0, columnspan=5)
        
        self.gauss_matrix_entries = []
        for i in range(3):
            row_entries = []
            for j in range(4):
                entry = tk.Entry(self.gauss_frame, width=5)
                entry.grid(row=i+1, column=j)
                row_entries.append(entry)
            self.gauss_matrix_entries.append(row_entries)

        tk.Button(self.gauss_frame, text="Eliminasi Gauss", command=self.eliminate_gauss).grid(row=4, column=0, columnspan=2)
        tk.Button(self.gauss_frame, text="Eliminasi Gauss-Jordan", command=self.eliminate_gauss_jordan).grid(row=4, column=2, columnspan=2)

    def create_matrix_op_widgets(self):
        tk.Label(self.matrix_op_frame, text="Masukkan ordo matriks:").grid(row=0, columnspan=2)
        tk.Label(self.matrix_op_frame, text="Baris:").grid(row=1, column=0)
        tk.Label(self.matrix_op_frame, text="Kolom:").grid(row=1, column=2)

        self.matrix_rows = tk.Entry(self.matrix_op_frame, width=5)
        self.matrix_rows.grid(row=1, column=1)
        self.matrix_cols = tk.Entry(self.matrix_op_frame, width=5)
        self.matrix_cols.grid(row=1, column=3)

        tk.Button(self.matrix_op_frame, text="Set Ordo", command=self.set_matrix_order).grid(row=1, column=4)

        self.matrix_a_entries = []
        self.matrix_b_entries = []

        self.matrix_a_frame = tk.Frame(self.matrix_op_frame)
        self.matrix_b_frame = tk.Frame(self.matrix_op_frame)

    def set_matrix_order(self):
        try:
            rows = int(self.matrix_rows.get())
            cols = int(self.matrix_cols.get())

            self.matrix_a_entries = []
            self.matrix_b_entries = []

            for widget in self.matrix_a_frame.winfo_children():
                widget.destroy()
            for widget in self.matrix_b_frame.winfo_children():
                widget.destroy()

            self.matrix_a_frame.grid(row=2, column=0, columnspan=3)
            self.matrix_b_frame.grid(row=2, column=4, columnspan=3)

            for i in range(rows):
                row_a_entries = []
                row_b_entries = []
                for j in range(cols):
                    entry_a = tk.Entry(self.matrix_a_frame, width=5)
                    entry_a.grid(row=i, column=j)
                    row_a_entries.append(entry_a)

                    entry_b = tk.Entry(self.matrix_b_frame, width=5)
                    entry_b.grid(row=i, column=j)
                    row_b_entries.append(entry_b)
                
                self.matrix_a_entries.append(row_a_entries)
                self.matrix_b_entries.append(row_b_entries)

            tk.Button(self.matrix_op_frame, text="Tambah", command=self.add_matrices).grid(row=4, column=0, columnspan=2)
            tk.Button(self.matrix_op_frame, text="Kurang", command=self.subtract_matrices).grid(row=4, column=2, columnspan=2)
            tk.Button(self.matrix_op_frame, text="Kali", command=self.multiply_matrices).grid(row=4, column=4, columnspan=2)
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_vector_op_widgets(self):
        tk.Label(self.vector_op_frame, text="Masukkan vektor A dan B untuk operasi penjumlahan, perkalian skalar, atau dot product:").grid(row=0, columnspan=6)
        
        self.vector_a_entries = []
        self.vector_b_entries = []
        
        for i in range(3):
            entry_a = tk.Entry(self.vector_op_frame, width=5)
            entry_a.grid(row=i+1, column=0)
            self.vector_a_entries.append(entry_a)
            
            entry_b = tk.Entry(self.vector_op_frame, width=5)
            entry_b.grid(row=i+1, column=2)
            self.vector_b_entries.append(entry_b)

        tk.Button(self.vector_op_frame, text="Tambah", command=self.add_vectors).grid(row=4, column=0, columnspan=2)
        tk.Button(self.vector_op_frame, text="Kali", command=self.multiply_vectors).grid(row=4, column=2, columnspan=2)
        tk.Button(self.vector_op_frame, text="Dot Product", command=self.dot_product_vectors).grid(row=4, column=4, columnspan=2)

    def solve_linear_eq(self):
        try:
            a1 = float(self.a1.get())
            b1 = float(self.b1.get())
            c1 = float(self.c1.get())
            a2 = float(self.a2.get())
            b2 = float(self.b2.get())
            c2 = float(self.c2.get())
            
            a = np.array([[a1, b1], [a2, b2]])
            b = np.array([c1, c2])
            solution = np.linalg.solve(a, b)
            
            messagebox.showinfo("Hasil", f"Solusi: x={solution[0]}, y={solution[1]}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminate_gauss(self):
        try:
            matrix = np.array([[float(entry.get()) for entry in row] for row in self.gauss_matrix_entries])
            matrix = self.gaussian_elimination(matrix)
            messagebox.showinfo("Hasil", f"Matriks setelah eliminasi Gauss:\n{matrix}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminate_gauss_jordan(self):
        try:
            matrix = np.array([[float(entry.get()) for entry in row] for row in self.gauss_matrix_entries])
            matrix = self.gaussian_jordan_elimination(matrix)
            messagebox.showinfo("Hasil", f"Matriks setelah eliminasi Gauss-Jordan:\n{matrix}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def gaussian_elimination(self, matrix):
        rows, cols = matrix.shape
        for i in range(rows):
            max_row = i + np.argmax(np.abs(matrix[i:, i]))
            matrix[[i, max_row]] = matrix[[max_row, i]]
            matrix[i] = matrix[i] / matrix[i, i]
            for j in range(i + 1, rows):
                matrix[j] -= matrix[i] * matrix[j, i]
        return matrix

    def gaussian_jordan_elimination(self, matrix):
        matrix = self.gaussian_elimination(matrix)
        rows, cols = matrix.shape
        for i in range(rows - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                matrix[j] -= matrix[i] * matrix[j, i]
        return matrix

    def add_matrices(self):
        try:
            a = np.array([[float(entry.get()) for entry in row] for row in self.matrix_a_entries])
            b = np.array([[float(entry.get()) for entry in row] for row in self.matrix_b_entries])
            result = a + b
            messagebox.showinfo("Hasil", f"Hasil Penjumlahan:\n{result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def subtract_matrices(self):
        try:
            a = np.array([[float(entry.get()) for entry in row] for row in self.matrix_a_entries])
            b = np.array([[float(entry.get()) for entry in row] for row in self.matrix_b_entries])
            result = a - b
            messagebox.showinfo("Hasil", f"Hasil Pengurangan:\n{result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def multiply_matrices(self):
        try:
            a = np.array([[float(entry.get()) for entry in row] for row in self.matrix_a_entries])
            b = np.array([[float(entry.get()) for entry in row] for row in self.matrix_b_entries])
            result = np.dot(a, b)
            messagebox.showinfo("Hasil", f"Hasil Perkalian:\n{result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_vectors(self):
        try:
            a = np.array([float(entry.get()) for entry in self.vector_a_entries])
            b = np.array([float(entry.get()) for entry in self.vector_b_entries])
            result = a + b
            messagebox.showinfo("Hasil", f"Hasil Penjumlahan Vektor:\n{result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def multiply_vectors(self):
        try:
            a = np.array([float(entry.get()) for entry in self.vector_a_entries])
            b = np.array([float(entry.get()) for entry in self.vector_b_entries])
            result = a * b  # Perkalian vektor dilakukan dengan mengalikan setiap elemen
            messagebox.showinfo("Hasil", f"Hasil Perkalian Vektor:\n{result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def dot_product_vectors(self):
        try:
            a = np.array([float(entry.get()) for entry in self.vector_a_entries])
            b = np.array([float(entry.get()) for entry in self.vector_b_entries])
            result = np.dot(a, b)
            messagebox.showinfo("Hasil", f"Hasil Dot Product:\n{result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = MathApp()
    app.mainloop()
