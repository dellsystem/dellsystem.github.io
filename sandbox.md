---
layout: default
title: Sandbox
code: true
---

Ruby:
{% highlight ruby %}
puts "lol"
{% endhighlight %}

C:
{% highlight c %}
printf("test");
{% endhighlight %}

Cython:
{% highlight cython %}
cimport numpy
print "lol"
{% endhighlight %}

Python:
{% highlight python %}
#!/usr/bin/env python
import sys, os
from PIL import Image
import math

# Does all the image processing
# Just give it a directory of images in .tif/.tiff format that are not processed
# It will find the lowest max zoom, and resize all larger images to that zoom level
# Then it will convert all the images to pyramidal tiff format, and put them into a subdirectory
# Then it will copy everything from that subdirectory to /mnt/images/dir
# Run it as su (add this later)

def main(argv):
    # Handle the command line arguments
    if len(argv) < 2:
        print 'Usage: ./process.py directory'
        return 1 

    # Catch the argument
    directory = argv[1]

    # Create a directory called "processed" within that directory
    # If that directory already exists, fail
    if os.path.isdir(directory + '/processed'):
        print 'There already is a processed directory! Delete it and try again.'
        return 1
    else:
        os.system('mkdir ' + directory + '/processed')

    # Now get the contents of the directory
    files = os.listdir(directory)
    # Try to sort it
    files.sort()

    # Store the zooms of the files in a list
    # Use another list to store filenames (same indices etc)
    max_zoom_list = []
    filename_list = []

    for filename in files:
        try:
            this_max_zoom = get_max_zoom(directory + '/' + filename)
            print 'file: ' + filename + ' has max zoom of: ' + str(this_max_zoom - 1) + ' (' + str(this_max_zoom) + ' zoom levels)'
            max_zoom_list.append(this_max_zoom)
            filename_list.append(filename)
        except IOError:
            pass

    # Now get the absolute lowest max zoom
    lowest_max_zoom = min(max_zoom_list)

    # Now figure out which files have a zoom larger than that
    for i in range(len(filename_list)):
        input_file = directory + '/' + filename_list[i]
        output_file = directory + '/processed/' + directory + '_' + str(i+1) + '.tif'
        
        # If the image needs to be resized
        if max_zoom_list[i] > lowest_max_zoom:
            print filename_list[i] + ' needs to be resized, resizing and converting now'
            # Resize this image to the proper size ... prepend resized_
            resized_file = directory + '/resized_' + filename_list[i]
            resize_image(lowest_max_zoom, input_file, resized_file)

            # Now convert it
            os.system('vips im_vips2tiff ' + resized_file + ' ' + output_file + ':jpeg:75,tile:256x256,pyramid')
        else:
            # Just convert this image directly (the right size)
            print filename_list[i] + ' does not need to be resized, converting'
            os.system('vips im_vips2tiff ' + input_file + ' ' + output_file + ':jpeg:75,tile:256x256,pyramid')

    # Now print out the max_zoom this document has
    print "This document has a max zoom of: " + str(lowest_max_zoom)

# Calculate the maximum zoom of an image given its filepath
def get_max_zoom(filepath):
    # First, find the largest dimension of the image
    image = Image.open(filepath)
    width = image.size[0]
    height = image.size[1]
    largest_dim = width if width > height else height

    # Now figure out the number of zooms
    zoom_levels = math.ceil(math.log((largest_dim + 1) / (257.0), 2)) + 1
    return int(zoom_levels)

# Resize an image to the desired zoom
def resize_image(desired_zoom, input_file, output_file):
    # Figure out the maximum dimensions we can give it with this zoom
    max_dim = (2**(desired_zoom-1) * 257) - 1

    # Now get the image dimensions (again ...)
    image = Image.open(input_file)
    width = image.size[0]
    height = image.size[1]
    if width > height:
        largest_dim = width
        width_largest = True
    else:
        largest_dim = height
        width_largest = False

    # Now figure out the new dimensions
    if width_largest:
        # imagemagick will figure out the aspect ratio stuff
        new_dimensions = str(max_dim) + 'x' + str(height)
    else:
        new_dimensions = str(width) + 'x' + str(max_dim)
    
    # Now do the resizing
    os.system( 'convert -resize ' + new_dimensions + ' ' + input_file + ' ' + output_file)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
{% endhighlight %}

Javascript:
{% highlight javascript %}
// Testing jQuery
$('#lol').click(function() {
	$('#otherlol').hide();
});
{% endhighlight %}
