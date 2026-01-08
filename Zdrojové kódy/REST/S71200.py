import snap7
from snap7.util import *

class output(object):
    bool = 1
    int = 2

class S71200:
    def __init__(self, ip, debug=False):
        self.debug = debug
        self.plc = snap7.client.Client()
        self.plc.connect(ip, 0, 1)
        self.ip = ip

    def getMem(self, mem, returnByte=False):
        area = 0x83
        length = 1
        out = None
        bit = 0
        start = 0

        if mem[0].lower() == "m":
            area = 0x83        
        elif mem[0].lower() == "i":
            area = 0x81
        
        if mem[1].lower() == "x":  # bit
            length = 1
            out = output().bool
            start = int(mem.split(".")[0][2:])
            bit = int(mem.split(".")[1])        
        elif mem[1].lower() == "b":  # byte
            length = 1
            out = output().int
            start = int(mem[2:])           

        if self.debug:
            print(mem[0].lower(), bit)

        if area == 0x81:
            self.plc.read_area(snap7.types.Areas.PE, 0, start, length)
            mbyte = self.plc.read_area(snap7.types.Areas.PE, 0, start, length)        
        elif area == 0x83:
            self.plc.read_area(snap7.types.Areas.MK, 0, start, length)
            mbyte = self.plc.read_area(snap7.types.Areas.MK, 0, start, length)
        
        if returnByte:
            return mbyte        
        elif output().bool == out:
            return get_bool(mbyte, 0, bit)        
        elif output().int == out:
            return get_int(mbyte, start)

    def writeMem(self, mem, value):
        data = self.getMem(mem, True)

        area = 0x83
        bit = 0
        start = 0

        if mem[0].lower() == "m":
            area = 0x83        
        elif mem[0].lower() == "i":
            area = 0x81
        
        if mem[1].lower() == "x":  # bit
            start = int(mem.split(".")[0][2:])
            bit = int(mem.split(".")[1])
            set_bool(data, 0, bit, int(value))        
        elif mem[1].lower() == "b":  # byte
            start = int(mem[2:])
            start = start - 1
            set_int(data, 0, value)

        if area == 0x81:
            return self.plc.write_area(snap7.types.Areas.PE, 0, start, data)        
        elif area == 0x83:
            return self.plc.write_area(snap7.types.Areas.MK, 0, start, data)