import os
import mailbox
from email import policy
from email.parser import BytesParser
import sys
import logging

# Set up logging
logging.basicConfig(filename='eml_to_mbox.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_banner():
    banner = r"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || | ____    ____ | || |   _____      | || |    _____     | || | ____    ____ | || |   ______     | || |     ____     | || |  ____  ____  | |
| | |_   ___  |  | || ||_   \  /   _|| || |  |_   _|     | || |   / ___ `.   | || ||_   \  /   _|| || |  |_   _ \    | || |   .'    `.   | || | |_  _||_  _| | |
| |   | |_  \_|  | || |  |   \/   |  | || |    | |       | || |  |_/___) |   | || |  |   \/   |  | || |    | |_) |   | || |  /  .--.  \  | || |   \ \  / /   | |
| |   |  _|  _   | || |  | |\  /| |  | || |    | |   _   | || |   .'____.'   | || |  | |\  /| |  | || |    |  __'.   | || |  | |    | |  | || |    > `' <    | |
| |  _| |___/ |  | || | _| |_\/_| |_ | || |   _| |__/ |  | || |  / /____     | || | _| |_\/_| |_ | || |   _| |__) |  | || |  \  `--'  /  | || |  _/ /'`\ \_  | |
| | |_________|  | || ||_____||_____|| || |  |________|  | || |  |_______|   | || ||_____||_____|| || |  |_______/   | || |   `.____.'   | || | |____||____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                       A simple EML to MBOX converter by Mario Bariša (https://barisa.me)
    """
    print(banner)

def print_progress_bar(iteration, total, length=50):
    percent = (iteration / total) * 100
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent:.2f}%')
    sys.stdout.flush()

def eml_to_mbox(eml_directory, mbox_file):
    # Create the directory for the MBOX file if it doesn't exist
    mbox_dir = os.path.dirname(mbox_file)
    if not os.path.exists(mbox_dir):
        os.makedirs(mbox_dir)

    # Create a new MBOX file
    mbox = mailbox.mbox(mbox_file)

    # Get the list of EML files
    eml_files = [f for f in os.listdir(eml_directory) if f.endswith('.eml')]
    total_files = len(eml_files)

    if total_files == 0:
        print("No EML files found in the specified directory.")
        return

    print("\nWARNING: This program will rename all EML filenames in the MBOX file based on the email header.")
    print("This application respects user privacy, and nothing is shared.")

    # Confirmation from the user
    confirmation = input("Type 'y' to confirm that you understand the implications: ")
    if confirmation.lower() != 'y':
        print("Operation cancelled.")
        return

    renamed_files_count = 0

    # Iterate through all EML files in the specified directory
    for i, filename in enumerate(eml_files):
        eml_path = os.path.join(eml_directory, filename)

        try:
            # Read the EML file
            with open(eml_path, 'rb') as eml_file:
                msg = BytesParser(policy=policy.default).parse(eml_file)

            # Get the subject header to use as the new filename
            subject = msg['subject']
            if subject:
                # Clean the subject to create a valid filename
                subject = ''.join(c if c.isalnum() or c in (' ', '.', '_', '-') else '_' for c in subject)
                new_filename = f"{subject}.eml"
                new_eml_path = os.path.join(eml_directory, new_filename)

                # Rename the EML file
                os.rename(eml_path, new_eml_path)
                renamed_files_count += 1
                logging.info(f"Renamed file: {filename} to {new_filename}")

            # Add the message to the MBOX
            mbox.add(msg)

            # Update progress bar
            print_progress_bar(i + 1, total_files)

        except Exception as e:
            print(f"\nError processing file {filename}: {e}")
            logging.error(f"Error processing file {filename}: {e}")

    # Close the MBOX file
    mbox.flush()
    mbox.close()

    # Summary report
    print("\nConversion completed!")
    print(f"Total files processed: {total_files}")
    print(f"Total files renamed: {renamed_files_count}")
    logging.info(f"Conversion completed: {total_files} files processed, {renamed_files_count} files renamed.")

if __name__ == "__main__":
    print_banner()
    # Specify the directory containing EML files and the output MBOX file
    eml_directory = input("Enter the directory containing EML files (without any quotes): ")
    mbox_file = input("Enter the output MBOX file path (e.g., /path/to/output.mbox, without any quotes): ")

    eml_to_mbox(eml_directory, mbox_file)
