import tkinter as tk

# --- LOGIKA ---

def parse_int(value):
    """Jeśli pole puste → 0, inaczej int"""
    value = value.strip()
    return int(value) if value else 0


def rozbij_na_monety(zk, ss, mp):
    total_mp = zk * 240 + ss * 12 + mp

    zk_new = total_mp // 240
    reszta = total_mp % 240

    ss_new = reszta // 12
    mp_new = reszta % 12

    return zk_new, ss_new, mp_new


# --- OBSŁUGA PRZYCISKÓW ---

def klik_rozbij():
    try:
        zk = parse_int(entry_zk.get())
        ss = parse_int(entry_ss.get())
        mp = parse_int(entry_mp.get())
    except ValueError:
        label_wynik.config(text="Błąd: wpisz liczby")
        return

    zk_new, ss_new, mp_new = rozbij_na_monety(zk, ss, mp)
    label_wynik.config(text=f"{zk_new} ZK, {ss_new} SS, {mp_new} MP")


def klik_przelicz():
    try:
        zk = parse_int(entry_zk.get())
        ss = parse_int(entry_ss.get())
        mp = parse_int(entry_mp.get())
    except ValueError:
        label_wynik.config(text="Błąd: wpisz liczby")
        return

    total_mp = zk * 240 + ss * 12 + mp
    label_wynik.config(text=f"{total_mp} MP")


# --- UI ---

root = tk.Tk()
root.title("Mennica Imperium")
root.geometry("320x260")

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=15)

# ZK
entry_zk = tk.Entry(frame_inputs, width=6)
entry_zk.grid(row=0, column=0, padx=5)
label_zk = tk.Label(frame_inputs, text="ZK")
label_zk.grid(row=0, column=1)

# SS
entry_ss = tk.Entry(frame_inputs, width=6)
entry_ss.grid(row=0, column=2, padx=5)
label_ss = tk.Label(frame_inputs, text="SS")
label_ss.grid(row=0, column=3)

# MP
entry_mp = tk.Entry(frame_inputs, width=6)
entry_mp.grid(row=0, column=4, padx=5)
label_mp = tk.Label(frame_inputs, text="MP")
label_mp.grid(row=0, column=5)

# Przyciski
btn_przelicz = tk.Button(root, text="→ Przelicz na pensy", command=klik_przelicz)
btn_przelicz.pack(pady=5)

btn_rozbij = tk.Button(root, text="→ Rozbij na monety", command=klik_rozbij)
btn_rozbij.pack(pady=5)

# Wynik
label_wynik = tk.Label(root, text="", font=("Arial", 12))
label_wynik.pack(pady=10)

# Info
label_info = tk.Label(root, text="1 ZK = 20 SS = 240 MP", font=("Arial", 8))
label_info.pack(side="bottom", pady=5)

root.mainloop()