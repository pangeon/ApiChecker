from datetime import datetime
import os
import random

def write_to_file(data):
    date_mark = str(datetime.now().date()) + "-" + str(random.randint(0, 10000))
    file_name = date_mark + ".json"
    complete_path = os.path.join(os.getcwd() + r"\data_store\json" + "\\", file_name)
    print(complete_path)
    file = open(complete_path, "w", encoding="utf-8")
    file.write(str(data))
    file.close()
