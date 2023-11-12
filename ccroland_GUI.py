print('Carliana Roland, 5/1/23, COMP163, Python GUI', '\n')
#SETUP
from tkinter import *  # tkinter is to be imported to create GUI's

# ROOT
# root is the main widget/ the window (below)
root = Tk()  # this function instantiate a root widget

def btnEnableCommand():  # making cause/ effect with the button
    lblButtonClicked = Label(root, text="If you\'re ever afraid of clowns, always remember: If Sam could do it, "
                                        "you can too! What would you have done if you were Sam? Answer in the entry "
                                        "above the button and re-click the button!")
    lblButtonClickedEntry = Label(root, text=entData.get())  # the get() would be able for the user to interact with the
    # interface
    lblButtonClickedEntry.pack()
    lblButtonClicked.pack()  # placing label on root

# makes a clickable button below
btnEnable = Button(root, text="When done reading, click here for a message!", command=btnEnableCommand)
# command causes function to run after button is clicked^^
entData = Entry(root, borderwidth=5)  # makes the entry for typing
entData.pack()
btnEnable.pack()  # puts widget on screen

# WIDGET
# putting a widget on a GUI
btnDisable = Button(root, text="Sorry, you can\'t click here. You\'re not registered as a member yet. Want to become a"
                               "member? Sign up today on our site or mobile app!", padx=50, state=DISABLED)
# padx and y makes the button wider or taller(bigger)^^
lblSupernaturalpt1 = Label(root, text="Castiel and Sam make their way pass the wall with the mother and child while "
                                      "being chased by the monsters.", pady=50)  # makes an unclickable button
lblSupernaturalpt2 = Label(root, text="The killer clown tries to stab them when he realizes he can\'t.")
lblSupernaturalpt3 = Label(root, text="In anger he screams in Sam's face.")
lblSupernaturalpt4 = Label(root, text="Sam looks at the clown in slight terror and says, 'Shut Up'.")  # root will
# contain the label
# (lbl) - the prefix for label which is readability of a program^^
# label with "Sam looks at the clown in fear and says, 'Shut Up'." as the text^^

# TODO: put label on container by placing it on root using pack
# PACK
btnDisable.pack()
lblSupernaturalpt1.pack()  # places label on the root
lblSupernaturalpt2.pack()
lblSupernaturalpt3.pack()
lblSupernaturalpt4.pack()

root.mainloop()  # creates event loop (infinite loop or while true loop)
# this will fire when an evnet happens ^^

lblSupernaturalpt1.grid(row=0, column=0)  # the grid lines up the quotes to be read correctly
lblSupernaturalpt2.grid(row=1, column=0)
lblSupernaturalpt3.grid(row=2, column=0)
lblSupernaturalpt4.grid(row=3, column=0)










