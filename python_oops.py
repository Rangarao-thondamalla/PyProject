# Generate a program that can explain the python oops with realtime example with  nice ui
import tkinter as tk
from tkinter import ttk

class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    def get_description(self):
        return f"Vehicle: {self._brand} {self._model}"

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self._doors = doors

    def get_description(self):
        return f"Car: {self._brand} {self._model} with {self._doors} doors"

    def open_trunk(self):
        return "Trunk opened"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, sidecar=False):
        super().__init__(brand, model)
        self._sidecar = sidecar

    def get_description(self):
        sidecar_text = "with sidecar" if self._sidecar else "without sidecar"
        return f"Motorcycle: {self._brand} {self._model} {sidecar_text}"

def show_example(example_text):
    output_text.set(example_text)

def example_oop():
    car = Car("Toyota", "Camry", 4)
    motorcycle = Motorcycle("Harley-Davidson", "Iron 883", sidecar=True)
    description = (
        "Class: Vehicle, Car, Motorcycle\n"
        "Object: car, motorcycle\n"
        "Encapsulation: private attributes like _brand and _model\n"
        "Inheritance: Car and Motorcycle inherit from Vehicle\n"
        "Polymorphism: get_description() works differently for each class\n\n"
        f"{car.get_description()}\n{car.start_engine()}\n{car.open_trunk()}\n\n"
        f"{motorcycle.get_description()}\n{motorcycle.start_engine()}"
    )
    show_example(description)

def example_realtime():
    show_example("Real-time example:\n"
                 "A ride sharing app can use OOP to model vehicles, drivers, and passengers.\n"
                 "Each ride request creates objects and updates status live.")

app = tk.Tk()
app.title("Python OOP Explainer")
app.geometry("520x380")

output_text = tk.StringVar()
output_text.set("Click a button to see a Python OOP example.")

frame = ttk.Frame(app, padding=16)
frame.pack(fill="both", expand=True)

title = ttk.Label(frame, text="Python OOP with Real-time Example", font=("Segoe UI", 14, "bold"))
title.pack(pady=(0, 12))

info = ttk.Label(frame, textvariable=output_text, wraplength=480, justify="left")
info.pack(fill="both", expand=True, pady=(0, 12))

button_frame = ttk.Frame(frame)
button_frame.pack(fill="x", pady=(0, 8))

button_oop = ttk.Button(button_frame, text="Show OOP Example", command=example_oop)
button_oop.pack(side="left", expand=True, fill="x", padx=(0, 4))

button_realtime = ttk.Button(button_frame, text="Show Realtime Example", command=example_realtime)
button_realtime.pack(side="left", expand=True, fill="x", padx=(4, 0))

app.mainloop()