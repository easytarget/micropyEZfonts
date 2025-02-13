'''
    ezFBfont_6x12_full_12 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original 6x12.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: 6x12
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/6x12.bdf', '_', './full-char.set']
# Date: 2024-07-31 14:56:42
'''
    Original Copyright, Comments and Notices from source:

    COMMENT "Public domain terminal emulator font.  Share and enjoy."
'''
version = '0.33'
name = '-misc-fixed-medium-r-semicondensed--12-110-75-75-c-60-iso10646-1'
family = 'fixed'
weight = 'medium'
size = 12

def height():
    return 12

def baseline():
    return 10

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 0

def max_ch():
    return 255

_g = {
  0:b'\x00\x00\x00\xa8\x00\x88\x00\x88\x00\xa8\x00\x00',
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  33:b'\x00\x00\x00     \x00 \x00\x00',
  34:b'\x00\x00PPP\x00\x00\x00\x00\x00\x00\x00',
  35:b'\x00\x00\x00\x00P\xf8PP\xf8P\x00\x00',
  36:b'\x00\x00 p\xa8\xa0p(\xa8p \x00',
  37:b'\x00\x00\x00\xc8\xc8\x10 @\x98\x98\x00\x00',
  38:b'\x00\x00\x00@\xa0\xa0@\xa8\x90h\x00\x00',
  39:b'\x00\x00   \x00\x00\x00\x00\x00\x00\x00',
  40:b'\x00\x00\x10  @@@  \x10\x00',
  41:b'\x00\x00@  \x10\x10\x10  @\x00',
  42:b'\x00\x00\x00 \xa8p p\xa8 \x00\x00',
  43:b'\x00\x00\x00\x00  \xf8  \x00\x00\x00',
  44:b'\x00\x00\x00\x00\x00\x00\x00\x00``\xc0\x00',
  45:b'\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00',
  46:b'\x00\x00\x00\x00\x00\x00\x00\x00``\x00\x00',
  47:b'\x00\x00\x00\x08\x10\x10 @@\x80\x00\x00',
  48:b'\x00\x00\x000HHHHH0\x00\x00',
  49:b'\x00\x00\x00 `    p\x00\x00',
  50:b'\x00\x00\x00p\x88\x08\x10 @\xf8\x00\x00',
  51:b'\x00\x00\x00\xf8\x08\x100\x08\x88p\x00\x00',
  52:b'\x00\x00\x00\x100P\x90\xf8\x10\x10\x00\x00',
  53:b'\x00\x00\x00\xf8\x80\xf0\x08\x08\x88p\x00\x00',
  54:b'\x00\x00\x000@\x80\xf0\x88\x88p\x00\x00',
  55:b'\x00\x00\x00\xf8\x08\x10\x10   \x00\x00',
  56:b'\x00\x00\x00p\x88\x88p\x88\x88p\x00\x00',
  57:b'\x00\x00\x00p\x88\x88x\x08\x10`\x00\x00',
  58:b'\x00\x00\x00\x00\x00``\x00``\x00\x00',
  59:b'\x00\x00\x00\x00\x00``\x00``\xc0\x00',
  60:b'\x00\x00\x00\x00\x10 @ \x10\x00\x00\x00',
  61:b'\x00\x00\x00\x00\x00\xf8\x00\xf8\x00\x00\x00\x00',
  62:b'\x00\x00\x00\x00@ \x10 @\x00\x00\x00',
  63:b'\x00\x00\x00p\x88\x10  \x00 \x00\x00',
  64:b'\x00\x00\x00p\x88\xb8\xa8\xb8\x80p\x00\x00',
  65:b'\x00\x00\x00p\x88\x88\xf8\x88\x88\x88\x00\x00',
  66:b'\x00\x00\x00\xf0HHpHH\xf0\x00\x00',
  67:b'\x00\x00\x00p\x88\x80\x80\x80\x88p\x00\x00',
  68:b'\x00\x00\x00\xf0HHHHH\xf0\x00\x00',
  69:b'\x00\x00\x00\xf8\x80\x80\xf0\x80\x80\xf8\x00\x00',
  70:b'\x00\x00\x00\xf8\x80\x80\xf0\x80\x80\x80\x00\x00',
  71:b'\x00\x00\x00p\x88\x80\x80\x98\x88p\x00\x00',
  72:b'\x00\x00\x00\x88\x88\x88\xf8\x88\x88\x88\x00\x00',
  73:b'\x00\x00\x00p     p\x00\x00',
  74:b'\x00\x00\x008\x10\x10\x10\x10\x90`\x00\x00',
  75:b'\x00\x00\x00\x88\x90\xa0\xc0\xa0\x90\x88\x00\x00',
  76:b'\x00\x00\x00\x80\x80\x80\x80\x80\x80\xf8\x00\x00',
  77:b'\x00\x00\x00\x88\xd8\xa8\x88\x88\x88\x88\x00\x00',
  78:b'\x00\x00\x00\x88\x88\xc8\xa8\x98\x88\x88\x00\x00',
  79:b'\x00\x00\x00p\x88\x88\x88\x88\x88p\x00\x00',
  80:b'\x00\x00\x00\xf0\x88\x88\xf0\x80\x80\x80\x00\x00',
  81:b'\x00\x00\x00p\x88\x88\x88\xa8\x90h\x00\x00',
  82:b'\x00\x00\x00\xf0\x88\x88\xf0\xa0\x90\x88\x00\x00',
  83:b'\x00\x00\x00p\x88\x80p\x08\x88p\x00\x00',
  84:b'\x00\x00\x00\xf8      \x00\x00',
  85:b'\x00\x00\x00\x88\x88\x88\x88\x88\x88p\x00\x00',
  86:b'\x00\x00\x00\x88\x88\x88\x88PP \x00\x00',
  87:b'\x00\x00\x00\x88\x88\x88\x88\xa8\xa8P\x00\x00',
  88:b'\x00\x00\x00\x88\x88P P\x88\x88\x00\x00',
  89:b'\x00\x00\x00\x88\x88P    \x00\x00',
  90:b'\x00\x00\x00\xf8\x08\x10 @\x80\xf8\x00\x00',
  91:b'\x00\x00p@@@@@@@p\x00',
  92:b'\x00\x00\x00\x80@@ \x10\x10\x08\x00\x00',
  93:b'\x00\x00p\x10\x10\x10\x10\x10\x10\x10p\x00',
  94:b'\x00\x00 P\x88\x00\x00\x00\x00\x00\x00\x00',
  95:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8',
  96:b'\x00\x00@ \x10\x00\x00\x00\x00\x00\x00\x00',
  97:b'\x00\x00\x00\x00\x00p\x08x\x88x\x00\x00',
  98:b'\x00\x00\x00\x80\x80\xf0\x88\x88\x88\xf0\x00\x00',
  99:b'\x00\x00\x00\x00\x00p\x88\x80\x88p\x00\x00',
  100:b'\x00\x00\x00\x08\x08x\x88\x88\x88x\x00\x00',
  101:b'\x00\x00\x00\x00\x00p\x88\xf0\x80p\x00\x00',
  102:b'\x00\x00\x000H@\xe0@@@\x00\x00',
  103:b'\x00\x00\x00\x00\x00p\x88\x88\x88x\x08p',
  104:b'\x00\x00\x00\x80\x80\xf0\x88\x88\x88\x88\x00\x00',
  105:b'\x00\x00\x00 \x00`   p\x00\x00',
  106:b'\x00\x00\x00\x08\x00\x18\x08\x08\x08\x08H0',
  107:b'\x00\x00\x00\x80\x80\x88\x90\xe0\x90\x88\x00\x00',
  108:b'\x00\x00\x00`     p\x00\x00',
  109:b'\x00\x00\x00\x00\x00\xd0\xa8\xa8\xa8\xa8\x00\x00',
  110:b'\x00\x00\x00\x00\x00\xb0\xc8\x88\x88\x88\x00\x00',
  111:b'\x00\x00\x00\x00\x00p\x88\x88\x88p\x00\x00',
  112:b'\x00\x00\x00\x00\x00\xf0\x88\x88\x88\xf0\x80\x80',
  113:b'\x00\x00\x00\x00\x00x\x88\x88\x88x\x08\x08',
  114:b'\x00\x00\x00\x00\x00\xb0\xc8\x80\x80\x80\x00\x00',
  115:b'\x00\x00\x00\x00\x00x\x80p\x08\xf0\x00\x00',
  116:b'\x00\x00\x00  \xf8   \x18\x00\x00',
  117:b'\x00\x00\x00\x00\x00\x88\x88\x88\x98h\x00\x00',
  118:b'\x00\x00\x00\x00\x00\x88\x88\x88P \x00\x00',
  119:b'\x00\x00\x00\x00\x00\x88\x88\xa8\xa8P\x00\x00',
  120:b'\x00\x00\x00\x00\x00\x88P P\x88\x00\x00',
  121:b'\x00\x00\x00\x00\x00\x88\x88\x88P @\x80',
  122:b'\x00\x00\x00\x00\x00\xf8\x10 @\xf8\x00\x00',
  123:b'\x00\x00\x10   @   \x10\x00',
  124:b'\x00\x00         \x00',
  125:b'\x00\x00@   \x10   @\x00',
  126:b'\x00\x00\x00\x00\x00H\xa8\x90\x00\x00\x00\x00',
  160:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  161:b'\x00\x00\x00 \x00     \x00\x00',
  162:b'\x00\x00\x00\x00 p\xa8\xa0\xa8p \x00',
  163:b'\x00\x00\x000H@\xe0@H\xb0\x00\x00',
  164:b'\x00\x00\x00\x00\x00\xa8P\x88P\xa8\x00\x00',
  165:b'\x00\x00\x00\x88P\xf8 \xf8  \x00\x00',
  166:b'\x00\x00\x00   \x00   \x00\x00',
  167:b'\x00\x008@0HH0\x08p\x00\x00',
  168:b'\x00\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  169:b'\x00\x00\x00x\x84\x94\xa4\x94\x84x\x00\x00',
  170:b'\x000P0\x00p\x00\x00\x00\x00\x00\x00',
  171:b'\x00\x00\x00\x00\x00(P\xa0P(\x00\x00',
  172:b'\x00\x00\x00\x00\x00\x00\xf8\x08\x08\x00\x00\x00',
  173:b'\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x00\x00',
  174:b'\x00\x00\x00x\x84\xb4\xa4\xa4\x84x\x00\x00',
  175:b'\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  176:b'\x000HH0\x00\x00\x00\x00\x00\x00\x00',
  177:b'\x00\x00\x00  \xf8  \x00\xf8\x00\x00',
  178:b' P\x10 p\x00\x00\x00\x00\x00\x00\x00',
  179:b'`\x10 \x10`\x00\x00\x00\x00\x00\x00\x00',
  180:b'\x00\x00\x10 @\x00\x00\x00\x00\x00\x00\x00',
  181:b'\x00\x00\x00\x00\x00\x88\x88\x88\x98\xe8\x80\x80',
  182:b'\x00\x00x\xe8\xe8\xe8h(((\x00\x00',
  183:b'\x00\x00\x00\x00\x0000\x00\x00\x00\x00\x00',
  184:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10`',
  185:b' `  p\x00\x00\x00\x00\x00\x00\x00',
  186:b' P \x00p\x00\x00\x00\x00\x00\x00\x00',
  187:b'\x00\x00\x00\x00\x00\xa0P(P\xa0\x00\x00',
  188:b'@\xc0@@P0Px\x10\x10\x00\x00',
  189:b'@\xc0@@P(\x08\x10 8\x00\x00',
  190:b'\xc0 @ \xd00Px\x10\x10\x00\x00',
  191:b'\x00\x00\x00 \x00  @\x88p\x00\x00',
  192:b'@ \x00p\x88\x88\xf8\x88\x88\x88\x00\x00',
  193:b'\x10 \x00p\x88\x88\xf8\x88\x88\x88\x00\x00',
  194:b' P\x00p\x88\x88\xf8\x88\x88\x88\x00\x00',
  195:b'h\xb0\x00p\x88\x88\xf8\x88\x88\x88\x00\x00',
  196:b'\x00P\x00p\x88\x88\xf8\x88\x88\x88\x00\x00',
  197:b' P p\x88\x88\xf8\x88\x88\x88\x00\x00',
  198:b'\x00\x00\x00x\xa0\xa0\xf0\xa0\xa0\xb8\x00\x00',
  199:b'\x00\x00\x00p\x88\x80\x80\x80\x88p\x10`',
  200:b'@ \x00\xf8\x80\x80\xf0\x80\x80\xf8\x00\x00',
  201:b'\x10 \x00\xf8\x80\x80\xf0\x80\x80\xf8\x00\x00',
  202:b' P\x00\xf8\x80\x80\xf0\x80\x80\xf8\x00\x00',
  203:b'\x00P\x00\xf8\x80\x80\xf0\x80\x80\xf8\x00\x00',
  204:b'@ \x00p     p\x00\x00',
  205:b'\x10 \x00p     p\x00\x00',
  206:b' P\x00p     p\x00\x00',
  207:b'\x00P\x00p     p\x00\x00',
  208:b'\x00\x00\x00pHH\xe8HHp\x00\x00',
  209:b'h\xb0\x00\x88\x88\xc8\xa8\x98\x88\x88\x00\x00',
  210:b'@ \x00p\x88\x88\x88\x88\x88p\x00\x00',
  211:b'\x10 \x00p\x88\x88\x88\x88\x88p\x00\x00',
  212:b' P\x00p\x88\x88\x88\x88\x88p\x00\x00',
  213:b'h\xb0\x00p\x88\x88\x88\x88\x88p\x00\x00',
  214:b'\x00P\x00p\x88\x88\x88\x88\x88p\x00\x00',
  215:b'\x00\x00\x00\x00\x88P P\x88\x00\x00\x00',
  216:b'\x00\x00\x08p\x98\xa8\xa8\xa8\xc8p\x80\x00',
  217:b'@ \x00\x88\x88\x88\x88\x88\x88p\x00\x00',
  218:b'\x10 \x00\x88\x88\x88\x88\x88\x88p\x00\x00',
  219:b' P\x00\x88\x88\x88\x88\x88\x88p\x00\x00',
  220:b'\x00P\x00\x88\x88\x88\x88\x88\x88p\x00\x00',
  221:b'\x10 \x00\x88\x88P    \x00\x00',
  222:b'\x00\x00\x00@pHHHp@\x00\x00',
  223:b'\x00\x00\x00p\x88\x90\xa0\x90\x88\xb0\x00\x00',
  224:b'\x00\x00@ \x00p\x08x\x88x\x00\x00',
  225:b'\x00\x00\x10 \x00p\x08x\x88x\x00\x00',
  226:b'\x00\x00 P\x00p\x08x\x88x\x00\x00',
  227:b'\x00\x00h\xb0\x00p\x08x\x88x\x00\x00',
  228:b'\x00\x00\x00P\x00p\x08x\x88x\x00\x00',
  229:b'\x00\x00 P p\x08x\x88x\x00\x00',
  230:b'\x00\x00\x00\x00\x00p(p\xa0x\x00\x00',
  231:b'\x00\x00\x00\x00\x00p\x88\x80\x88p\x10`',
  232:b'\x00\x00@ \x00p\x88\xf0\x80p\x00\x00',
  233:b'\x00\x00\x10 \x00p\x88\xf0\x80p\x00\x00',
  234:b'\x00\x00 P\x00p\x88\xf0\x80p\x00\x00',
  235:b'\x00\x00\x00P\x00p\x88\xf0\x80p\x00\x00',
  236:b'\x00\x00@ \x00`   p\x00\x00',
  237:b'\x00\x00\x10 \x00`   p\x00\x00',
  238:b'\x00\x00 P\x00`   p\x00\x00',
  239:b'\x00\x00\x00P\x00`   p\x00\x00',
  240:b'\x00P P\x08x\x88\x88\x88p\x00\x00',
  241:b'\x00\x00h\xb0\x00\xb0\xc8\x88\x88\x88\x00\x00',
  242:b'\x00\x00@ \x00p\x88\x88\x88p\x00\x00',
  243:b'\x00\x00\x10 \x00p\x88\x88\x88p\x00\x00',
  244:b'\x00\x00 P\x00p\x88\x88\x88p\x00\x00',
  245:b'\x00\x00h\xb0\x00p\x88\x88\x88p\x00\x00',
  246:b'\x00\x00\x00P\x00p\x88\x88\x88p\x00\x00',
  247:b'\x00\x00\x00\x00 \x00\xf8\x00 \x00\x00\x00',
  248:b'\x00\x00\x00\x00\x00x\x98\xa8\xc8\xf0\x00\x00',
  249:b'\x00\x00@ \x00\x88\x88\x88\x88p\x00\x00',
  250:b'\x00\x00\x10 \x00\x88\x88\x88\x88p\x00\x00',
  251:b'\x00\x00 P\x00\x88\x88\x88\x88p\x00\x00',
  252:b'\x00\x00\x00P\x00\x88\x88\x88\x88p\x00\x00',
  253:b'\x00\x00\x10 \x00\x88\x88\x88P @\x80',
  254:b'\x00\x00\x00\x80\x80\xf0\x88\x88\x88\xf0\x80\x80',
  255:b'\x00\x00\x00P\x00\x88\x88\x88P @\x80',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 12, 6
