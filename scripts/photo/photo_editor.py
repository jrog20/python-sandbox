# Photo Editor
# pip install Pillow

# The Pillow module provides the following set of predefined image enhancement filters:

# BLUR
# CONTOUR
# DETAIL
# EDGE_ENHANCE
# EDGE_ENHANCE_MORE
# EMBOSS
# FIND_EDGES
# SMOOTH
# SMOOTH_MORE
# SHARPEN

from PIL import Image, ImageFilter

def blurred():
    try:
        # Load an image from the hard drive
        original = Image.open("images/whiskers.png")

        # Blur the image
        blurred = original.filter(ImageFilter.BLUR)

        # Display both images
        original.show()
        blurred.show()

        # save the new image
        blurred.save("blurred.png")

    except:
        print("Unable to load image")

##########################################################
# create a thumbnail
def thumbnail():
    size = (128, 128)
    original = "images/peri.png"

    try:
        small = Image.open(original)
    except:
        print("Unable to load image")

    small.thumbnail(size)
    small.save("images/thumbnamil.png")
    small.show()

##########################################################
# Blog suggestions

# # Crop
# def crop():
#     myimage = Image.open('photo.jpg')
#     pic.crop((20, 20, 20, 20)).save('test_crop.jpg')

# # Resize
# def resize():
#     pic= Image.open('photo.jpg')
#     pic.resize((200, 200)).save('test_resize.jpg')

# # Flip
# def flip():
#     pic= Image.open('photo.jpg')
#     pic.transpose(Image.FLIP_LEFT_RIGHT).save('test_flip.jpg')

# # Rotate
# def rotate():
#     pic= Image.open('photo.jpg')
#     pic.rotate(90).save('test_rotate.jpg')

# # Add Text to Image
# def add_text():
#     pic= Image.open('photo.jpg')
#     font= Image.font('arial.ttf', 20)
#     draw= ImageDraw.Draw(pic)
#     draw.text((10, 10), 'Hello World', font=font, fill=(255, 0, 0))
#     pic.save('test_text.jpg')

# # Convert to Grey Scale
# def grey_scale():
#     photo = Image.open('whiskers.jpg')
#     photo.convert(mode=Image.L).save('grey_whiskers.jpg')

# # Sharpen
# def sharpen():
#     pic= Image.open('photo.jpg')
#     pic.filter(ImageFilter.SHARPEN).save('test_sharp.jpg')

# # Merge Images
# def merge():
#     pic1= Image.open('photo.jpg')
#     pic2= Image.open('photo.jpg')
#     Image.alpha_composite(pic1, pic2).save('test_merge.jpg')

##########################################################
if __name__ == "__main__": 
    thumbnail()