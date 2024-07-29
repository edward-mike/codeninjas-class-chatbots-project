from datetime import datetime



class Storage:
    file_name = "storage.txt"
    datetime_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def to_txt(cls, text):
        file = open(cls.file_name,"+a")
        file.write(text + " - " + cls.datetime_stamp + "\n")
        file.close()

