import os

def delete_non_tex_files (folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and not filename.endswith('.tex'):
                os.remove(file_path)  
                print(f"Deleted: {file_path}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = './physics/01_lasers/latex/'

delete_non_tex_files(folder_path)