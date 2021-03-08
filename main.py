from tkinter import *

window = Tk()  # creates the window
window.title("Distance converter")  # Assign a title on the window
window.config(padx=20, pady=20)


def converter():
    number = input.get()  # gets the number entered by the user
    if radio_state.get() == 1:
        answer = float(number)*1.609  # converts to km
        rounded_answer = round(answer)  # rounds the answer to the nearest integer
        result.config(text=f"{rounded_answer}")  # sets the result label with the rounded answer as text
    elif radio_state.get() == 2:
        answer = float(number) / 1.609  # converts to mile
        rounded_answer = round(answer)  # rounds the answer to the nearest integer
        result.config(text=f"{rounded_answer}")    # sets the result label with the rounded answer as text


def change_layout():  # method changes the text of the labels according to which radio button is pressed
    if radio_state.get() == 1:
        label1.config(text="Miles")
        label3.config(text="Km")
    if radio_state.get() == 2:
        label1.config(text="Km")
        label3.config(text="miles")


# Radio buttons
radio_state = IntVar()  # Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Convert from miles to km", value=1, variable=radio_state, command=change_layout)
radiobutton2 = Radiobutton(text="Convert from km to miles", value=2, variable=radio_state, command=change_layout)
radiobutton1.grid(column=4, row=0)
radiobutton2.grid(column=9, row=0)


# Entry
input = Entry(width=10)  # creates an Entry widget
input.grid(column=6, row=2)

# Labels
label1 = Label(text="Miles", font=("Calibri", 24, "bold"))  # creates a component on the window
label1.grid(column=7, row=2)

label2 = Label(text="is equal to", font=("Calibri", 24, "bold"))  # creates a component on the window
label2.grid(column=5, row=3)

result = Label(text="")
result.grid(column=6, row=3)

label3 = Label(text="Km", font=("Calibri", 24, "bold"))  # creates a component on the window
label3.grid(column=7, row=3)

# Button
button = Button(text="Calculate", command=converter)
button.grid(column=6, row=4)


window.mainloop()  # This line keeps the GUI open on the screen
