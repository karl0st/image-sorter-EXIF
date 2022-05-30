import os, shutil
from exif import Image

cur_dir = os.getcwd() + "\\"

def rename_image(file):
    print("Renaming '" + file + "'")
    img = Image(file)

    if img.has_exif:
        dateTime = img.get("datetime_original")
        dateTime = str(dateTime).replace(":", "-")
        os.rename(file, dateTime[2:] + ".JPG")
    else:
        if not os.path.exists(os.path.join(cur_dir, "no_EXIF")):
            os.mkdir(os.path.join(cur_dir, "no_EXIF"))

            shutil.move(cur_dir + file, cur_dir + "no_EXIF" + "\\" + file)

def sort_images_year(file):
    print("Sorting '" + file + "' by year")
    img = Image(file)
    dateTime = img.get("datetime_original")
    year = dateTime[0:4]

    if not os.path.exists(os.path.join(cur_dir, year)):
        os.mkdir(os.path.join(cur_dir, year))

    shutil.move(cur_dir + file, cur_dir + year + "\\" + file)

def sort_images_month(file):
    print("Sorting '" + file + "' by month")
    img = Image(file)
    dateTime = img.get("datetime_original")
    month = dateTime[5:7]

    if not os.path.exists(os.path.join(cur_dir, month)):
        os.mkdir(os.path.join(cur_dir, month))

    shutil.move(cur_dir + file, cur_dir + month + "\\" + file)

os.chdir(cur_dir)

for file in os.listdir():
    if os.path.splitext(file)[1] == ".jpg" or os.path.splitext(file)[1] == ".JPG":
        rename_image(file)
        # sort_images_year(file)
        # sort_images_month(file)
    else:
        if os.path.isdir(file):
            print("'" + file + "' is a directory and cannot be moved.")
        else:
            print("'" + file + "'" + "is not in JPG format. Moving into 'unsorted'.")
            if not os.path.exists(cur_dir + "unsorted"):
                os.mkdir(cur_dir + "unsorted")
            shutil.move(cur_dir + file, cur_dir + "unsorted" + "\\" + file)
