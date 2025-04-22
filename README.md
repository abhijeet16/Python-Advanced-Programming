# Python-Advanced-Programming

This repository contains a collection of Python-based applications that demonstrate advanced programming concepts, including object-oriented programming, graphical user interfaces, and file handling. Each application is designed to solve a specific problem or provide a unique functionality. Below is a detailed overview of the projects included in this repository.

---

## Table of Contents
1. [Applications Overview](#applications-overview)
2. [Setup Instructions](#setup-instructions)
3. [Dependencies](#dependencies)
4. [Project Details](#project-details)
   - [Geometry Game](#geometry-game)
   - [Flatmates Bill Share](#flatmates-bill-share)
   - [Math Painting](#math-painting)
   - [Webcam Photo Sharer](#webcam-photo-sharer)
5. [Contributing](#contributing)
6. [License](#license)

---

## Applications Overview

This repository includes the following applications:

1. **Geometry Game**: A game that allows users to guess whether a point lies within a randomly generated rectangle and compare their guessed area with the actual area.
2. **Flatmates Bill Share**: A utility to calculate and generate a PDF report of bill shares between flatmates based on their stay duration.
3. **Math Painting**: A program to create a canvas and draw geometrical shapes like squares and rectangles with user-defined dimensions and colors.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Python-Advanced-Programming.git
   cd Python-Advanced-Programming
---

## Dependencies

The repository uses the following Python libraries:

- **NumPy**: For numerical operations in the Math Painting application.
- **Pillow**: For image creation and manipulation in the Math Painting application.
- **FPDF**: For generating PDF reports in the Flatmates Bill Share application.
- **Kivy**: For building graphical user interfaces in the Webcam Photo Sharer application.

Refer to the `requirements.txt` file in the `App4-Webcam_Photo_Sharer` directory for a complete list of dependencies.

---

## Project Details

### Geometry Game
- **Description**: A game where users guess if a point lies within a rectangle and estimate the rectangle's area.
- **Key Features**:
  - Randomly generated rectangles.
  - Graphical representation using the `turtle` module.
  - User interaction through console inputs.
- **File**: `App1-Geometry_Game/geometry_game.py`

---

### Flatmates Bill Share
- **Description**: Calculates and splits bills between flatmates based on their stay duration and generates a PDF report.
- **Key Features**:
  - Object-oriented design with `Bill`, `Flatmate`, and `PdfReport` classes.
  - PDF generation using the `FPDF` library.
- **Files**:
  - `Files/flat.py`
  - `Files/report.py`
  - `Files/main.py`

---

### Math Painting
- **Description**: Allows users to create a canvas and draw shapes like squares and rectangles with specified dimensions and colors.
- **Key Features**:
  - Uses NumPy for canvas creation and manipulation.
  - Saves the final canvas as an image file.
- **Files**:
  - `Files/canvas.py`
  - `Files/shapes.py`
  - `Files/main.py`

---

### Webcam Photo Sharer
- **Description**: A GUI application to display and manipulate images using Kivy.
- **Key Features**:
  - Interactive GUI built with Kivy.
  - Image manipulation and display.
- **Files**:
  - `frontend.kv`
  - `main.py`

---

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.