import tkinter as tk


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def encrypt_text():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = caesar_cipher(plaintext, shift)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", encrypted_text)


def decrypt_text():
    shift = int(shift_entry.get())
    encrypted_text = input_text.get("1.0", "end-1c")
    decrypted_text = caesar_cipher(encrypted_text, -shift)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", decrypted_text)


def copy_result():
    result = result_text.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(result)


# Create the main window
root = tk.Tk()
root.title("EncryptEasy")

# Input Text Box
input_label = tk.Label(root, text="Enter Text:")
input_label.pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack()

# Shift Entry
shift_label = tk.Label(root, text="Enter Shift (0-25):")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

# Decrypt Button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Result Text Box
result_label = tk.Label(root, text="Result:")
result_label.pack()
result_text = tk.Text(root, height=5, width=40)
result_text.pack()

# Copy Button
copy_button = tk.Button(root, text="Copy Result", command=copy_result)
copy_button.pack()

# Start the GUI main loop
root.mainloop()
