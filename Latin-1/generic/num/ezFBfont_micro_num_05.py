'''
    ezFBfont_micro_num_05 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original micro.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: micro
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/micro.bdf', '_', './num-char.set']
# Date: 2024-07-31 14:57:23
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = 'micro'
family = 'generic'
weight = 'none'
size = None

def height():
    return 5

def baseline():
    return 5

def max_width():
    return 4

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
  32:b'\x00\x00\x00\x00\x00',
  37:b'\xa0`\xc0\xa0\x00',
  40:b' @@@ ',
  41:b'\x80@@@\x80',
  42:b'\xa0@\xe0@\xa0',
  43:b'\x00@\xe0@\x00',
  44:b'\x00\x00\x00@\xc0',
  45:b'\x00\x00\xe0\x00\x00',
  46:b'\x00\x00\x00\xc0\xc0',
  47:b'  @@\x80',
  48:b'@\xa0\xa0\xa0@',
  49:b'@\xc0@@@',
  50:b'\xc0 @\x80\xe0',
  51:b'\xc0 ` \xe0',
  52:b'\xa0\xa0\xa0\xe0 ',
  53:b'\xe0\x80\xc0 \xc0',
  54:b'`\x80\xe0\xa0\xe0',
  55:b'\xe0  @@',
  56:b'\xe0\xa0\xe0\xa0\xe0',
  57:b'\xe0\xa0\xe0 \xc0',
  58:b'\xc0\xc0\x00\xc0\xc0',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 5, 4
