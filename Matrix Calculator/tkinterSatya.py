import tkinter as tk
import numpy as np
from svdCel import SVD_function
from luRey import lu_decomposition
from diagTony import check_diagonalizability, calculate_eigen
from powerZel import power_method 

saved_matrix = None
matrixIsNull = True

class CommandPrompt(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.output = tk.Text(self, wrap='word', bg='black', fg='white', insertbackground='white', font=("Courier", 12))
        self.output.pack(fill='both', expand=True)
        self.output.insert('end', "Enter matrix rows one by one:\n")
        self.output.config(state='disabled')

        self.input_frame = tk.Frame(self, bg='black')
        self.input_frame.pack(fill='x')
        self.input_label = tk.Label(self.input_frame, text="User Input: ", bg='black', fg='white', font=("Courier", 12))
        self.input_label.pack(side='left')
        self.input = tk.Entry(self.input_frame, bg='black', fg='white', insertbackground='white', font=("Courier", 12))
        self.input.pack(side='left', fill='x', expand=True)
        self.input.bind('<Return>', self.on_enter)
        self.input.focus()

        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.pack(pady=10)

        self.submit_button = tk.Button(self.button_frame, text="Submit Matrix", command=self.submit_matrix, bg='#839e9e', fg='white', font=("Courier", 12))
        self.submit_button.pack(side='left', padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Reset Console/Matrix", command=self.reset_console, bg='#839e9e', fg='white', font=("Courier", 12))
        self.clear_button.pack(side='left', padx=5)

        self.matrix_lines = []


    def on_enter(self, event):
        input_text = self.input.get().strip()
        self.output.config(state='normal')
        self.output.insert('end', f"{input_text}\n")
        self.output.config(state='disabled')
        self.input.delete(0, 'end')
        self.matrix_lines.append(input_text)
        return 'break'

    def submit_matrix(self):
        global saved_matrix
        if not self.matrix_lines:
            self.output.config(state='normal')
            self.output.insert('end', "No matrix input provided.\n")
            self.output.config(state='disabled')
            return

        try:
            matrix = [list(map(float, line.split())) for line in self.matrix_lines]
            row_lengths = [len(row) for row in matrix]
            if len(set(row_lengths)) != 1:
                raise ValueError("All rows must have the same length.")
            saved_matrix = np.array(matrix)
            self.output.config(state='normal')
            self.output.insert('end', "Matrix saved successfully.\n")
            self.output.config(state='disabled')
        except ValueError as e:
            self.output.config(state='normal')
            self.output.insert('end', f"Invalid matrix: {e}\n")
            self.output.config(state='disabled')
            self.matrix_lines = []

    
    def reset_console(self):
        global saved_matrix
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        self.output.insert('end', "Enter matrix rows one by one:\n")
        self.output.config(state='disabled')
        self.matrix_lines.clear()
        saved_matrix = None

def set_MatrixAsNotNull():
    global matrixIsNull
    matrixIsNull = False

def show_frame(frame):
    for f in all_frames:
        f.pack_forget()  # Hide all frames
    frame.pack(fill=tk.BOTH, expand=True)  # Show the specified frame

def refresh_main_menu():
    for widget in frame1.winfo_children():
        widget.destroy()  # Clear existing widgets

    label_logo = tk.Label(
        frame1,
        text="[A]",
        bg="#13273f",
        fg='white',
        font=("TkMenuFont", 80),
    )
    label_logo.pack(pady=(40, 20))

    label_title = tk.Label(
        frame1,
        text="A Matrix Calculator",
        bg="#13273f",
        fg='white',
        font=("TkMenuFont", 30),
    )
    label_title.pack(pady=(0, 30))

    tk.Button(
        frame1,
        text="Insert/Change your Matrix",
        font=("TkHeadingFont", 15),
        bg="#839e9e",
        fg="white",
        cursor="hand2",
        activebackground="white",
        activeforeground="black",
        command=lambda: show_frame(frame0)
    ).pack(pady=10)

    if not matrixIsNull:
        tk.Button(
            frame1,
            text="Diagonalizable Matrix",
            font=("TkHeadingFont", 15),
            bg="#839e9e",
            fg="white",
            cursor="hand2",
            activebackground="white",
            activeforeground="black",
            command=lambda: show_frame(frame2)
        ).pack(pady=10)

        tk.Button(
            frame1,
            text="LU Decomposition",
            font=("TkHeadingFont", 15),
            bg="#839e9e",
            fg="white",
            cursor="hand2",
            activebackground="white",
            activeforeground="black",
            command=lambda: show_frame(frame3)
        ).pack(pady=10)

        tk.Button(
            frame1,
            text="Power Method",
            font=("TkHeadingFont", 15),
            bg="#839e9e",
            fg="white",
            cursor="hand2",
            activebackground="white",
            activeforeground="black",
            command=lambda: show_frame(frame4)
        ).pack(pady=10)

        tk.Button(
            frame1,
            text="Singular Value Decomposition",
            font=("TkHeadingFont", 15),
            bg="#839e9e",
            fg="white",
            cursor="hand2",
            activebackground="white",
            activeforeground="black",
            command=lambda: show_frame(frame5)
        ).pack(pady=10)

    tk.Button(
        frame1,
        text="Credits",
        font=("TkHeadingFont", 15),
        bg="#839e9e",
        fg="white",
        cursor="hand2",
        activebackground="white",
        activeforeground="black",
        command=lambda: show_frame(frame6)
    ).pack(pady=10)

# Initialize app
root = tk.Tk()
root.title("AOL Project for Matrix Calculations")

# Center the window
x = root.winfo_screenwidth() // 2 - 350
y = int(root.winfo_screenheight() * 0.015)
root.geometry('700x650+' + str(x) + '+' + str(y))

# Define frames
frame0 = tk.Frame(root, bg="#2f4f4f")
frame0.pack(fill="both", expand=True)  # Insert/Change Matrix

frame1 = tk.Frame(root, bg="#13273f")  # Main Menu
frame2 = tk.Frame(root, bg="#2f4f4f")  # Diagonalizable Matrix
frame3 = tk.Frame(root, bg="#2f4f4f")  # LU Decomposition
frame4 = tk.Frame(root, bg="#2f4f4f")  # Power Method
frame5 = tk.Frame(root, bg="#2f4f4f")  # SVD
frame6 = tk.Frame(root, bg="black")    # Credits
all_frames = [frame0, frame1, frame2, frame3, frame4, frame5, frame6]

# Frame 0 ==================================================================
tk.Label(
    frame0,
    text="Insert the Matrix here",
    bg="#2f4f4f",
    fg='white',
    font=("TkMenuFont", 30),
).pack(pady=(5, 10))

command_prompt = CommandPrompt(frame0)
command_prompt.pack(fill='both', expand=True)

tk.Button(
    frame0,
    text="Back to Main Menu",
    font=("TkHeadingFont", 20),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=lambda: [set_MatrixAsNotNull(), show_frame(frame1), refresh_main_menu()]
).pack(pady=20)

# Frame 2 (Diagonalizable Matrix) ==================================================================
label_diag = tk.Label(
    frame2,
    text="Diagonalizable Matrix",
    bg="#2f4f4f",
    fg='white',
    font=("TkMenuFont", 30),
)
label_diag.pack(pady=(5, 10))

diag_output = tk.Text(frame2, wrap='word', bg='black', fg='white', insertbackground='white', font=("Courier", 12))
diag_output.pack(fill='both', expand=True)
diag_output.config(state='disabled')

def check_diag_matrix():
    global saved_matrix
    if saved_matrix is None:
        diag_output.config(state='normal')
        diag_output.delete('1.0', tk.END)
        diag_output.insert('end', "No matrix saved. Please input a matrix from the Main Menu.\n")
        diag_output.config(state='disabled')
        return

    if saved_matrix.shape[0] != saved_matrix.shape[1]:
        diag_output.config(state='normal')
        diag_output.delete('1.0', tk.END)
        diag_output.insert('end', "Matrix is not square. This program requires a square matrix.\n")
        diag_output.config(state='disabled')
        return

    try:
        is_diagonalizable, eigenvalues, eigenvectors = check_diagonalizability(saved_matrix)
        diag_output.config(state='normal')
        diag_output.delete('1.0', tk.END)
        diag_output.insert('end', f"Matrix:\n{saved_matrix}\n")
        diag_output.insert('end', f"\nEigenvalues:\n{eigenvalues}\n")
        diag_output.insert('end', f"\nEigenvectors:\n{eigenvectors}\n")
        if is_diagonalizable:
            diag_output.insert('end', "\nThe matrix is diagonalizable.\n")
        else:
            diag_output.insert('end', "\nThe matrix is not diagonalizable.\n")
    except Exception as e:
        diag_output.config(state='normal')
        diag_output.delete('1.0', tk.END)
        diag_output.insert('end', f"An error occurred: {e}\n")
    diag_output.config(state='disabled')

tk.Button(
    frame2,
    text="Check Diagonalizability",
    font=("TkHeadingFont", 15),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=check_diag_matrix
).pack(pady=10)

tk.Button(
    frame2,
    text="Back to Main Menu",
    font=("TkHeadingFont", 20),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=lambda: show_frame(frame1)
).pack(pady=20)

# Frame 3 (LU Decomposition) ==================================================================
label_lu = tk.Label(
    frame3,
    text="LU Decomposition",
    bg="#2f4f4f",
    fg='white',
    font=("TkMenuFont", 30),
)
label_lu.pack(pady=(5, 10))

lu_output = tk.Text(frame3, wrap='word', bg='black', fg='white', insertbackground='white', font=("Courier", 12))
lu_output.pack(fill='both', expand=True)
lu_output.config(state='disabled')

def perform_lu():
    global saved_matrix
    if saved_matrix is None:
        lu_output.config(state='normal')
        lu_output.delete('1.0', tk.END)
        lu_output.insert('end', "No matrix saved. Please input a matrix from the Main Menu.\n")
        lu_output.config(state='disabled')
        return
    if saved_matrix.shape[0] != saved_matrix.shape[1]:
        lu_output.config(state='normal')
        lu_output.delete('1.0', tk.END)
        lu_output.insert('end', "Matrix is not square. This program requires a square matrix.\n")
        lu_output.config(state='disabled')
        return
    try:
        L, U = lu_decomposition(saved_matrix)
        lu_output.config(state='normal')
        lu_output.delete('1.0', tk.END)
        lu_output.insert('end', f"Original Matrix:\n{saved_matrix}\n\n")
        lu_output.insert('end', f"Lower Triangular Matrix L:\n{L}\n\n")
        lu_output.insert('end', f"Upper Triangular Matrix U:\n{U}\n\n")
        lu_output.config(state='disabled')
    except Exception as e:
        lu_output.config(state='normal')
        lu_output.delete('1.0', tk.END)
        lu_output.insert('end', f"Error performing LU decomposition: {e}\n")
        lu_output.config(state='disabled')

tk.Button(
    frame3,
    text="Perform LU Decomposition",
    font=("TkHeadingFont", 15),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=perform_lu
).pack(pady=10)

tk.Button(
    frame3,
    text="Back to Main Menu",
    font=("TkHeadingFont", 20),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=lambda: show_frame(frame1)
).pack(pady=20)

# Frame 4 (Power Method) ==================================================================
label_svd = tk.Label(
    frame4,
    text="Power Method",
    bg="#2f4f4f",
    fg='white',
    font=("TkMenuFont", 30),
)
label_svd.pack(pady=(5, 10))

power_output = tk.Text(frame4, wrap='word', bg='black', fg='white', insertbackground='white', font=("Courier", 12))
power_output.pack(fill='both', expand=True)
power_output.config(state='disabled')

def perform_power_method():
    global saved_matrix
    if saved_matrix is None:
        power_output.config(state='normal')
        power_output.delete('1.0', tk.END)
        power_output.insert('end', "No matrix saved. Please input a matrix from the Main Menu.\n")
        power_output.config(state='disabled')
        return
    if saved_matrix.shape[0] != saved_matrix.shape[1]:
        power_output.config(state='normal')
        power_output.delete('1.0', tk.END)
        power_output.insert('end', "Matrix is not square. This program requires a square matrix.\n")
        power_output.config(state='disabled')
        return
    try:
        eigenvalue, eigenvector = power_method(saved_matrix)
        power_output.config(state='normal')
        power_output.delete('1.0', tk.END)
        power_output.insert('end', f"Original Matrix:\n{saved_matrix}\n\n")
        power_output.insert('end', f"Dominant Eigenvalue: {eigenvalue:.6f}\n\n")
        power_output.insert('end', f"Dominant Eigenvector:\n{eigenvector}\n\n")
        power_output.config(state='disabled')
    except Exception as e:
        power_output.config(state='normal')
        power_output.delete('1.0', tk.END)
        power_output.insert('end', f"Error performing Power Method: {e}\n")
        power_output.config(state='disabled')

tk.Button(
    frame4,
    text="Perform Power Method",
    font=("TkHeadingFont", 15),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=perform_power_method
).pack(pady=10)

tk.Button(
    frame4,
    text="Back to Main Menu",
    font=("TkHeadingFont", 20),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=lambda: show_frame(frame1)
).pack(pady=20)

# Frame 5 (SVD Menu) ==================================================================
label_svd = tk.Label(
    frame5,
    text="Singular Value Decomposition",
    bg="#2f4f4f",
    fg='white',
    font=("TkMenuFont", 30),
)
label_svd.pack(pady=(5, 10))

svd_output = tk.Text(frame5, wrap='word', bg='black', fg='white', insertbackground='white', font=("Courier", 12))
svd_output.pack(fill='both', expand=True)
svd_output.config(state='disabled')

def perform_svd():
    global saved_matrix
    if saved_matrix is None:
        svd_output.config(state='normal')
        svd_output.delete('1.0', tk.END)
        svd_output.insert('end', "No matrix saved. Please input a matrix from the Main Menu.\n")
        svd_output.config(state='disabled')
        return
    try:
        U, S, Vt = SVD_function(saved_matrix)
        svd_output.config(state='normal')
        svd_output.delete('1.0', tk.END)
        svd_output.insert('end', f"Original Matrix:\n{saved_matrix}\n\n")
        svd_output.insert('end', f"Matrix U:\n{U}\n\n")
        svd_output.insert('end', f"Singular values Σ:\n{np.diag(S)}\n\n")
        svd_output.insert('end', f"Matrix Vᵀ:\n{Vt}\n\n")
        svd_output.config(state='disabled')
    except np.linalg.LinAlgError:
        svd_output.config(state='normal')
        svd_output.delete('1.0', tk.END)
        svd_output.insert('end', "Matrix is not valid for SVD. Please input a valid matrix in Frame 0.\n")
        svd_output.config(state='disabled')

tk.Button(
    frame5,
    text="Perform SVD",
    font=("TkHeadingFont", 15),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=perform_svd
).pack(pady=10)

tk.Button(
    frame5,
    text="Back to Main Menu",
    font=("TkHeadingFont", 20),
    bg="#839e9e",
    fg="white",
    cursor="hand2",
    activebackground="white",
    activeforeground="black",
    command=lambda: show_frame(frame1)
).pack(pady=20)

# Configure Frame 6 (Credits) ==================================================================
tk.Label(
    frame6,
    text="Created by yours truly,",
    bg="black",
    fg='white',
    font=("TkMenuFont", 30),
).pack(pady=(50, 20))
tk.Label(
    frame6,
    text="Anthony - 2702377612\nHazel Z. Adityo - 2702329576\nMarcell Prasetyo - 2702229895\nSatya D. Padmakumara - 2702244662\nSiddharta R. Wallace - 2702215233",
    bg="black",
    fg='white',
    font=("TkMenuFont", 20),
    justify="center"
).pack(pady=(50, 50))
tk.Button(
    frame6,
    text="Back to Main Menu",
    font=("TkHeadingFont", 20),
    bg="black",
    bd = 0,
    fg="white",
    cursor="hand2",
    activebackground="black",
    activeforeground="yellow",
    command=lambda: show_frame(frame1)
).pack(pady=20)

# Show the main menu
refresh_main_menu()
show_frame(frame1)

# Run app
root.mainloop()
