from domains.Student import Student
from domains.Course import Course
import pickle
import gzip


def pickleAndCompress(students, courses, filename):
    try:
        print(f"Saving data to '{filename}'")
        with gzip.open(f"{filename}", "wb") as f_in:
            pickle.dump((students, courses), f_in)
        print("Saved")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f_in.close()
        

def decompressAndUnpickle(filename):
    students, courses = [], []
    print(f"Reading data from '{filename}'")
    try:
        with gzip.open(f"{filename}", "rb") as f_in:
            students, courses = pickle.load(f_in)
        print("Done reading")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        f_in.close()
        return students, courses