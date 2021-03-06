# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from zzz_driver_msgs/FrenetSerretState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FrenetSerretState(genpy.Message):
  _md5sum = "f03652b9c5f9bef88b4d78664fce1034"
  _type = "zzz_driver_msgs/FrenetSerretState"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This message describes a state in 3d Frenet-Serret Frame
# Currently we don't use 3D frenet state actually
# For more information, refer to https://en.wikipedia.org/wiki/Frenet-Serret_formulas

# 3D states
float32 s # Offset in tanget direction
float32 d # Offset in normal direction
float32 b # Offset in binormal direction
float32 psi_s
float32 psi_d
float32 psi_b
float32[36] pose_covariance

# First order derivatives
float32 vs
float32 vd
float32 vb
float32 omega_s
float32 omega_d
float32 omega_b
float32[36] twist_covariance

# Second order derivatives
float32 sa # prevent keyword conflict
float32 ad
float32 ab
float32 epsilon_s
float32 epsilon_d
float32 epsilon_b
float32[36] accel_covariance
"""
  __slots__ = ['s','d','b','psi_s','psi_d','psi_b','pose_covariance','vs','vd','vb','omega_s','omega_d','omega_b','twist_covariance','sa','ad','ab','epsilon_s','epsilon_d','epsilon_b','accel_covariance']
  _slot_types = ['float32','float32','float32','float32','float32','float32','float32[36]','float32','float32','float32','float32','float32','float32','float32[36]','float32','float32','float32','float32','float32','float32','float32[36]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       s,d,b,psi_s,psi_d,psi_b,pose_covariance,vs,vd,vb,omega_s,omega_d,omega_b,twist_covariance,sa,ad,ab,epsilon_s,epsilon_d,epsilon_b,accel_covariance

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FrenetSerretState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.s is None:
        self.s = 0.
      if self.d is None:
        self.d = 0.
      if self.b is None:
        self.b = 0.
      if self.psi_s is None:
        self.psi_s = 0.
      if self.psi_d is None:
        self.psi_d = 0.
      if self.psi_b is None:
        self.psi_b = 0.
      if self.pose_covariance is None:
        self.pose_covariance = [0.] * 36
      if self.vs is None:
        self.vs = 0.
      if self.vd is None:
        self.vd = 0.
      if self.vb is None:
        self.vb = 0.
      if self.omega_s is None:
        self.omega_s = 0.
      if self.omega_d is None:
        self.omega_d = 0.
      if self.omega_b is None:
        self.omega_b = 0.
      if self.twist_covariance is None:
        self.twist_covariance = [0.] * 36
      if self.sa is None:
        self.sa = 0.
      if self.ad is None:
        self.ad = 0.
      if self.ab is None:
        self.ab = 0.
      if self.epsilon_s is None:
        self.epsilon_s = 0.
      if self.epsilon_d is None:
        self.epsilon_d = 0.
      if self.epsilon_b is None:
        self.epsilon_b = 0.
      if self.accel_covariance is None:
        self.accel_covariance = [0.] * 36
    else:
      self.s = 0.
      self.d = 0.
      self.b = 0.
      self.psi_s = 0.
      self.psi_d = 0.
      self.psi_b = 0.
      self.pose_covariance = [0.] * 36
      self.vs = 0.
      self.vd = 0.
      self.vb = 0.
      self.omega_s = 0.
      self.omega_d = 0.
      self.omega_b = 0.
      self.twist_covariance = [0.] * 36
      self.sa = 0.
      self.ad = 0.
      self.ab = 0.
      self.epsilon_s = 0.
      self.epsilon_d = 0.
      self.epsilon_b = 0.
      self.accel_covariance = [0.] * 36

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.s, _x.d, _x.b, _x.psi_s, _x.psi_d, _x.psi_b))
      buff.write(_get_struct_36f().pack(*self.pose_covariance))
      _x = self
      buff.write(_get_struct_6f().pack(_x.vs, _x.vd, _x.vb, _x.omega_s, _x.omega_d, _x.omega_b))
      buff.write(_get_struct_36f().pack(*self.twist_covariance))
      _x = self
      buff.write(_get_struct_6f().pack(_x.sa, _x.ad, _x.ab, _x.epsilon_s, _x.epsilon_d, _x.epsilon_b))
      buff.write(_get_struct_36f().pack(*self.accel_covariance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.s, _x.d, _x.b, _x.psi_s, _x.psi_d, _x.psi_b,) = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 144
      self.pose_covariance = _get_struct_36f().unpack(str[start:end])
      _x = self
      start = end
      end += 24
      (_x.vs, _x.vd, _x.vb, _x.omega_s, _x.omega_d, _x.omega_b,) = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 144
      self.twist_covariance = _get_struct_36f().unpack(str[start:end])
      _x = self
      start = end
      end += 24
      (_x.sa, _x.ad, _x.ab, _x.epsilon_s, _x.epsilon_d, _x.epsilon_b,) = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 144
      self.accel_covariance = _get_struct_36f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.s, _x.d, _x.b, _x.psi_s, _x.psi_d, _x.psi_b))
      buff.write(self.pose_covariance.tostring())
      _x = self
      buff.write(_get_struct_6f().pack(_x.vs, _x.vd, _x.vb, _x.omega_s, _x.omega_d, _x.omega_b))
      buff.write(self.twist_covariance.tostring())
      _x = self
      buff.write(_get_struct_6f().pack(_x.sa, _x.ad, _x.ab, _x.epsilon_s, _x.epsilon_d, _x.epsilon_b))
      buff.write(self.accel_covariance.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.s, _x.d, _x.b, _x.psi_s, _x.psi_d, _x.psi_b,) = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 144
      self.pose_covariance = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=36)
      _x = self
      start = end
      end += 24
      (_x.vs, _x.vd, _x.vb, _x.omega_s, _x.omega_d, _x.omega_b,) = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 144
      self.twist_covariance = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=36)
      _x = self
      start = end
      end += 24
      (_x.sa, _x.ad, _x.ab, _x.epsilon_s, _x.epsilon_d, _x.epsilon_b,) = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 144
      self.accel_covariance = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=36)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_36f = None
def _get_struct_36f():
    global _struct_36f
    if _struct_36f is None:
        _struct_36f = struct.Struct("<36f")
    return _struct_36f
_struct_6f = None
def _get_struct_6f():
    global _struct_6f
    if _struct_6f is None:
        _struct_6f = struct.Struct("<6f")
    return _struct_6f
