import sys
import numpy as np
from PIL import Image, ImageFilter
src,out = sys.argv[1],sys.argv[2]
x0,y0,x1,y1, tx,ty,tw, ang, blur = map(float, sys.argv[3:12])
x0,y0,x1,y1=map(int,(x0,y0,x1,y1))
im = Image.open(src).convert("RGB")
reg = im.crop((x0,y0,x1,y1))
w,h = reg.size
clean = reg.filter(ImageFilter.MedianFilter(21)).filter(ImageFilter.GaussianBlur(3))
med = np.asarray(reg.filter(ImageFilter.MedianFilter(17))).astype(float)
pink = ((med[...,0]>170)&(med[...,0]-med[...,1]>18)&(med[...,0]-med[...,2]>10)).astype(np.uint8)*255
m = Image.fromarray(pink).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.5))
# ink from the real coupon reference: text block + stamp
c = Image.open("/home/user/Ruslan-Sazonov/shelter56/refs/coupon.png").convert("RGB").crop((870,520,2030,1290))
ca = np.asarray(c).astype(float)
paper = np.asarray(c.filter(ImageFilter.MedianFilter(31)).filter(ImageFilter.GaussianBlur(10))).astype(float)
ink = np.clip(ca/np.maximum(paper,1),0,1)          # 1 = paper, <1 = ink
th = int(round(tw*c.size[1]/c.size[0]))
inkim = Image.fromarray((ink*255).astype(np.uint8)).resize((int(tw),th), Image.LANCZOS)
inkim = inkim.rotate(ang, expand=True, fillcolor=(255,255,255)).filter(ImageFilter.GaussianBlur(blur))
layer = Image.new("RGB",(w,h),(255,255,255))
layer.paste(inkim,(int(tx-x0-inkim.size[0]/2), int(ty-y0)))
res = (np.asarray(clean).astype(float)*np.asarray(layer).astype(float)/255).astype(np.uint8)
res = Image.composite(Image.fromarray(res), reg, m)
im.paste(res,(x0,y0)); im.save(out)
