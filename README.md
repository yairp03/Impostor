# Impostor

A Discord bot written in [discord.py](https://github.com/Rapptz/discord.py) for managing [Among Us](https://store.steampowered.com/app/945360/Among_Us/) games.

---

### Installation

1. Clone the repo

    ```bash
    git clone https://github.com/yairp03/Impostor.git
    ```

2. `cd` into the main directory and create the virtual environment

    ```bash
    # linux
    cd Impostor && python3 -m venv env

    # windows
    cd Impostor && python -m venv env
    ```

3. Activate the virtual environment

    ```bash
    # linux
    source env/bin/activate

    # windows
    env\Scripts\activate.bat
    ```

4. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```


### Running

1. Create a `.env` file with the following contents
    ```
    TOKEN="your_token"
    ```

2. Run the bot
    ```bash
    python3 impostor.py
    ```
