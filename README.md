This is a helper tool for the game Starfield.
It allows users to create a list of outpost modules,
    and calculates the crafting resources required to construct the list.

HOW TO RUN LOCALLY:
    This project written in Python 3.


    1. Install Python3 ( see https://www.python.org/downloads/ )

    2. (optional) virtual environment management:
        (the venv module is native to Python3 at the time of writing)

        2.1 create virtual environment

            [path/to/project/root]> python -m venv venv

        2.2 activate teh virtual environment

            # powershell -- may have to set execution policy first
            [path/to/project/root]> .\venv\Scripts\Activate.ps1

            # command line
            [path/to/project/root]> .\venv\Scripts\activate.bat

            # linux terminal
            [path/to/project/root]$ .\venv\Scripts\activate

        If successful, you should see something like,

        '(venv)[path/to/project/root]>' as your prompt

    3. Install dependencies:

        (venv)[path/to/project/root]> pip install -r requirements.txt

    4. Run the server:

        (venv)[path/to/project/root]/starfield_outpost_planner> python manage.py runserver

        should see lines like:

        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        July 30, 2024 - 18:54:38
        Django version 5.0.7, using settings 'starfield_outpost_planner.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

    5. Navigate to locally hosted website:

        in your browser of choice, navigate to
            http://127.0.0.1:8000/
