# Copyright (c) 2006- Facebook
# Distributed under the Thrift Software License
#
# See accompanying file LICENSE or visit the Thrift site at:
# http://developers.facebook.com/thrift/

class TType:
  STOP   = 0
  VOID   = 1
  BOOL   = 2
  BYTE   = 3
  I08    = 3
  DOUBLE = 4
  I16    = 6
  I32    = 8
  I64    = 10
  STRING = 11
  UTF7   = 11
  STRUCT = 12
  MAP    = 13
  SET    = 14
  LIST   = 15
  UTF8   = 16
  UTF16  = 17

class TMessageType:
  CALL  = 1
  REPLY = 2
  EXCEPTION = 3

class TProcessor:

  """Base class for procsessor, which works on two streams."""

  def process(iprot, oprot):
    pass

class TException(Exception):

  """Base class for all thrift exceptions."""

  def __init__(self, message=None):
    Exception.__init__(self, message)
    self.message = message

class TApplicationException(TException):

  """Application level thrift exceptions."""

  UNKNOWN = 0
  UNKNOWN_METHOD = 1
  INVALID_MESSAGE_TYPE = 2
  WRONG_METHOD_NAME = 3
  BAD_SEQUENCE_ID = 4
  MISSING_RESULT = 5

  def __init__(self, type=UNKNOWN, message=None):
    TException.__init__(self, message)
    self.type = type

  def __str__(self):
    if self.message:
      return self.message
    elif self.type == UNKNOWN_METHOD:
      return 'Unknown method'
    elif self.type == INVALID_MESSAGE_TYPE:
      return 'Invalid message type'
    elif self.type == WRONG_METHOD_NAME:
      return 'Wrong method name'
    elif self.type == BAD_SEQUENCE_ID:
      return 'Bad sequence ID'
    elif self.type == MISSING_RESULT:
      return 'Missing result'
    else:
      return 'Default (unknown) TApplicationException'

  def read(self, iprot):
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    oprot.writeStructBegin('TApplicationException')
    if self.message != None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.type != None:
      oprot.writeFieldBegin('type', TType.I32, 2)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
