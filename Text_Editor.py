from tkinter import *
from tkinter import filedialog, colorchooser
from tkinter import font

root = Tk()
root.title("Text Editor By M074MED")
root.geometry("800x600")

global open_status_name
open_status_name = False

global selected
selected = False


def new_file(e):
    text.delete(1.0, END)
    root.title("New File - Text Editor By M074MED")
    status_bar.config(text="New File    ")

    global open_status_name
    open_status_name = False


def open_file(e):
    text.delete(1.0, END)
    file = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"),
                                                                    ("Doc Files", "*.doc"),
                                                                    ("HTML Files", "*.html"),
                                                                    ("Python Files", "*.py"),
                                                                    ("All Files", "*.*")))
    name = file
    text_file = open(file, "r")
    stuff = text_file.read()
    root.title(f"{name} - Text Editor By M074MED")
    status_bar.config(text=f"{name} Opened    ")
    text.insert(END, stuff)
    text_file.close()

    if file:
        global open_status_name
        open_status_name = file


def save_as_file(e):
    file = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt", filetypes=(("Text Files", "*.txt"),
                                                                                               ("Doc Files", "*.doc"),
                                                                                               ("HTML Files", "*.html"),
                                                                                               ("Python Files", "*.py"),
                                                                                               ("All Files", "*.*")))
    if file:
        name = file
        status_bar.config(text=f"{name} Saved    ")

        text_file = open(file, "w")
        text_file.write(text.get(1.0, END))
        text_file.close()


def save_file(e):
    global open_status_name
    if open_status_name:
        status_bar.config(text=f"{open_status_name} Saved    ")
        text_file = open(open_status_name, "w")
        text_file.write(text.get(1.0, END))
        text_file.close()
    else:
        save_as_file(e)


def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        selected = text.selection_get()
        text.delete("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected)


def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        selected = text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    elif selected:
        position = text.index(INSERT)
        root.clipboard_clear()
        root.clipboard_append(selected)
        text.insert(position, selected)


def del_text():
    text.delete("sel.first", "sel.last")


def bold_it(e):
    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")
    text.tag_configure("bold", font=bold_font)
    current_tags = text.tag_names("sel.first")
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")


def italics_it(e):
    italics_font = font.Font(text, text.cget("font"))
    italics_font.configure(slant="italic")
    text.tag_configure("italic", font=italics_font)
    current_tags = text.tag_names("sel.first")
    if "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    else:
        text.tag_add("italic", "sel.first", "sel.last")


def underline_it(e):
    underline_font = font.Font(text, text.cget("font"))
    underline_font.configure(underline=True)
    text.tag_configure("underline", font=underline_font)
    current_tags = text.tag_names("sel.first")
    if "underline" in current_tags:
        text.tag_remove("underline", "sel.first", "sel.last")
    else:
        text.tag_add("underline", "sel.first", "sel.last")


def text_color():
    color = colorchooser.askcolor()[1]
    status_bar.config(text=f"Color: {color}    ")
    if color:
        color_font = font.Font(text, text.cget("font"))
        text.tag_configure("colored", font=color_font, foreground=color)  # or fg (instead of foreground)
        current_tags = text.tag_names("sel.first")
        if "colored" in current_tags:
            text.tag_remove("colored", "sel.first", "sel.last")
        else:
            text.tag_add("colored", "sel.first", "sel.last")


def all_text_color():
    color = colorchooser.askcolor()[1]
    status_bar.config(text=f"Color: {color}    ")
    if color:
        text.configure(fg=color)


def bg_color():
    color = colorchooser.askcolor()[1]
    status_bar.config(text=f"Color: {color}    ")
    if color:
        text.configure(bg=color)


def select_all(e):
    text.tag_add("sel", 1.0, END)


def clear(e):
    text.delete(1.0, END)


def night_mode_on():
    main_color = "#333333"
    second_color = "#222222"
    txt_color = "white"
    root.config(bg=main_color)
    text.config(bg=main_color, fg=txt_color)
    status_bar.config(bg=second_color, fg=txt_color)
    frame.config(bg=main_color)
    menu.config(bg=main_color, fg=txt_color)
    file_menu.config(bg=main_color, fg=txt_color)
    edit_menu.config(bg=main_color, fg=txt_color)
    format_menu.config(bg=main_color, fg=txt_color)
    colors.config(bg=main_color, fg=txt_color)
    options_menu.config(bg=main_color, fg=txt_color)
    toolbar_frame.config(bg=second_color)
    bold_button.config(bg=main_color, fg=txt_color)
    italics_button.config(bg=main_color, fg=txt_color)
    underline_button.config(bg=main_color, fg=txt_color)
    text_color_button.config(bg=main_color, fg=txt_color)
    undo_button.config(bg=main_color, fg=txt_color)
    redo_button.config(bg=main_color, fg=txt_color)
    select_all_button.config(bg=main_color, fg=txt_color)
    clear_button.config(bg=main_color, fg=txt_color)


def night_mode_off():
    main_color = "SystemButtonFace"
    second_color = "SystemButtonFace"
    txt_color = "black"
    root.config(bg=main_color)
    text.config(bg=main_color, fg=txt_color)
    status_bar.config(bg=second_color, fg=txt_color)
    frame.config(bg=main_color)
    menu.config(bg=main_color, fg=txt_color)
    file_menu.config(bg=main_color, fg=txt_color)
    edit_menu.config(bg=main_color, fg=txt_color)
    format_menu.config(bg=main_color, fg=txt_color)
    colors.config(bg=main_color, fg=txt_color)
    options_menu.config(bg=main_color, fg=txt_color)
    toolbar_frame.config(bg=second_color)
    bold_button.config(bg=main_color, fg=txt_color)
    italics_button.config(bg=main_color, fg=txt_color)
    underline_button.config(bg=main_color, fg=txt_color)
    text_color_button.config(bg=main_color, fg=txt_color)
    undo_button.config(bg=main_color, fg=txt_color)
    redo_button.config(bg=main_color, fg=txt_color)
    select_all_button.config(bg=main_color, fg=txt_color)
    clear_button.config(bg=main_color, fg=txt_color)


status_bar = Label(root, text="Ready    ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=3)

toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

frame = Frame(root)
frame.pack(pady=0.1)

vert_scroll = Scrollbar(frame)
vert_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(frame, orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X)

text = Text(frame,
            width=125,
            height=27,
            borderwidth=0,
            font=("Arial", 16),
            selectbackground="yellow",
            selectforeground="black",
            undo=True,
            yscrollcommand=vert_scroll.set,
            xscrollcommand=hor_scroll.set,
            wrap="none")
text.pack(fill=BOTH)

vert_scroll.config(command=text.yview)
hor_scroll.config(command=text.xview)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_file(False), accelerator="     Ctrl+N")
file_menu.add_command(label="Open...", command=lambda: open_file(False), accelerator="     Ctrl+O")
file_menu.add_command(label="Save", command=lambda: save_file(False), accelerator="     Ctrl+S")
file_menu.add_command(label="Save As...", command=lambda: save_as_file(False), accelerator="     Ctrl+Shift+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo, accelerator="     Ctrl+Z")
edit_menu.add_command(label="Redo", command=text.edit_redo, accelerator="     Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="     Ctrl+X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="     Ctrl+C")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="     Ctrl+V")
edit_menu.add_command(label="Delete", command=del_text, accelerator="     Del")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all(False), accelerator="     Ctrl+A")
edit_menu.add_command(label="Clear", command=lambda: clear(False), accelerator="     Ctrl+Shift+A")


format_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Format", menu=format_menu)
colors = Menu(format_menu, tearoff=False)
format_menu.add_command(label="Bold", font=("", 10, "bold"), command=lambda: bold_it(False),
                        accelerator="     Ctrl+B")
format_menu.add_command(label="Italic", font=("", 10, "italic"), command=lambda: italics_it(False),
                        accelerator="     Ctrl+L")
format_menu.add_command(label="Underline", font=("", 10, "underline"), command=lambda: underline_it(False),
                        accelerator="     Ctrl+U")
format_menu.add_separator()
format_menu.add_cascade(label="Colors", menu=colors)
colors.add_command(label="Text Color", command=text_color)
colors.add_command(label="All Text Color", command=all_text_color)
colors.add_command(label="Background Color", command=bg_color)

options_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Night Mode On", command=night_mode_on)
options_menu.add_command(label="Night Mode Off", command=night_mode_off)

root.bind("<Control-x>", cut_text)  # or <Control-key-x>
root.bind("<Control-c>", copy_text)
root.bind("<Control-v>", paste_text)
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-S>", save_as_file)
root.bind("<Control-b>", bold_it)
root.bind("<Control-l>", italics_it)
root.bind("<Control-u>", underline_it)
root.bind("<Control-A>", clear)

bold_button = Button(toolbar_frame, text="B", command=lambda: bold_it(False), font=("", 10, "bold"))
bold_button.grid(row=0, column=0, sticky=W)
italics_button = Button(toolbar_frame, text="I", command=lambda: italics_it(False), font=("", 10, "italic"))
italics_button.grid(row=0, column=1, padx=15)
underline_button = Button(toolbar_frame, text="U", command=lambda: underline_it(False), font=("", 10, "underline"))
underline_button.grid(row=0, column=2)
text_color_button = Button(toolbar_frame, text="Text Color", command=text_color)
text_color_button.grid(row=0, column=3, padx=15)
undo_button = Button(toolbar_frame, text="Undo", command=text.edit_undo)
undo_button.grid(row=0, column=4)
redo_button = Button(toolbar_frame, text="Redo", command=text.edit_redo)
redo_button.grid(row=0, column=5, padx=15)
select_all_button = Button(toolbar_frame, text="Select All", command=lambda: select_all(False))
select_all_button.grid(row=0, column=6)
clear_button = Button(toolbar_frame, text="Clear", command=lambda: clear(False))
clear_button.grid(row=0, column=7, padx=15)

root.mainloop()
