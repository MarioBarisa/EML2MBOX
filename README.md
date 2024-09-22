# EML2MBOX Converter

**EML2MBOX** is a simple command-line tool that converts EML files to MBOX format. This program is designed to help users manage their email files efficiently while respecting user privacy.

## Features

- **Batch Conversion**: Convert multiple EML files to a single MBOX file.
- **File Renaming**: Automatically renames EML files based on the email subject header for better organization.
- **Progress Bar**: Visual feedback during the conversion process with a progress bar.
- **Logging**: Logs important events, errors, and warnings to a log file for easy tracking.
- **User Privacy**: The application does not share any user data or files.
- **Error Handling**: Gracefully handles errors during file processing and provides informative messages.

## How to Use

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- This program uses built-in Python libraries, so no additional installations are required.

### Step-by-Step Instructions

1. **Clone the Repository**:
   Open your terminal or command prompt and run the following command to clone the repository:
   ```bash
   git clone https://github.com/yourusername/EML2MBOX.git
   ```
   Replace `yourusername` with your actual GitHub username.

2. **Navigate to the Project Directory**:
   Change into the project directory:
   ```bash
   cd EML2MBOX
   ```

3. **Prepare Your EML Files**:
   Gather all the EML files you want to convert and place them in a single directory.
   Make sure the directory path does not contain any special characters or spaces that could cause issues.

4. **Run the Program**:
   Execute the program by running the following command:
   ```bash
   python eml_to_mbox.py
   ```

5. **Input Directory**:
   When prompted, enter the full path to the directory containing your EML files.
   Example: `/path/to/your/eml/files` (do not include quotes).

6. **Output File Path**:
   Next, enter the desired output path for the MBOX file.
   Example: `/path/to/output.mbox` (do not include quotes).

7. **Confirm Your Choices**:
   The program will display a warning message indicating that it will rename EML files based on the email subject header.
   Type `y` and press Enter to confirm that you understand the implications of this action.

8. **Monitor the Conversion Process**:
   The program will display a progress bar as it processes each EML file.
   If any errors occur during processing, they will be displayed in the terminal.

9. **Check the Log File**:
   After the conversion is complete, a log file named `eml_to_mbox.log` will be created in the project directory.
   Open this file to review a summary of the operation, including any errors encountered and the number of files processed.

10. **Locate Your MBOX File**:
    The converted MBOX file will be located at the path you specified in step 6.
