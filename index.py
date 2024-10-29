import os
import datetime

def write_image_names_to_file(folder_path, output_file):
    # List of common image file extensions
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp']

    # Extract the folder name from the folder_path
    folder_name = os.path.basename(folder_path)

    try:
        # Open the output file in write mode with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as file:
            # Loop through each file in the folder
            for filename in os.listdir(folder_path):
                # Check if the file has an image extension
                if any(filename.lower().endswith(ext) for ext in image_extensions):
                    # Get the full file path
                    file_path = os.path.join(folder_path, filename)
                    
                    # Get the file modification date
                    file_mod_time = os.path.getmtime(file_path)
                    file_date = datetime.datetime.fromtimestamp(file_mod_time).strftime('%Y-%m-%d')
                    
                    # Write the image details in the desired format
                    file.write(f'{{ src: "storage/images/events/{folder_name}/{filename}", alt: "{folder_name}", title: "{folder_name}", description: "{folder_name}", date: "{file_date}", category: "{folder_name}" }},\n')

        print(f"Image names have been written to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your folder path and output file name
folder_path = r'C:\path\to\your\image\folder'
output_file = r'C:\path\to\your\output\file.txt'

write_image_names_to_file(folder_path, output_file)
