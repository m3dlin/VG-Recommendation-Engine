"""
this module will display the gui that the user will see.
will ask user for 3 games they have played before,
and using the recommendation_engine.py, the gui will
display 10 recommendations (per game) as well as other information on each game
"""
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser
import subprocess
import sys
import os
import getpass
import recommendation_engine as rec

# will be used to save recommendations into a txt file
recommendation_text = []


def callback(url):
    webbrowser.open_new_tab(url)


# used to restart program so user can enter different games
def restart_program():
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()


# define a function to get the user's input and display the results
def get_recommendations_window():
    # get user input from the text boxes
    game1 = entry1.get()
    game2 = entry2.get()
    game3 = entry3.get()

    # checks to see if all input fields are filled
    # it then checks each field to make sure the game is a valid title
    if game1 == '' or game2 == '' or game3 == '':
        messagebox.showinfo('error', "not all fields have been filled.")
        return
    elif not (rec.validate_name(game1)):
        messagebox.showinfo('error', "could not find " + game1 + " in the database")
        return
    elif not (rec.validate_name(game2)):
        messagebox.showinfo('error', "could not find " + game2 + " in the database")
        return
    elif not (rec.validate_name(game3)):
        messagebox.showinfo('error', "could not find " + game3 + " in the database")
        return

    # THIS IS WHERE I ADD THE RECOMMENDATIONS
    # ===========================================================
    # GAME 1
    index = rec.find_game_index(game1)
    game1_recommendations = rec.get_recommendations(index)
    game1_ids = rec.list_of_appids(index)
    # ===========================================================
    # GAME 2
    index2 = rec.find_game_index(game2)
    game2_recommendations = rec.get_recommendations(index2)
    game2_ids = rec.list_of_appids(index2)
    # ===========================================================
    # GAME 3
    index3 = rec.find_game_index(game3)
    game3_recommendations = rec.get_recommendations(index3)
    game3_ids = rec.list_of_appids(index3)
    # ===========================================================

    # pack_forget will "clear" the screen
    # remove the labels and entry widgets for the games
    logo_label.pack_forget()
    welcome_label.pack_forget()
    welcome_label2.pack_forget()
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
    results_label.pack(anchor='center')

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

    # ===================GAME 1===================================================================================
    recommendations_with_links = [
        (game1_recommendations[i], game1_ids[i], "https://store.steampowered.com/app/" + game1_ids[i]) for i in
        range(len(game1_recommendations))
    ]
    game1_title_label = Label(frame, text='Games like: ' + game1, font=('TkDefaultFont', 20))
    game1_title_label.pack(pady=15, anchor="center", expand=True)
    for recommendation, id, link in recommendations_with_links:
        recommendations_label = Label(frame, text=recommendation, cursor="hand2")
        recommendations_label.pack(pady=10, anchor='center')
        recommendations_label.bind("<Button-1>", lambda e, link=link: callback(link))
        recommendation_text.append(recommendation)
    # ===================GAME 2===================================================================================
    recommendations_with_links2 = [
        (game2_recommendations[i], game2_ids[i], "https://store.steampowered.com/app/" + game2_ids[i]) for i in
        range(len(game2_recommendations))
    ]
    game2_title_label = Label(frame, text='Games like: ' + game2, font=('TkDefaultFont', 20))
    game2_title_label.pack(pady=15, anchor="center", expand=True)
    for recommendation, id, link in recommendations_with_links2:
        recommendations_label = Label(frame, text=recommendation, cursor="hand2")
        recommendations_label.pack(pady=10, anchor='center')
        recommendations_label.bind("<Button-1>", lambda e, link=link: callback(link))
        recommendation_text.append(recommendation)
    # ===================GAME 3===================================================================================
    recommendations_with_links3 = [
        (game3_recommendations[i], game3_ids[i], "https://store.steampowered.com/app/" + game3_ids[i]) for i in
        range(len(game3_recommendations))
    ]
    game3_title_label = Label(frame, text='Games like: ' + game3, font=('TkDefaultFont', 20))
    game3_title_label.pack(pady=15, anchor="center", expand=True)
    for recommendation, id, link in recommendations_with_links3:
        recommendations_label = Label(frame, text=recommendation, cursor="hand2")
        recommendations_label.pack(pady=10, anchor='center')
        recommendations_label.bind("<Button-1>", lambda e, link=link: callback(link))
        recommendation_text.append(recommendation)
    # ============================================================================================================

    # save games to a txt file, will be saved to user downloads folder
    save_button = Button(frame, text="Save Games", command=save_as_txt)
    save_button.pack()
    # go back to main window
    back_button = Button(frame, text="Go Back", command=restart_program)
    back_button.pack()

    # configure the canvas to update its scroll region when the frame size changes
    frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))


def save_as_txt():
    # finds downloads folder path
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # if there is no path, return
    if not downloads_folder:
        return
    # used to add username of the computer to the txt file
    username = getpass.getuser()

    # Save games to downloads folder
    filename = "recommendation_list.txt"
    file_path = os.path.join(downloads_folder, filename)
    with open(file_path, "w") as f:
        f.write(f"{username}'s Recommendation List\n\n")
        # writes recommendation format in the txt file
        for rec in recommendation_text:
            f.write(rec + '\n\n')

    # ensure user understands that the file was saved
    messagebox.showinfo('showinfo', "your games list has been saved")


################
# ----MAIN----
################
# root window and set its title
root = Tk()
root.title("Get Rec'd")
root.geometry("900x500")
logo = Image.open("steam_logo.jpg")
resized_logo = logo.resize((400, 150))
test = ImageTk.PhotoImage(resized_logo)

logo_label = Label(image=test)
logo_label.pack()
# displays what this program is
welcome_label = Label(root, text="\nWelcome to Get Rec'd!", justify='center',font=('TkDefaultFont', 20))
welcome_label2 = Label(root,text="This is a video game recommendation engine that takes "
                                 "3 games that you've played\n and gives you 10 "
                                 "recommendations per game\n", justify='center')
welcome_label.pack()
welcome_label2.pack()

# labels and text boxes for the user to input games

# GAME 1
label1 = Label(root, text="Enter Game 1:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
# GAME 2
label2 = Label(root, text="Enter Game 2:")
label2.pack()
entry2 = Entry(root)
entry2.pack()
# GAME 3
label3 = Label(root, text="Enter Game 3:")
label3.pack()
entry3 = Entry(root)
entry3.pack()

# Create a button to submit the input and generate recommendations
submit_button = Button(root, text="Get Rec'd", command=get_recommendations_window)
submit_button.pack()

# run main
root.mainloop()

# testing