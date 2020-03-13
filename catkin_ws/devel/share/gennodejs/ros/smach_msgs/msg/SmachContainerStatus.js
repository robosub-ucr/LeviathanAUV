// Auto-generated. Do not edit!

// (in-package smach_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class SmachContainerStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.path = null;
      this.initial_states = null;
      this.active_states = null;
      this.local_data = null;
      this.info = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('path')) {
        this.path = initObj.path
      }
      else {
        this.path = '';
      }
      if (initObj.hasOwnProperty('initial_states')) {
        this.initial_states = initObj.initial_states
      }
      else {
        this.initial_states = [];
      }
      if (initObj.hasOwnProperty('active_states')) {
        this.active_states = initObj.active_states
      }
      else {
        this.active_states = [];
      }
      if (initObj.hasOwnProperty('local_data')) {
        this.local_data = initObj.local_data
      }
      else {
        this.local_data = '';
      }
      if (initObj.hasOwnProperty('info')) {
        this.info = initObj.info
      }
      else {
        this.info = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SmachContainerStatus
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [path]
    bufferOffset = _serializer.string(obj.path, buffer, bufferOffset);
    // Serialize message field [initial_states]
    bufferOffset = _arraySerializer.string(obj.initial_states, buffer, bufferOffset, null);
    // Serialize message field [active_states]
    bufferOffset = _arraySerializer.string(obj.active_states, buffer, bufferOffset, null);
    // Serialize message field [local_data]
    bufferOffset = _serializer.string(obj.local_data, buffer, bufferOffset);
    // Serialize message field [info]
    bufferOffset = _serializer.string(obj.info, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SmachContainerStatus
    let len;
    let data = new SmachContainerStatus(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [path]
    data.path = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [initial_states]
    data.initial_states = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [active_states]
    data.active_states = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [local_data]
    data.local_data = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [info]
    data.info = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += object.path.length;
    object.initial_states.forEach((val) => {
      length += 4 + val.length;
    });
    object.active_states.forEach((val) => {
      length += 4 + val.length;
    });
    length += object.local_data.length;
    length += object.info.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'smach_msgs/SmachContainerStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5ba2bb79ac19e3842d562a191f2a675b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
    # The path to this node in the server
    string path
    
    # The initial state description
    # Effects an arc from the top state to each one
    string[] initial_states
    
    # The current state description
    string[] active_states
    
    # A pickled user data structure
    # i.e. the UserData's internal dictionary
    string local_data
    
    # Debugging info string
    string info
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SmachContainerStatus(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.path !== undefined) {
      resolved.path = msg.path;
    }
    else {
      resolved.path = ''
    }

    if (msg.initial_states !== undefined) {
      resolved.initial_states = msg.initial_states;
    }
    else {
      resolved.initial_states = []
    }

    if (msg.active_states !== undefined) {
      resolved.active_states = msg.active_states;
    }
    else {
      resolved.active_states = []
    }

    if (msg.local_data !== undefined) {
      resolved.local_data = msg.local_data;
    }
    else {
      resolved.local_data = ''
    }

    if (msg.info !== undefined) {
      resolved.info = msg.info;
    }
    else {
      resolved.info = ''
    }

    return resolved;
    }
};

module.exports = SmachContainerStatus;
