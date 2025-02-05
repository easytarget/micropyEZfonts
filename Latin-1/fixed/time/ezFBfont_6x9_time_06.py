'''
    ezFBfont_6x9_time_06 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x9.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 6x9
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/6x9.bdf', '_', './time-char.set']
# Date: 2024-07-31 14:56:46
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-r-normal--9-90-75-75-c-60-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 9

def height():
    return 6

def baseline():
    return 6

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 58

_g = {
  32:b'\x00\x00\x00\x00\x00\x00',
  43:b'\x00  \xf8  ',
  45:b'\x00\x00\x00\xf8\x00\x00',
  46:b'\x00\x00\x00\x0000',
  48:b'0HHHH0',
  49:b' `   p',
  50:b'0H\x08\x10 x',
  51:b'x\x100\x08\x08p',
  52:b'\x100P\x90\xf8\x10',
  53:b'x@p\x08\x08p',
  54:b'0@pHH0',
  55:b'x\x08\x08\x10  ',
  56:b'0H0HH0',
  57:b'0HH8\x080',
  58:b'\x0000\x0000',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 6, 6
