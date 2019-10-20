import tkinter as tk

window = tk.Tk()
window.title("Compound interest formula")

tk.Label(window, text="Calculate",
              fg="white", bg="black").grid(row=1)

principal = tk.StringVar()
principal.set("100")

interest_rate = tk.StringVar()
interest_rate.set("0.4")

number_of_compound_times = tk.StringVar()
number_of_compound_times.set("2")

total_time = tk.StringVar()
total_time.set("5")

def compounded ():
    p = float(principal.get())
    r = float(interest_rate.get())
    n = float(number_of_compound_times.get())
    t = float(total_time.get())

    amount = round(p*((1+(r/n))**(n*t)), 2)
    tk.Label(window, text="Total amount: $"+str(amount)).grid(row=10)
    return

tk.Label(window, text="Principal amount: ").grid(row=2)
tk.Entry(window, textvariable=principal).grid(row=2, column=1)

tk.Label(window, text="Interest rate: ").grid(row=3)
tk.Entry(window, textvariable=interest_rate).grid(row=3, column=1)

tk.Label(window, text="Number of times interest is compounded : ").grid(row=4)
tk.Entry(window, textvariable=number_of_compound_times).grid(row=4, column=1)

tk.Label(window, text="Total time: ").grid(row=5)
tk.Entry(window, textvariable=total_time).grid(row=5, column=1)

tk.Button(window, text="Calculate", command=compounded).grid(row=8, column=1)

window.mainloop()
