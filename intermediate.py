import qrcode
import qrcode.image.svg as sv

#method to choose which factory method to use
method = "path"

data = "This is for qr code generation"

if method == 'basic':
    #just a set of rects.
    factory = sv.SvgImage
elif method == 'fragment':
    #also just a set of rects
    factory = sv.SvgFragmentImage
elif method == 'path':
    # Combined path factory, fixes white space that may occur when zooming
    factory = sv.SvgPathImage


img = qrcode.make(data, image_factory = factory)


img.save("A:/Qr code generator/intermediate.svg")
