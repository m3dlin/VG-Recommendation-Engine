"""
this module will display the gui that the user will see.
will ask user for 3 games they have played before,
and using the recommendation_engine.py, the gui will
display 10 recommendations as well as other information on the game
"""

from tkinter import *
from tkinter import messagebox


# define a function to get the user's input and display the results
def get_recommendations():
    # get user input from the text boxes
    game1 = entry1.get()
    game2 = entry2.get()
    game3 = entry3.get()

    if game1 == '' or game2 == '' or game3 == '' or game4 == '' or game5 == '':
        error_message = messagebox.showinfo('error', "not all fields have been filled.")
        return
    # THIS IS WHERE I ADD THE RECOMMENDATIONS
    #  = get_recommendations(game1, game2, game3, game4, game5)
    recommendations = ["Stardew Valley", "Core Keeper"] # return an array of strings

    # remove the labels and entry widgets for the games
    welcome_label.pack_forget()
    label1.pack_forget()
    entry1.pack_forget()
    label2.pack_forget()
    entry2.pack_forget()
    label3.pack_forget()
    entry3.pack_forget()

    # Remove the submit button
    submit_button.pack_forget()

    # label to display the recommendations
    results_label = Label(root, text="Your recommendations:")
    results_label.pack()

    # new label to display new window with recommendations
    recommendations_label = Label(root, text="")
    recommendations_label.pack()

    # update the label with the recommendations
    recommendations_label.config(text='\n'.join(recommendations))


#  main window and set its title
root = Tk()
root.title("Get Rec'd")
root.geometry("600x400")

# displays what this program is
welcome_label = Label(root, text="\n\nWelcome to my CS4375 project.\n"
                                 "This is a video game recommendation engine that takes "
                                 "3 games that you've played\n and gives you 10 "
                                 "recommendations on what other games you may like.", justify='center')
welcome_label.pack()

# labels and text boxes for the user to input games
label1 = Label(root, text="Enter Game 1:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter Game 2:")
label2.pack()
entry2 = Entry(root)
entry2.pack()

label3 = Label(root, text="Enter Game 3:")
label3.pack()
entry3 = Entry(root)
entry3.pack()


# Create a button to submit the input and generate recommendations
submit_button = Button(root, text="Get Rec'd", command=get_recommendations)
submit_button.pack()

# run main
root.mainloop()
