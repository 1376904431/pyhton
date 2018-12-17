from PIL.ImageGrab import grab
from math import pi,asin
from pykeyboard import PyKeyboard
from time import sleep
pkb=PyKeyboard()
#non0= lambda x:1/1e99 if x==0 else x
keyx= lambda x:6 if x>0 else 4 if x<0 else 7
keyy= lambda x:5 if x>0 else 8 if x<0 else 7

xs=1920
ys=1080
x0=xs/2
y0=ys/2
while 1==1:
    im=grab((0,0,xs,ys))
    pix=list(im.getdata())
    try:
        n=pix.index((255,0,19))
    except:
        x=xs/2
        y=ys/2
    else:
        x=n%xs#+偏移量
        y=n//xs#+偏移量


    ax=xs-x
    ay=xs-(y+420)
    b=xs/((2)**0.5)
    cx=(ax**2+b**2-((2)**0.5)*ax*b)**0.5
    xt=45-360*(asin(ax*(2)**0.5/(2*cx))/(2*pi))
    cy=(ay**2+b**2-((2)**0.5)*ay*b)**0.5
    yt=45-360*(asin(ay*(2)**0.5/(2*cy))/(2*pi))#x一圈3636像素 y一圈3600像素    
    nx=round(xt*3636/360)#此处得xt与yt函数可以简化
    ny=round(yt*3600/360)#round后误差仅在1像素即0.1度左右，是可以接受的误差
    pkb.tap_key(pkb.numpad_keys[keyx(nx)],n=abs(nx))
    pkb.tap_key(pkb.numpad_keys[keyy(ny)],n=abs(ny))
