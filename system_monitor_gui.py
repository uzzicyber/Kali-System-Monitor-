import tkinter as tk
from tkinter import ttk
import psutil

# Create main window
root = tk.Tk()
root.title("KaliSysMonitor")
root.geometry("500x400")
root.resizable(False, False)

# CPU usage
cpu_label = tk.Label(root, text="CPU Usage per Core", font=("Arial", 12, "bold"))
cpu_label.pack(pady=5)

cpu_bars = []
for i in range(psutil.cpu_count()):
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=20, pady=2)
    label = tk.Label(frame, text=f"Core {i+1}")
    label.pack(side="left")
    bar = ttk.Progressbar(frame, length=300, maximum=100)
    bar.pack(side="left", padx=10)
    cpu_bars.append(bar)

# Memory usage
mem_label = tk.Label(root, text="Memory Usage", font=("Arial", 12, "bold"))
mem_label.pack(pady=10)
mem_bar = ttk.Progressbar(root, length=400, maximum=100)
mem_bar.pack(pady=5)

# Disk usage
disk_label = tk.Label(root, text="Disk Usage", font=("Arial", 12, "bold"))
disk_label.pack(pady=10)
disk_bar = ttk.Progressbar(root, length=400, maximum=100)
disk_bar.pack(pady=5)

# Update function
def update():
    # CPU
    for i, bar in enumerate(cpu_bars):
        bar['value'] = psutil.cpu_percent(percpu=True)[i]
    # Memory
    mem_bar['value'] = psutil.virtual_memory().percent
    # Disk
    disk_bar['value'] = psutil.disk_usage('/').percent
    root.after(1000, update)  # update every second

update()
root.mainloop()
