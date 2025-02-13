'''
    ezFBfont_8x13B_ascii_12 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 8x13B.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 8x13B
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/8x13B.bdf', '_', './ascii-char.set']
# Date: 2024-07-31 14:56:54
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-bold-r-normal--13-120-75-75-c-80-iso10646-1'
family = 'fixed'
weight = 'bold'
size = 13

def height():
    return 12

def baseline():
    return 10

def max_width():
    return 8

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 32

def max_ch():
    return 126

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  33:b'\x18\x18\x18\x18\x18\x18\x18\x00\x18\x18\x00\x00',
  34:b'llll\x00\x00\x00\x00\x00\x00\x00\x00',
  35:b'\x00ll\xfe\xfel\xfe\xfell\x00\x00',
  36:b'\x10|\xd6\xd0\xf0|\x1e\x16\xd6|\x10\x00',
  37:b'\xe6\xa6\xec\x18\x1800n\xca\xce\x00\x00',
  38:b'\x00\x00\x00x\xcc\xccx\xce\xcc~\x00\x00',
  39:b'\x18\x18\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00',
  40:b'\x0c\x1800```00\x18\x0c\x00',
  41:b'`0\x18\x18\x0c\x0c\x0c\x18\x180`\x00',
  42:b'\x00\x00\x10\x10\xfe88lD\x00\x00\x00',
  43:b'\x00\x00\x18\x18~~\x18\x18\x00\x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00<\x1c\x1c\x180\x00',
  45:b'\x00\x00\x00\x00\x00~\x00\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x18<\x18\x00\x00',
  47:b'\x02\x06\x06\x0c\x180`\xc0\xc0\x80\x00\x00',
  48:b'8l\xc6\xc6\xc6\xc6\xc6\xc6l8\x00\x00',
  49:b'\x188x\x18\x18\x18\x18\x18\x18~\x00\x00',
  50:b'|\xc6\xc6\x06\x0c\x180`\xc0\xfe\x00\x00',
  51:b'\xfe\x06\x0c\x18<\x06\x06\x06\xc6|\x00\x00',
  52:b'\x0c\x1c<l\xcc\xcc\xfe\x0c\x0c\x0c\x00\x00',
  53:b'\xfe\xc0\xc0\xfc\xe6\x06\x06\x06\xc6|\x00\x00',
  54:b'<`\xc0\xc0\xfc\xe6\xc6\xc6\xe6|\x00\x00',
  55:b'\xfe\x06\x06\x0c\x18\x180000\x00\x00',
  56:b'|\xc6\xc6\xc6|\xc6\xc6\xc6\xc6|\x00\x00',
  57:b'|\xce\xc6\xc6\xce~\x06\x06\x0cx\x00\x00',
  58:b'\x00\x00\x18<\x18\x00\x00\x18<\x18\x00\x00',
  59:b'\x00\x00\x18<\x18\x00<\x1c\x1c\x180\x00',
  60:b'\x00\x06\x0c\x180`0\x18\x0c\x06\x00\x00',
  61:b'\x00\x00\x00\x00~\x00\x00~\x00\x00\x00\x00',
  62:b'\x00`0\x18\x0c\x06\x0c\x180`\x00\x00',
  63:b'|\xc6\xc6\x06\x0c\x18\x18\x00\x18\x18\x00\x00',
  64:b'\x00|\xfe\xce\xde\xd2\xd2\xde\xe0~\x00\x00',
  65:b'8|\xc6\xc6\xc6\xfe\xc6\xc6\xc6\xc6\x00\x00',
  66:b'\xfcfff|ffff\xfc\x00\x00',
  67:b'|\xe6\xc6\xc0\xc0\xc0\xc0\xc6\xe6|\x00\x00',
  68:b'\xfcffffffff\xfc\x00\x00',
  69:b'\xfe\xc0\xc0\xc0\xf8\xc0\xc0\xc0\xc0\xfe\x00\x00',
  70:b'\xfe\xc0\xc0\xc0\xf8\xc0\xc0\xc0\xc0\xc0\x00\x00',
  71:b'|\xc6\xc6\xc0\xc0\xc0\xce\xc6\xc6|\x00\x00',
  72:b'\xc6\xc6\xc6\xc6\xfe\xc6\xc6\xc6\xc6\xc6\x00\x00',
  73:b'<\x18\x18\x18\x18\x18\x18\x18\x18<\x00\x00',
  74:b'\x0e\x06\x06\x06\x06\x06\x06\xc6\xc6|\x00\x00',
  75:b'\xc6\xc6\xcc\xd8\xf0\xf0\xd8\xcc\xc6\xc6\x00\x00',
  76:b'\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc2\xfe\x00\x00',
  77:b'\xc6\xc6\xee\xfe\xd6\xc6\xc6\xc6\xc6\xc6\x00\x00',
  78:b'\xc6\xc6\xe6\xe6\xf6\xde\xce\xce\xc6\xc6\x00\x00',
  79:b'|\xc6\xc6\xc6\xc6\xc6\xc6\xc6\xc6|\x00\x00',
  80:b'\xfc\xc6\xc6\xc6\xc6\xfc\xc0\xc0\xc0\xc0\x00\x00',
  81:b'|\xc6\xc6\xc6\xc6\xc6\xc6\xc6\xde|\x06\x00',
  82:b'\xfc\xc6\xc6\xc6\xfc\xf8\xcc\xcc\xc6\xc6\x00\x00',
  83:b'|\xc6\xc6\xc0|\x06\x06\xc6\xc6|\x00\x00',
  84:b'~\x18\x18\x18\x18\x18\x18\x18\x18\x18\x00\x00',
  85:b'\xc6\xc6\xc6\xc6\xc6\xc6\xc6\xc6\xc6|\x00\x00',
  86:b'\xc6\xc6\xc6\xc6Dll88\x10\x00\x00',
  87:b'\xc6\xc6\xc6\xc6\xc6\xc6\xd6\xd6\xfel\x00\x00',
  88:b'\xc6\xc6ll88ll\xc6\xc6\x00\x00',
  89:b'fff<<\x18\x18\x18\x18\x18\x00\x00',
  90:b'\xfe\x06\x06\x0c\x180`\xc0\xc0\xfe\x00\x00',
  91:b'|`````````|\x00',
  92:b'\x80\xc0\xc0`0\x18\x0c\x06\x06\x02\x00\x00',
  93:b'|\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c|\x00',
  94:b'\x108l\xc6\x00\x00\x00\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x00',
  96:b'0\x18\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  97:b'\x00\x00\x00|\x06~\xc6\xc6\xcev\x00\x00',
  98:b'\xc0\xc0\xc0\xdc\xe6\xc6\xc6\xc6\xe6\xdc\x00\x00',
  99:b'\x00\x00\x00|\xe6\xc0\xc0\xc0\xe6|\x00\x00',
  100:b'\x06\x06\x06v\xce\xc6\xc6\xc6\xcev\x00\x00',
  101:b'\x00\x00\x00|\xc6\xc6\xfe\xc0\xc6|\x00\x00',
  102:b'<f```\xfc````\x00\x00',
  103:b'\x00\x00\x00~\xcc\xcc\xccx\xf0|\xc6|',
  104:b'\xc0\xc0\xc0\xdc\xe6\xc6\xc6\xc6\xc6\xc6\x00\x00',
  105:b'\x00\x18\x18\x008\x18\x18\x18\x18<\x00\x00',
  106:b'\x00\x06\x06\x00\x0e\x06\x06\x06\x06\xc6\xc6|',
  107:b'\xc0\xc0\xc0\xcc\xd8\xf0\xf0\xd8\xcc\xc6\x00\x00',
  108:b'8\x18\x18\x18\x18\x18\x18\x18\x18<\x00\x00',
  109:b'\x00\x00\x00l\xfe\xd6\xd6\xc6\xc6\xc6\x00\x00',
  110:b'\x00\x00\x00\xdc\xe6\xc6\xc6\xc6\xc6\xc6\x00\x00',
  111:b'\x00\x00\x00|\xc6\xc6\xc6\xc6\xc6|\x00\x00',
  112:b'\x00\x00\x00\xdc\xe6\xc6\xc6\xc6\xe6\xdc\xc0\xc0',
  113:b'\x00\x00\x00v\xce\xc6\xc6\xc6\xcev\x06\x06',
  114:b'\x00\x00\x00\xdc\xe6\xc0\xc0\xc0\xc0\xc0\x00\x00',
  115:b'\x00\x00\x00|\xc6`8\x0c\xc6|\x00\x00',
  116:b'````\xfc```f<\x00\x00',
  117:b'\x00\x00\x00\xc6\xc6\xc6\xc6\xc6\xcev\x00\x00',
  118:b'\x00\x00\x00\xc6\xc6\xc6\xc6ll8\x00\x00',
  119:b'\x00\x00\x00\xc6\xc6\xc6\xd6\xd6\xfel\x00\x00',
  120:b'\x00\x00\x00\xc6\xc6l8l\xc6\xc6\x00\x00',
  121:b'\x00\x00\x00\xc6\xc6\xc6\xc6\xcev\x06\xc6|',
  122:b'\x00\x00\x00\xfe\x0c\x180`\xc0\xfe\x00\x00',
  123:b'\x1e000\x18p\x18000\x1e\x00',
  124:b'\x18\x18\x18\x18\x18\x18\x18\x18\x18\x18\x00\x00',
  125:b'x\x0c\x0c\x0c\x18\x0e\x18\x0c\x0c\x0cx\x00',
  126:b'\x00r\xfe\x9c\x00\x00\x00\x00\x00\x00\x00\x00',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 12, 8
