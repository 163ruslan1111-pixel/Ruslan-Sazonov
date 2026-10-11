import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
src, out, x0, y0, x1, y1, lx, ly, lh, fs, angle = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:12])
x0,y0,x1,y1=map(int,(x0,y0,x1,y1))
im = Image.open(src).convert("RGB")
reg = im.crop((x0,y0,x1,y1))
clean = reg.filter(ImageFilter.MedianFilter(21)).filter(ImageFilter.GaussianBlur(4))
# card mask: pinkish pixels in the cleaned region
w,h = reg.size
m = Image.new("L",(w,h),0); mp=m.load(); cp=reg.filter(ImageFilter.MedianFilter(9)).load()
for y in range(h):
    for x in range(w):
        r,g,b = cp[x,y]
        if r>170 and r-g>18 and r-b>10: mp[x,y]=255
m = m.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(2))
# text layer
txt = Image.new("L",(w,h),0); d=ImageDraw.Draw(txt)
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", int(fs))
lines=["УБЕЖИЩЕ ГО №56","СЕМЬЯ ГРОМОВЫХ","3 МЕСТА"]
for i,l in enumerate(lines):
    tw = d.textlength(l,font=f)
    d.text((lx-x0 - tw/2, ly-y0 + i*lh), l, font=f, fill=200)
# stamp
cx,cy,r = w-fs*2.0, h-fs*1.6, fs*1.25
d2=Image.new("L",(w,h),0); dd=ImageDraw.Draw(d2)
dd.ellipse((cx-r,cy-r,cx+r,cy+r),outline=120,width=max(1,int(fs/8)))
import math
pts=[(cx+r*0.6*math.sin(math.radians(a*72))*(1 if a%1==0 else 1), cy-r*0.6*math.cos(math.radians(a*72))) for a in range(5)]
star=[pts[i] for i in (0,2,4,1,3)]
dd.polygon(star,fill=110)
txt = txt.rotate(angle, center=(w/2,h/2)).filter(ImageFilter.GaussianBlur(0.7))
d2 = d2.rotate(angle, center=(w/2,h/2)).filter(ImageFilter.GaussianBlur(0.7))
ink = Image.new("RGB",(w,h),(55,45,50)); stampc=Image.new("RGB",(w,h),(150,110,175))
card = Image.composite(ink, clean, txt)
card = Image.composite(stampc, card, d2)
res = Image.composite(card, reg, m)
im.paste(res,(x0,y0)); im.save(out)
