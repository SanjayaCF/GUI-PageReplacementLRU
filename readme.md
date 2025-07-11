# LRU Page Replacement Simulator

This project is a graphical user interface (GUI) application that simulates the Least Recently Used (LRU) page replacement algorithm. It's designed to help visualize how the LRU algorithm works by allowing users to input a reference string and the number of frames, and then see a step-by-step simulation of the cache states, hits, and misses.

-----

## Features

  * **Interactive Simulation:** Input your own reference strings and number of frames to see the LRU algorithm in action.
  * **Step-by-Step Visualization:** The simulation displays each step, showing the page, the state of the LRU cache, and whether it was a "hit" or a "miss."
  * **Detailed Statistics:** Get a summary of the simulation, including:
      * Total References
      * Total Distinct References
      * Number of Hits
      * Number of Faults (Misses)
      * Hit Rate (%)
      * Fault Rate (%)
  * **Two GUI Options:** Choose between a simple, single-window interface (`gui.py`) or a tabbed notebook interface (`guiNotebook.py`) that includes an introduction page.

-----

## Technologies Used

  * **Python**
  * **Tkinter:** The standard Python interface to the Tk GUI toolkit.
  * **customtkinter:** A modern and customizable UI-library for Tkinter.

-----

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You will also need to install the `customtkinter` library.

```bash
pip install customtkinter
```

### Running the Application

1.  Clone the repository or download the source code.

2.  Navigate to the project directory.

3.  You can run either of the GUI applications:

    For the simple interface:

    ```bash
    python gui.py
    ```

    For the notebook interface with an introduction page:

    ```bash
    python guiNotebook.py
    ```

-----

## How to Use

1.  Enter the **reference string** in the first input field (e.g., "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1").
2.  Enter the number of **frames** in the second input field (e.g., "3").
3.  Click the **"Simulasi Jadwal"** (Simulate Schedule) button to run the simulation.
4.  The results of the simulation will be displayed in a table on the same page.

-----

## Project Files

  * **`script.py`**: This file contains the core logic for the LRU page replacement algorithm simulation.
      * The `AlgoritmaLRU` class has methods to simulate the cache, calculate page faults, and prepare the output for display.
  * **`gui.py`**: This script creates a simple, single-window GUI for the LRU simulation.
  * **`guiNotebook.py`**: This script provides a tabbed GUI. The first tab is an introduction page with project and team details, and the second tab contains the LRU simulation.
  * **`readme.md`**: Project documentation (the file you are currently reading).

-----

## Team

  * Rendy Ananta Kristanto - 71220840
  * Vittorio Emmanuel Harianto - 71220912
  * Leif Sean Kusumo - 71220915
  * Sanjaya Cahyadi Fuad - 71220965
