import os

BUILD_PATH = './build/'

PHY_CHAPTERS = ['lasers']
MATH_CHAPTERS = ['diff_eqns']

def delete_non_tex_files (folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and not (filename.endswith('.tex') or filename.endswith('.md') or filename.endswith('.pdf')):
                os.remove(file_path)  
                print(f"Deleted: {file_path}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

def move_pdf_files (folder_path, subject):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.pdf'):
                os.replace(file_path, os.path.join(BUILD_PATH, f"{subject}_{filename[:-4]}.pdf"))  
                print(f"Moved: {file_path}")
                
    except Exception as e:
        print(f"An error occurred: {e}")

def build_subject (subject, chapters):
    for i, chapter in enumerate(chapters, start=1):
        folder = f"{f"0{str(i)}" if i < 10 else str(i)}_{chapter}"
        folder_path = f"./{subject}/{folder}/"

        print(f"Building: {folder_path}")

        delete_non_tex_files(folder_path)
        delete_non_tex_files(folder_path + 'latex/')
        move_pdf_files(folder_path, subject)

        print("Build Complete\n")

build_subject("physics", PHY_CHAPTERS)
build_subject("maths", MATH_CHAPTERS)