from ij import IJ, ImagePlus
from ij import WindowManager as wm
from ij.io import FileSaver
from os import path, mkdir

# important to convert to stack
img = wm.getCurrentImage()
stack = img.getImageStack()


# extract name and format from name
img_base_name = img.getTitle()
img_name = img_base_name[0:-4]
img_format = img_base_name[-4:]

# expand home tilde
out_dir = path.expanduser("~/bf_slices_out/")

# get current slice number
curr_slice = img.getSlice()

# create image name
out_img_name = img_name + "_z" + str(curr_slice) + img_format


# extract slice
stack_slice = stack.getProcessor(curr_slice)
# convert to ImagePlus
imp = ImagePlus(out_img_name, stack_slice)

#imp2.show()

filepath = path.join(out_dir, out_img_name)

if path.exists(out_dir) and path.isdir(out_dir):
	pass
else: mkdir(out_dir)

if path.exists(filepath):
	print "File exists! Not saving the image, would overwrite a file!"

  # have to save specific slice
elif FileSaver(imp).saveAsTiff(filepath):
    print "File saved successfully at ", filepath
