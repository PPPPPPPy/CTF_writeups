#!/usr/bin/env python
# -*- for height_is_weird.png -*-
# -*- coding: utf-8 -*-
import binascii
import struct

#\x49\x48\x44\x52\x00\x00\x01\xF4\x00\x00\x01\xA4\x08\x06\x00\x00\x00
# === Chunck Type + Chunck Data === (4 bytes + 13 bytes)
#\x49\x48\x44\x52\x00\x00\x03\x5A\x00\x00\x01\x52\x08\x02\x00\x00\x00

crc32key = 0x7248220F
for i in range(0, 65535):
  height = struct.pack('>i', i)
  #CRC: CBD6DF8A
  data = '\x49\x48\x44\x52\x00\x00\x03\x5A' + height + '\x08\x02\x00\x00\x00'

  crc32result = binascii.crc32(data) & 0xffffffff
  # Brute force to get value and collision with CRC
  if crc32result == crc32key:
    print ''.join(map(lambda c: "%02X" % ord(c), height))