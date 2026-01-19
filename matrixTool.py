import tkinter as tk
from tkinter import messagebox
import numpy as np

def parse_matrix(text):
    try:
        rows = text.strip().split('\n')
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except:
        raise ValueError("Invalid matrix format")

def show_result(result):
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

def add_matrices():
    try:
        A = parse_matrix(matrix_a.get("1.0", tk.END))
        B = parse_matrix(matrix_b.get("1.0", tk.END))
        if A.shape != B.shape:
            raise ValueError("Matrices must have same dimensions")
        show_result(A + B)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def subtract_matrices():
    try:
        A = parse_matrix(matrix_a.get("1.0", tk.END))
        B = parse_matrix(matrix_b.get("1.0", tk.END))
        if A.shape != B.shape:
            raise ValueError("Matrices must have same dimensions")
        show_result(A - B)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def multiply_matrices():
    try:
        A = parse_matrix(matrix_a.get("1.0", tk.END))
        B = parse_matrix(matrix_b.get("1.0", tk.END))
        if A.shape[1] != B.shape[0]:
            raise ValueError("Invalid dimensions for multiplication")
        show_result(np.dot(A, B))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def transpose_matrix():
    try:
        A = parse_matrix(matrix_a.get("1.0", tk.END))
        show_result(A.T)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def determinant_matrix():
    try:
        A = parse_matrix(matrix_a.get("1.0", tk.END))
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square")
        show_result(np.linalg.det(A))
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Matrix Operations Tool")
root.geometry("700x500")

tk.Label(root, text="Matrix A (rows separated by new line)").pack()
matrix_a = tk.Text(root, height=5, width=50)
matrix_a.pack()

tk.Label(root, text="Matrix B (only for add, subtract, multiply)").pack()
matrix_b = tk.Text(root, height=5, width=50)
matrix_b.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=15, command=add_matrices).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Subtract", width=15, command=subtract_matrices).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Multiply", width=15, command=multiply_matrices).grid(row=0, column=2, padx=5)

tk.Button(button_frame, text="Transpose (A)", width=15, command=transpose_matrix).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Determinant (A)", width=15, command=determinant_matrix).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Result").pack()
result_text = tk.Text(root, height=5, width=50)
result_text.pack()

root.mainloop()
