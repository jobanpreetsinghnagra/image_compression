#logic to check image format
import os
from PIL import Image

filepaths = ["test.jpg", "test.png"]

for fp in filepaths:
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(fp)[-1].lower()

    # Now we can simply use == to check for equality, no need for wildcards.
    if ext == ".png":
        print (fp, "is an png!")
    elif ext == ".jpeg" or ext == ".jpg":
        print (fp, "jpeg file")
        img = Image.open(fp)
        img.save('changed.png')