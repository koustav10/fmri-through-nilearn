import os
import numpy as np
import nibabel as nib
from  matplotlib import pyplot as plt
from PIL import Image
from nilearn import plotting
from nilearn import image

                                        # interactively ask for the .nii file
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
                                        #from nibabel.testing import data_path

image1 = nib.load(filename)
print(image1.shape[:-1])			#image size in pixels
print(image1.get_data_dtype())	        #image data type

                                        # The get_data() function returns a standard NumPy multi-dimensional array, so you can treat it as you would any other ndarray.
image_data = image1.get_data()

#img = Image.fromarray(image_data)
#img

first_rsn = image.index_img(image1, 0)
plotting.plot_stat_map(first_rsn)
plotting.show()

