'''
    ezFBfont_helvR08_num_10 : generated as part of the microPyEZfonts repository
      https://github.com/easytarget/microPyEZfonts

    This font definition can be used with the "ezFBfont" class provided there.
    It can also be used with the "writer" class from Peter Hinches micropython
      font-to-py tool: https://github.com/peterhinch/micropython-font-to-py

    Original helvR08.bdf font file was sourced from the U8G2 project:
      https://github.com/olikraus/u8g2

'''
# Code generated by bdf2dict.py
# Font: helvR08
# Cmd: ['bdf2dict.py'], ['Latin-1-bdf-sources/helvR08.bdf', '_', './num-char.set']
# Date: 2024-07-31 14:57:18
'''
    Original Copyright, Comments and Notices from source:

    COPYRIGHT ISO10646-1 extension by Markus Kuhn <mkuhn@acm.org>, 2001-03-20
    COPYRIGHT 
    COPYRIGHT +
    COPYRIGHT Copyright 1984-1989, 1994 Adobe Systems Incorporated.
    COPYRIGHT Copyright 1988, 1994 Digital Equipment Corporation.
    COPYRIGHT 
    COPYRIGHT Adobe is a trademark of Adobe Systems Incorporated which may be
    COPYRIGHT registered in certain jurisdictions.
    COPYRIGHT Permission to use these trademarks is hereby granted only in
    COPYRIGHT association with the images described in this file.
    COPYRIGHT 
    COPYRIGHT Permission to use, copy, modify, distribute and sell this software
    COPYRIGHT and its documentation for any purpose and without fee is hereby
    COPYRIGHT granted, provided that the above copyright notices appear in all
    COPYRIGHT copies and that both those copyright notices and this permission
    COPYRIGHT notice appear in supporting documentation, and that the names of
    COPYRIGHT Adobe Systems and Digital Equipment Corporation not be used in
    COPYRIGHT advertising or publicity pertaining to distribution of the software
    COPYRIGHT without specific, written prior permission.  Adobe Systems and
    COPYRIGHT Digital Equipment Corporation make no representations about the
    COPYRIGHT suitability of this software for any purpose.  It is provided "as
    COPYRIGHT is" without express or implied warranty.
    COPYRIGHT -

    COMMENT "Copyright (c) 1984, 1987 Adobe Systems Incorporated. All Rights Reserved. Copyright (c) 1988, 1991 Digital Equipment Corporation. All Rights Reserved."

    NOTICE "Helvetica is a trademark of Linotype-Hell AG and/or its subsidiaries.  "
'''
version = '0.33'
name = '-adobe-helvetica-medium-r-normal--11-80-100-100-p-56-iso10646-1'
family = 'helvetica'
weight = 'medium'
size = 11

def height():
    return 10

def baseline():
    return 8

def max_width():
    return 9

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 32

def max_ch():
    return 176

_g = {
  32:b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03',
  37:b'd\x00\x94\x00h\x00\x08\x00\x10\x00\x16\x00)\x00&\x00\x00\x00\x00\x00\t',
  40:b' @@\x80\x80\x80\x80@@ \x04',
  41:b'@  \x10\x10\x10\x10  @\x04',
  42:b'\xa0@\xa0\x00\x00\x00\x00\x00\x00\x00\x04',
  43:b'\x00\x00  \xf8  \x00\x00\x00\x06',
  44:b'\x00\x00\x00\x00\x00\x00\x00@@\x80\x03',
  45:b'\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x04',
  46:b'\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x03',
  47:b'  @@@@\x80\x80\x00\x00\x03',
  48:b'p\x88\x88\x88\x88\x88\x88p\x00\x00\x06',
  49:b' `      \x00\x00\x06',
  50:b'p\x88\x08\x080@\x80\xf8\x00\x00\x06',
  51:b'p\x88\x080\x08\x08\x88p\x00\x00\x06',
  52:b'\x100PP\x90\xf8\x10\x10\x00\x00\x06',
  53:b'x@@p\x08\x08\x88p\x00\x00\x06',
  54:b'p\x88\x80\xf0\x88\x88\x88p\x00\x00\x06',
  55:b'\xf8\x08\x10  @@@\x00\x00\x06',
  56:b'p\x88\x88p\x88\x88\x88p\x00\x00\x06',
  57:b'p\x88\x88\x88x\x08\x88p\x00\x00\x06',
  58:b'\x00\x00@\x00\x00\x00\x00@\x00\x00\x03',
  176:b'`\x90\x90`\x00\x00\x00\x00\x00\x00\x04',
}

def get_ch(ch):
    c = ord(ch)
    if c not in _g.keys():
        return None, 0, 0
    return memoryview(_g[c]), 10, int(_g[c][-1])
