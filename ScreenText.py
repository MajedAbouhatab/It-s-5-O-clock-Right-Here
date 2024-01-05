from lvgl import img, img_dsc_t, scr_act, label, ALIGN
from imagetools import open_png, get_png_info
from axpili9342 import ili9341

def UpdateLabel(b,s):
    if b:
        TopLabel.set_text(s)
    else:
        BottomLabel.set_text(s)

display = ili9341(factor=16)

driver = img.decoder_create()
driver.open_cb = open_png
driver.info_cb = get_png_info
with open('/cancun.png','rb') as f:
    raw_image = f.read()
image_description = img_dsc_t()
image_description.data = raw_image
image_description.data_size = len(raw_image)
image = img(scr_act())
image.set_src(image_description)

TopLabel = label(scr_act())
TopLabel.align(ALIGN.CENTER, 0, -106)
UpdateLabel(True,'Looking for Wi-Fi...')

BottomLabel = label(scr_act())
BottomLabel.align(ALIGN.CENTER, 0, 108)
UpdateLabel(False,'')
BottomLabel.set_long_mode(label.LONG.SCROLL_CIRCULAR)
BottomLabel.set_width(275)