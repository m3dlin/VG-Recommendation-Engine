"""
this module will display the gui that the user will see.
will ask user for 3 games they have played before,
and using the recommendation_engine.py, the gui will
display 10 recommendations as well as other information on the game
"""

from tkinter import *
from tkinter import messagebox, font
import webbrowser
import recommendation_engine as rec


def callback(url):
    webbrowser.open_new_tab(url)


# define a function to get the user's input and display the results
def get_recommendations_window():
    # get user input from the text boxes
    game1 = entry1.get()
    game2 = entry2.get()
    game3 = entry3.get()

    if game1 == '' or game2 == '' or game3 == '':
        error_message = messagebox.showinfo('error', "not all fields have been filled.")
        return
    elif not (rec.validate_name(game1)):
        error_message = messagebox.showinfo('error', "could not find game for game 1")
        return
    elif not (rec.validate_name(game2)):
        error_message = messagebox.showinfo('error', "could not find game for game 2")
        return
    elif not (rec.validate_name(game3)):
        error_message = messagebox.showinfo('error', "could not find game for game 3")
        return
    # THIS IS WHERE I ADD THE RECOMMENDATIONS
    index = rec.find_game_index(game1)
    game1_recommendations = rec.get_recommendations(index)
    game1_ids = rec.list_of_appids(index)

    index2 = rec.find_game_index(game2)
    game2_recommendations = rec.get_recommendations(index2)
    game2_ids = rec.list_of_appids(index2)

    index3 = rec.find_game_index(game3)
    game3_recommendations = rec.get_recommendations(index3)
    game3_ids = rec.list_of_appids(index3)

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
    results_label = Label(root, text="Your recommendations:", font=('TkDefaultFont', 26))
    results_label.pack()

    # Create a canvas widget with a scrollbar
    canvas = Canvas(root)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a frame inside the canvas to hold the scrollable content
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # scrollable content

    # -------------------GAME 1-----------------------------------------------------------------------------------
    game1_title_label = Label(frame, text='game1', font=('TkDefaultFont', 20))
    game1_title_label.pack(pady=15, anchor="center", expand=True)
    for i in range(len(game1_recommendations)):
        # new label to display new window with recommendations
        recommendations_label = Label(frame, text=game1_recommendations[i])
        recommendations_label.pack(pady=10)
        recommendations_label.bind("<Button-1>", lambda e: callback("https://store.steampowered.com/app/" + game1_ids[i]))

    # -------------------GAME 2-----------------------------------------------------------------------------------
    game2_title_label = Label(frame, text='game2', font=('TkDefaultFont', 20))
    game2_title_label.pack(pady=15, anchor="center", expand=True)
    for i in range(len(game2_recommendations)):
        # new label to display new window with recommendations
        recommendations_label = Label(frame, text=game2_recommendations[i])
        recommendations_label.pack(pady=10)
    # -------------------GAME 2-----------------------------------------------------------------------------------
    game3_title_label = Label(frame, text='game3', font=('TkDefaultFont', 20))
    game3_title_label.pack(pady=15, anchor="center", expand=True)
    for i in range(len(game3_recommendations)):
        # new label to display new window with recommendations
        recommendations_label = Label(frame, text=game3_recommendations[i])
        recommendations_label.pack(pady=10)
    # Configure the canvas to update its scroll region when the frame size changes
    frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    # update the label with the recommendations
    # recommendations_label.config(text='\n\n'.join(game1_recommendations))


#  main window and set its title
root = Tk()
root.title("Get Rec'd")
root.geometry("900x500")

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
submit_button = Button(root, text="Get Rec'd", command=get_recommendations_window)
submit_button.pack()

# run main
root.mainloop()
