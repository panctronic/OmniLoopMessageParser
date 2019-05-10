# file: messagePatternParsing
import numpy as np
from byteUtils import *
from utils import *

import parse_02
import parse_06
import parse_0e
import parse_1a13
import parse_1a16
import parse_1a17
import parse_1d
import parse_1f

# note - parsers not finished return a hex string for 'message_type', e.g., '0x01'
#        whereas parsers that have been finished use '1a16' or '1d'
def ignoreMsg(msg):
    msgDict = {}
    byteMsg = bytearray.fromhex(msg)
    msgDict['mtype'] = byteMsg[0]
    msgDict['message_type'] = hex(byteMsg[0])
    msgDict['raw_value']    = msg
    return msgDict

def parse_1a(msg):
    # extract information the indicator for type of 1a command
    byteMsg = bytearray.fromhex(msg)
    byteList = list(byteMsg)
    xtype = byteList[16]
    if xtype == 0x16:
        msgDict = parse_1a16.parse_1a16(msg)
    elif xtype == 0x17:
        msgDict = parse_1a17.parse_1a17(msg)
    else:
        msgDict = parse_1a13.parse_1a13(msg)

    return msgDict

chooseMsgType = {
    0x02: parse_02.parse_02,
    0x06: parse_06.parse_06,
    0x0e: parse_0e.parse_0e,
    0x1a: parse_1a,
    0x1d: parse_1d.parse_1d,
    0x1f: parse_1f.parse_1f,
}

def processMsg(msg):
    byteMsg = bytearray.fromhex(msg)
    return chooseMsgType.get(byteMsg[0],ignoreMsg)(msg)
