#!/paty/to/python
# -*- coding: utf-8 -*-
import smbus
import time

i2c = smbus.SMBus(1)

# 画面初期化 (カーソル表示。点滅あり)
i2c.write_byte_data(0x50, 0x00, 0x01)
time.sleep(0.2)
i2c.write_byte_data(0x50, 0x00, 0x38)
time.sleep(0.1)
i2c.write_byte_data(0x50, 0x00, 0x0f)
time.sleep(0.1)
i2c.write_byte_data(0x50, 0x00, 0x06)
time.sleep(0.1)

# `XYZ` 出力
i2c.write_byte_data(0x50, 0x80, 0x58)
i2c.write_byte_data(0x50, 0x80, 0x59)
i2c.write_byte_data(0x50, 0x80, 0x5a)

# アドレス `40h` にカーソル移動 (DDRAM Address という一般的な 7 ビットの形式で指定)
i2c.write_byte_data(0x50, 0x00, 0xc0)
time.sleep(0.1)

# `xyz` 出力
i2c.write_byte_data(0x50, 0x80, 0x78)
i2c.write_byte_data(0x50, 0x80, 0x79)
i2c.write_byte_data(0x50, 0x80, 0x7a)

