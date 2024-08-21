import os

def delete_non_tex_files (folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and not (filename.endswith('.tex') or filename.endswith('.md') or filename.endswith('.pdf')):
                os.remove(file_path)  
                print(f"Deleted: {file_path}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

def move_pdf_files (folder_path, build_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.pdf'):
                os.replace(file_path, os.path.join(build_path, f"physics_{filename[:-4]}.pdf"))  
                print(f"Moved: {file_path}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

delete_non_tex_files('./physics/01_lasers/latex/')
delete_non_tex_files('./physics/01_lasers/')
move_pdf_files('./physics/01_lasers/', './build/')