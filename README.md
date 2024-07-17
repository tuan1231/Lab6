# Data Entry Form Application

## Overview

This is a simple Tkinter-based GUI application for data entry. The application allows users to input personal information, registration status, and accept terms and conditions before submitting the data. The form includes fields for first name, last name, title, age, nationality, registration status, number of completed courses, and number of semesters. Additionally, it features a screen recording function.

## Features

- User Information Section
  - First Name
  - Last Name
  - Title (Mr., Mrs., Ms., Dr.)
  - Age (Spinbox)
  - Nationality

- Registration Status Section
  - Currently Registered (Checkbox)
  - Number of Completed Courses (Spinbox)
  - Number of Semesters (Spinbox)

- Terms & Conditions Section
  - Accept terms and conditions (Checkbox)

- Submit Button
  - Validates if terms and conditions are accepted
  - Displays the entered data in the console

- Screen Recording Function
  - Start and stop screen recording

## Requirements

- Python 3.x
- Tkinter
- Pillow
- OpenCV
- pyautogui

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/data-entry-form.git
    cd data-entry-form
    ```

2. Install the required libraries:
    ```bash
    pip install pyautogui opencv-python pillow
    ```

## Usage

1. Navigate to the project directory:
    ```bash
    cd data-entry-form
    ```

2. Run the application:
    ```bash
    python main.py
    ```

3. Fill out the form with the required information.

4. Accept the terms and conditions.

5. Click on the "Enter data" button to submit the data.

6. Use the "Record Screen" button to start and stop screen recording.

## Screenshots

![Application Screenshot](path/to/screenshot.png)

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Tkinter for the GUI framework
- OpenCV and pyautogui for screen recording capabilities
