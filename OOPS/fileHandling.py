# with open("myfile.txt","w")as file:
#     file.write("this is line 1")
#     file.writelines(("\nthis is line 2","\nthis is line 3","\nthis is line 4 "))

import json

with open("OOPS/filehandling/file.txt", "r") as file:
        student ={
            "name": "John Doe",
            "age": 20,
            "grade": "A"
        }
        json.dump(student, file)
        print("json data inserted")

