from domains.Student import Student
from domains.Course import Course
import gzip
import os

def studentsToFile(students):
    try:
        print("Saving student's information to 'students.txt'")
        f = open("students.txt", "w+")
        for idx, student in enumerate(students, start=1):
            f.write(f"{idx}. {student.getName()}" + "\r")
            f.write(student.getID() + "\r")
            f.write(student.getDob() + "\n")
        print("Saved")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close()
        
        
def coursesToFile(courses):
    try:
        print("Saving course's information to 'courses.txt'")
        f = open("courses.txt", "w+")
        for idx, course in enumerate(courses, start=1):
            f.write(f"{idx}. {course.getName()}" + "\r")
            f.write(course.getID() + "\n")
        print("Saved")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close()
        
        
def marksToFile(courses):
    try:
        print("Saving marks to 'marks.txt'")
        f = open("marks.txt", "w+")
        for course in courses:
            marks = course.getMarks()
            for student_id in marks.key():
                f.write(student_id + "\n")
                for mark in marks[student_id]:
                    f.write(mark + "\r")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f.close()

        
def compress(input_files, compressed_file):
    with gzip.open(compressed_file, "wb") as f_out:
        for file in input_files:
            with open(file, "rb") as f_in:
                content = f_in.read()
            filename = os.path.basename(file).encode() # Extract the file name from path and encode it to bytes
            f_out.write(len(filename)).to_bytes(4, byteorder="big")
            f_out.write(filename)
            f_out.write(len(content)).to_bytes(8, byteorder="big")
            f_out.write(content)
    print("Done")
    

def decompress(compressed_file, output_folder):
    with gzip.open(compressed_file, "rb") as f_in:
        while True:
            # Read the file name's length (first 4 bytes)
            filename_length_bytes = compressed_file.read(4)
            if not filename_length_bytes:
                break
            
            filename_length = int.from_bytes(filename_length_bytes, byteorder="big")
            
            # Read the file name
            filename = compressed_file.read(filename_length).decode()
            
            # Read the file size
            file_size = int.from_bytes(compressed_file.read(8), byteorder="big")
            
            # Read the content of the file
            content = compressed_file.read(file_size)
            
            with open(os.path.join(output_folder, filename), "wb") as f_out:
                f_out.write(content)
        
        print("Done")