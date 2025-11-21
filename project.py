"""
===========================================================
         🌐 LANGUAGE TRANSLATION TOOL (FINAL)
      ✨ Professional UI • Modern Colors • Full Features ✨
===========================================================
"""

from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyperclip


# =============================================================
#   MAIN APPLICATION CLASS WITH PREMIUM COLOR THEME
# =============================================================
class LanguageTranslator:

    def __init__(self, root):

        self.root = root
        self.root.title("🌐 Language Translation Tool - Task 1")
        self.root.geometry("950x620")
        self.root.config(bg="#EFE6FF")     # Soft Lavender

        # Translator instance
        self.translator = Translator()

        # Languages
        self.languages = list(LANGUAGES.values())
        self.lang_codes = {v: k for k, v in LANGUAGES.items()}

        self.build_ui()


    # =============================================================
    #   BUILD THE COMPLETE USER INTERFACE
    # =============================================================
    def build_ui(self):

        # ---------- Title Section ----------
        Label(
            self.root,
            text="🌐 Language Translation Tool",
            font=("Arial", 26, "bold"),
            bg="#EFE6FF",
            fg="#4A0072"
        ).pack(pady=20)


        # ---------- Language Select Frame ----------
        lang_frame = Frame(self.root, bg="#EFE6FF")
        lang_frame.pack(pady=10)

        # From Language
        Label(lang_frame, text="From Language:", font=("Arial", 14), bg="#EFE6FF", fg="#4A0072") \
            .grid(row=0, column=0, padx=15)

        self.src_lang = StringVar(value="english")
        ttk.Combobox(
            lang_frame,
            textvariable=self.src_lang,
            values=self.languages,
            width=28,
            state="readonly"
        ).grid(row=0, column=1, padx=15)

        # To Language
        Label(lang_frame, text="To Language:", font=("Arial", 14), bg="#EFE6FF", fg="#4A0072") \
            .grid(row=0, column=2, padx=15)

        self.dest_lang = StringVar(value="hindi")
        ttk.Combobox(
            lang_frame,
            textvariable=self.dest_lang,
            values=self.languages,
            width=28,
            state="readonly"
        ).grid(row=0, column=3, padx=15)


        # ---------- Input Box ----------
        Label(
            self.root,
            text="Enter Text:",
            font=("Arial", 16, "bold"),
            bg="#EFE6FF",
            fg="#4A0072"
        ).pack()

        self.input_box = Text(
            self.root,
            width=100,
            height=8,
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#4A0072",
            relief=SOLID,
            bd=2
        )
        self.input_box.pack(pady=10)


        # ---------- Buttons ----------
        button_frame = Frame(self.root, bg="#EFE6FF")
        button_frame.pack(pady=20)

        translate_btn = Button(
            button_frame,
            text="Translate",
            command=self.translate_text,
            width=14,
            font=("Arial", 13, "bold"),
            bg="#6A0DAD",
            fg="white",
            relief=RAISED,
            bd=3
        )
        translate_btn.grid(row=0, column=0, padx=15)

        clear_btn = Button(
            button_frame,
            text="Clear",
            command=self.clear_text,
            width=14,
            font=("Arial", 13),
            bg="#8E24AA",
            fg="white",
            relief=RAISED,
            bd=3
        )
        clear_btn.grid(row=0, column=1, padx=15)

        copy_btn = Button(
            button_frame,
            text="Copy Output",
            command=self.copy_result,
            width=14,
            font=("Arial", 13),
            bg="#BA68C8",
            fg="white",
            relief=RAISED,
            bd=3
        )
        copy_btn.grid(row=0, column=2, padx=15)


        # ---------- Output Box ----------
        Label(
            self.root,
            text="Translated Output:",
            font=("Arial", 16, "bold"),
            bg="#EFE6FF",
            fg="#4A0072"
        ).pack()

        self.output_box = Text(
            self.root,
            width=100,
            height=8,
            font=("Arial", 12),
            bg="#FFFFFF",
            fg="#4A0072",
            relief=SOLID,
            bd=2
        )
        self.output_box.pack(pady=10)


    # =============================================================
    #   TRANSLATION FUNCTION
    # =============================================================
    def translate_text(self):
        try:
            text = self.input_box.get("1.0", END).strip()

            if not text:
                messagebox.showwarning("Warning", "Please enter text to translate.")
                return

            src = self.src_lang.get()
            dest = self.dest_lang.get()

            translated = self.translator.translate(
                text,
                src=self.lang_codes[src],
                dest=self.lang_codes[dest]
            )

            self.output_box.delete("1.0", END)
            self.output_box.insert(END, translated.text)

        except Exception:
            messagebox.showerror(
                "Error",
                "Failed to translate. Check your internet connection."
            )


    # =============================================================
    #   CLEAR FUNCTION
    # =============================================================
    def clear_text(self):
        self.input_box.delete("1.0", END)
        self.output_box.delete("1.0", END)


    # =============================================================
    #   COPY FUNCTION
    # =============================================================
    def copy_result(self):
        text = self.output_box.get("1.0", END)
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")


# =============================================================
#   RUN APPLICATION
# =============================================================
if __name__ == "__main__":
    root = Tk()
    LanguageTranslator(root)
    root.mainloop()

