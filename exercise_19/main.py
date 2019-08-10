from PIL import Image, ImageDraw, ImageFont

# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', 24)


# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image, text, font=font):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(76, 234, 124, 180))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text


im_before = Image.open("uouo123.jpg")
im_before.show()
im_after = add_text_to_image(im_before, 'blog.uouo123.com')
im_after.show()

def add_watermark_to_image(image, watermark):
    rgba_image = image.convert('RGBA')
    rgba_watermark = watermark.convert('RGBA')

    image_x, image_y = rgba_image.size
    watermark_x, watermark_y = rgba_watermark.size

    # 缩放图片
    scale = 10
    watermark_scale = max(image_x / (scale * watermark_x), image_y / (scale * watermark_y))
    new_size = (int(watermark_x * watermark_scale), int(watermark_y * watermark_scale))
    rgba_watermark = rgba_watermark.resize(new_size, resample=Image.ANTIALIAS)
    # 透明度
    rgba_watermark_mask = rgba_watermark.convert("L").point(lambda x: min(x, 180))
    rgba_watermark.putalpha(rgba_watermark_mask)

    watermark_x, watermark_y = rgba_watermark.size
    # 水印位置
    rgba_image.paste(rgba_watermark, (image_x - watermark_x, image_y - watermark_y), rgba_watermark_mask)

    return rgba_image


im_before = Image.open("uouo123.jpg")
im_before.show()

im_watermark = Image.open("blog.jpg")
im_after = add_watermark_to_image(im_before, im_watermark)
im_after.show()
# im.save('im_after.jpg')
