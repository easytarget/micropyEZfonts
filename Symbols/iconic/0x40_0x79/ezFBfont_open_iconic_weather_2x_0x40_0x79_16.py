'''
    ezFBfont_open_iconic_weather_2x_0x40_0x79_16 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original open_iconic_weather_2x.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: open_iconic_weather_2x
# Cmd: ['bdf2dict.py'], ['Symbols-bdf-sources/open_iconic_weather_2x.bdf', '_', './0x40_0x79-char.set']
# Date: 2024-07-31 15:36:45
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "https://github.com/iconic/open-iconic, SIL OPEN FONT LICENSE"
'''
version = '0.33'
name = 'open_iconic_weather_2x'
family = 'iconic'
weight = 'none'
size = None

def height():
    return 16

def baseline():
    return 16

def max_width():
    return 16

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 64

def max_ch():
    return 69

_g = {
  64:b'\x00\x00\x00\x00\x01\xe0\x07\xf8\x07\xf8\x0f\xfc?\xfc\x7f\xfc\xff\xfe\xff\xff\xff\xff\xff\xff\x7f\xff?\xfe\x00\x00\x00\x00',
  65:b'\x1e\x00\x7f\x80|\x00\xf8\x00\xf1\xe0\xe7\xf8\xc7\xf8\x0f\xfc?\xfc\x7f\xfc\xff\xfe\xff\xff\xff\xff\xff\xff\x7f\xff?\xfe',
  66:b'\x08\x00\x18\x008\x00x\x00x\x00\xfc\x00\xfc\x00\xfe\x00\xff\x00\xff\x80\x7f\xf2\x7f\xfe?\xfc\x1f\xf8\x0f\xf0\x01\x80',
  67:b'\x01\xe0\x07\xf8\x07\xf8\x0f\xfc?\xfc\x7f\xfc\xff\xfe\xff\xff\xf8\x7f\xf0?\x03\x07\x03\x0230303030',
  68:b'\x00\x00\x00\x00\x01\x80\x01\x80\x01\x80\x03\xc0\x7f\xfe?\xfc\x1f\xf8\x0f\xf0\x07\xe0\x07\xe0\x0ep\x0c0\x08\x10\x00\x00',
  69:b'\x01\x80\x01\x800\x0c0\x0c\x03\xc0\x07\xe0\x0f\xf0\xcf\xf3\xcf\xf3\x0f\xf0\x07\xe0\x03\xc00\x0c0\x0c\x01\x80\x01\x80',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 16, 16
