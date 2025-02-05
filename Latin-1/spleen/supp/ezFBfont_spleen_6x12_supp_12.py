'''
    ezFBfont_spleen_6x12_supp_12 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original spleen_6x12.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: spleen_6x12
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/spleen-6x12.bdf', '_', './supp-char.set']
# Date: 2024-07-31 14:57:37
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT /*
    COPYRIGHT * Spleen 6x12 1.9.1
    COPYRIGHT * Copyright (c) 2018-2022, Frederic Cambus
    COPYRIGHT * https://www.cambus.net/
    COPYRIGHT *
    COPYRIGHT * Created:      2020-04-08
    COPYRIGHT * Last Updated: 2021-03-12
    COPYRIGHT *
    COPYRIGHT * Spleen is released under the BSD 2-Clause license.
    COPYRIGHT * See LICENSE file for details.
    COPYRIGHT *
    COPYRIGHT * SPDX-License-Identifier: BSD-2-Clause
    COPYRIGHT */

    COMMENT "Copyright (c) 2018-2022, Frederic Cambus"
'''
version = '0.33'
name = '-misc-spleen-medium-r-normal--12-120-72-72-c-60-iso10646-1'
family = 'spleen'
weight = 'medium'
size = 12

def height():
    return 12

def baseline():
    return 9

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return True

def min_ch():
    return 160

def max_ch():
    return 255

_g = {
  160:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  161:b'\x00 \x00      \x00\x00\x00',
  162:b'\x00\x00 x\xa0\xa0\xa0\xa0x \x00\x00',
  163:b'\x000H@@\xf0@\x80\xf8\x00\x00\x00',
  164:b'\x00\x00\x00H0HH0H\x00\x00\x00',
  165:b'\x00\x88P p p  \x00\x00\x00',
  166:b'    \x00\x00    \x00\x00',
  167:b'\x000H 0HHH0\x10H0',
  168:b'\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  169:b'\x00x\x84\x94\xa4\xa4\xb4\x84x\x00\x00\x00',
  170:b'\x000\x088H8\x00x\x00\x00\x00\x00',
  171:b'\x00\x00\x00$H\x90\x90H$\x00\x00\x00',
  172:b'\x00\x00\x00\x00\x00\xf8\x08\x08\x00\x00\x00\x00',
  173:b'\x00\x00\x00\x00\x00p\x00\x00\x00\x00\x00\x00',
  174:b'\x00x\x84\xb4\xac\xb4\xac\x84x\x00\x00\x00',
  175:b'\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
  176:b'\x000HH0\x00\x00\x00\x00\x00\x00\x00',
  177:b'\x00\x00  \xf8  \x00\xf8\x00\x00\x00',
  178:b'\x000H\x08\x10 x\x00\x00\x00\x00\x00',
  179:b'\x000H\x10\x08H0\x00\x00\x00\x00\x00',
  180:b'\x00\x10 @\x00\x00\x00\x00\x00\x00\x00\x00',
  181:b'\x00\x00\x00\x90\x90\x90\x90\x90\xe8\x80\x80\x00',
  182:b'\x00x\xa8\xa8h((((\x00\x00\x00',
  183:b'\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00',
  184:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00  @',
  185:b'\x00 `   p\x00\x00\x00\x00\x00',
  186:b'\x000HHH0\x00x\x00\x00\x00\x00',
  187:b'\x00\x00\x00\x90H$$H\x90\x00\x00\x00',
  188:b'@\xc0@DH\x10 `\xa8<\x08\x08',
  189:b'@\xc0@DH\x10 X\xa4\x08\x10<',
  190:b'`\x90 \x14\x98p `\xa8<\x08\x08',
  191:b'\x00 \x00  @\x80\x88p\x00\x00\x00',
  192:b'@ p\x88\x88\xf8\x88\x88\x88\x00\x00\x00',
  193:b'\x10 p\x88\x88\xf8\x88\x88\x88\x00\x00\x00',
  194:b' Pp\x88\x88\xf8\x88\x88\x88\x00\x00\x00',
  195:b'H\xb0p\x88\x88\xf8\x88\x88\x88\x00\x00\x00',
  196:b'P\x00p\x88\x88\xf8\x88\x88\x88\x00\x00\x00',
  197:b' Pp\x88\x88\xf8\x88\x88\x88\x00\x00\x00',
  198:b'\x00x\xa0\xa0\xa0\xf8\xa0\xa0\xb8\x00\x00\x00',
  199:b'\x00x\x80\x80\x80\x80\x80\x80x  @',
  200:b'@ x\x80\x80\xf0\x80\x80x\x00\x00\x00',
  201:b'\x10 x\x80\x80\xf0\x80\x80x\x00\x00\x00',
  202:b' Px\x80\x80\xf0\x80\x80x\x00\x00\x00',
  203:b'P\x00x\x80\x80\xf0\x80\x80x\x00\x00\x00',
  204:b'@ p     p\x00\x00\x00',
  205:b'\x10 p     p\x00\x00\x00',
  206:b' Pp     p\x00\x00\x00',
  207:b'P\x00p     p\x00\x00\x00',
  208:b'\x00pHH\xe8HHHp\x00\x00\x00',
  209:b'H\xb0\x88\xc8\xc8\xa8\xa8\x98\x98\x00\x00\x00',
  210:b'@ p\x88\x88\x88\x88\x88p\x00\x00\x00',
  211:b'\x10 p\x88\x88\x88\x88\x88p\x00\x00\x00',
  212:b' Pp\x88\x88\x88\x88\x88p\x00\x00\x00',
  213:b'H\xb0p\x88\x88\x88\x88\x88p\x00\x00\x00',
  214:b'P\x00p\x88\x88\x88\x88\x88p\x00\x00\x00',
  215:b'\x00\x00\x00H00H\x00\x00\x00\x00\x00',
  216:b'\x08p\x88\x98\xa8\xa8\xc8\x88p\x80\x00\x00',
  217:b'@ \x88\x88\x88\x88\x88\x88x\x00\x00\x00',
  218:b'\x10 \x88\x88\x88\x88\x88\x88x\x00\x00\x00',
  219:b' P\x88\x88\x88\x88\x88\x88x\x00\x00\x00',
  220:b'P\x00\x88\x88\x88\x88\x88\x88x\x00\x00\x00',
  221:b'\x10 \x88\x88\x88x\x08\x08\xf0\x00\x00\x00',
  222:b'\x00\x00\x80\xf0\x88\x88\x88\x88\xf0\x80\x00\x00',
  223:b'\x00`\x90\x90\xa0\x90\x88\xc8\xb0\x00\x00\x00',
  224:b' \x10\x00p\x08x\x88\x88x\x00\x00\x00',
  225:b'\x10 \x00p\x08x\x88\x88x\x00\x00\x00',
  226:b' P\x00p\x08x\x88\x88x\x00\x00\x00',
  227:b'H\xb0\x00p\x08x\x88\x88x\x00\x00\x00',
  228:b'\x00P\x00p\x08x\x88\x88x\x00\x00\x00',
  229:b' P p\x08x\x88\x88x\x00\x00\x00',
  230:b'\x00\x00\x00\xd8(h\xb8\xa0x\x00\x00\x00',
  231:b'\x00\x00\x00x\x80\x80\x80\x80x  @',
  232:b' \x10\x00x\x88\x88\xf8\x80x\x00\x00\x00',
  233:b'\x10 \x00x\x88\x88\xf8\x80x\x00\x00\x00',
  234:b' P\x00x\x88\x88\xf8\x80x\x00\x00\x00',
  235:b'\x00P\x00x\x88\x88\xf8\x80x\x00\x00\x00',
  236:b' \x10\x00`    0\x00\x00\x00',
  237:b'\x10 \x00`    0\x00\x00\x00',
  238:b' P\x00`    0\x00\x00\x00',
  239:b'\x00P\x00`    0\x00\x00\x00',
  240:b'\xa0@\xa0p\x88\x88\x88\x88p\x00\x00\x00',
  241:b'H\xb0\x00\xf0\x88\x88\x88\x88\x88\x00\x00\x00',
  242:b' \x10\x00p\x88\x88\x88\x88p\x00\x00\x00',
  243:b'\x10 \x00p\x88\x88\x88\x88p\x00\x00\x00',
  244:b' P\x00p\x88\x88\x88\x88p\x00\x00\x00',
  245:b'H\xb0\x00p\x88\x88\x88\x88p\x00\x00\x00',
  246:b'\x00P\x00p\x88\x88\x88\x88p\x00\x00\x00',
  247:b'\x00\x00\x00 \x00\xf8\x00 \x00\x00\x00\x00',
  248:b'\x00\x00\x08p\x98\xa8\xc8\x88p\x80\x00\x00',
  249:b' \x10\x00\x88\x88\x88\x88\x88x\x00\x00\x00',
  250:b'\x10 \x00\x88\x88\x88\x88\x88x\x00\x00\x00',
  251:b' P\x00\x88\x88\x88\x88\x88x\x00\x00\x00',
  252:b'\x00P\x00\x88\x88\x88\x88\x88x\x00\x00\x00',
  253:b'\x10 \x00\x88\x88\x88\x88\x88x\x08\x08\xf0',
  254:b'\x00\x80\x80\xf0\x88\x88\x88\x88\xf0\x80\x80\x00',
  255:b'\x00P\x00\x88\x88\x88\x88\x88x\x08\x08\xf0',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 12, 6
