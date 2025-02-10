from PIL import Image, ImageFilter, ImageEnhance

with Image.open("Figma-logo.svg.png") as picture:
    #picture.show()

    black_white=picture.convert("L")
    black_white.save("gary.png")

    mirror=picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("mirror.png")

    blur=picture.filter(ImageFilter.BLUR)
    blur.save("blur.png")
    

    #imageEnhance

    contrast=ImageEnhance.Contrast(picture)
    contrast=contrast.enhance(2.5)
    contrast.save("contrast.png")

    color=ImageEnhance.Color(picture).enhance(2.5)
    color.save("color.png")