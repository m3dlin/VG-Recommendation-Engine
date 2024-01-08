# Get Rec'd  🎮

Get Rec'd is a [Steam](https://store.steampowered.com) video game recommendation engine and application. It takes games entered by the user and provides a list of 30 recommended games (10 per input) that are most similar in terms of features and characteristics.

## 🏆 Award-Winning Project

This project has been recognized and awarded **Best Data Science Project** at the Spring 2023 StMU CS Symposium


## 🛠️ Installation

1. Clone the repository using
```bash
git clone https://github.com/m3dlin/FlaskTutorial.git
```
2. Install all dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Run application by executing this command within the project
```bash
python3 src/gui.py
```
2. Input 3 games you have played before. This application must take 3 inputs and the inputs must be actual titles from Steam.

## ℹ️ How it Works
1. **Data Collection**: The application uses a dataset of games' features and characteristics. This list was collected from the developer using requests accessing [Steam Spy API](https://steamspy.com/api.php). The data was added to a comprehensive CSV file.
2. **Data Cleaning**: The data retrieved was a bit messy and had excessive amounts of unnecessary data. The developer narrowed down the data to what was needed (characteristics, genre, price, user scores, etc).
3. **Recommendation Engine**: This application leverages cosine similarity to generate game recommendations by comparing user-input games with a diverse set of games within the dataset. The comparison is based on the tags and genres associated with each game. Based on the computed similarity scores, the application suggests the top 10 games that have the highest similarity to the user-input games. This allows users to discover related games they might enjoy.

4. **GUI**: The GUI is simple and takes inputs from the user and will output the games in the following format - 
```
game_name  price: $0.00  rating: 00%  store link: https://store.steampowered.com/app/game_id/
```
At the bottom of the list, users can go back and input a new selection or save the 30 games as a text file to their downloads folder.

## 🔮 Future Work
- Currently, Get Rec'd uses a static and outdated (Spring 2023) dataset. I would like to incorporate more dynamic data that changes as the steam library changes. 
- Additionally, due to the time constraint I used cosine similarity. The downside is that this method only recommends the same 10 games per game you suggest. I would also like to add another recommendation engine that is more dynamic or updates which games are shown to the user.
- The current version of the application features a straightforward GUI for user interaction. While functional, there are opportunities for enhancing its usability and aesthetics to provide a more engaging and intuitive experience.

## 👥 Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
