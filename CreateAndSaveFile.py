from tkinter import *
from tkinter import filedialog

def save_file():
    
    file = filedialog.asksaveasfile(initialdir="\\Users\\jason\\PycharmProjects\\pythonProject\\CreateAndSaveFile.py",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text Files",".txt"),          # Text files
                                        ("HTML Files", ".html"),        # HTML files
                                        ("All Files", ".*"),            # All files
                                    ])

    file_text = str(text.get(1.0,END))
    file.write(file_text)
    file.close()

    # Close out if no file saved
    if file is None:
        return

# Create GUI window
window = Tk()

# Create save button
button = Button(window,text="Save",command=save_file)
button.pack()

# Create textarea
text = Text(window)
text.pack()

window.mainloop()
