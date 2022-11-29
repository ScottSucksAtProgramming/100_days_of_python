####################################################################
# Resources
####################################################################
import tkinter

####################################################################
# Functions
####################################################################


def calc_km():
    kilo = round(int(entry.get()) * 1.609344, 2)
    answer.config(text=kilo)


####################################################################
# tkinter Layout
####################################################################

# And Scott said, "Let there be a window," and it was good
window = tkinter.Tk()
window.title("Mile to Kilometer Conversion Machine")
window.minsize(width=600, height=600)

# Next, Scott created an Entry Box, and there was must rejoicing
entry = tkinter.Entry(width=30)
entry.insert(0, string="0")
entry.grid(column=1, row=0)
entry.focus()
# In which, Scott creates some labels to elucidate this program's divine purpose.
miles = tkinter.Label(text="miles")
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

answer = tkinter.Label(text="X")
answer.grid(column=1, row=1)

km = tkinter.Label(text="kilometers")
km.grid(column=2, row=1)

# Behold! The mighty, Button!!!
button = tkinter.Button(text="Do the thing!!", command=calc_km)
button.grid(column=1, row=3)
####################################################################
# Functionality Code
####################################################################

window.mainloop()