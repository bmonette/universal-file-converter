import customtkinter as ctk

def create_ebook_tab(parent):
    """
    Sets up the eBook Converter UI inside the given tab (parent frame).
    """
    title_label = ctk.CTkLabel(parent, text="📚 eBook Converter", font=("Arial", 24, "bold"))
    title_label.pack(pady=20)

    coming_soon = ctk.CTkLabel(parent, text="🚧 Feature coming soon...", font=("Arial", 16))
    coming_soon.pack(pady=10)
