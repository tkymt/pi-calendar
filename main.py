from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont

inky = auto(ask_user=True, verbose=True)

image = Image.new("RGB", inky.resolution, (255, 255, 255))
draw = ImageDraw.Draw(image)

draw.line((0, 0) + image.size, fill=128)
draw.line((0, image.size[1], image.size[0], 0), fill=128)

font = ImageFont.truetype("./fonts/IBMPlexSansJP-Regular.otf", 24)
icon = ImageFont.truetype("./fonts/weathericons-regular.otf",72)
draw.multiline_text((10, 10), "Hello\nWorld!!", font=font,fill=(0, 0, 0))
draw.multiline_text((100, 100), '\uf00d', font=icon, fill=(255, 0, 0))
inky.set_image(image)
inky.show()
