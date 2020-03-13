// Auto-generated. Do not edit!

// (in-package smach_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class SmachContainerInitialStatusCmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.path = null;
      this.initial_states = null;
      this.local_data = null;
    }
    else {
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
      if (initObj.hasOwnProperty('local_data')) {
        this.local_data = initObj.local_data
      }
      else {
        this.local_data = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SmachContainerInitialStatusCmd
    // Serialize message field [path]
    bufferOffset = _serializer.string(obj.path, buffer, bufferOffset);
    // Serialize message field [initial_states]
    bufferOffset = _arraySerializer.string(obj.initial_states, buffer, bufferOffset, null);
    // Serialize message field [local_data]
    bufferOffset = _serializer.string(obj.local_data, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SmachContainerInitialStatusCmd
    let len;
    let data = new SmachContainerInitialStatusCmd(null);
    // Deserialize message field [path]
    data.path = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [initial_states]
    data.initial_states = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [local_data]
    data.local_data = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.path.length;
    object.initial_states.forEach((val) => {
      length += 4 + val.length;
    });
    length += object.local_data.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'smach_msgs/SmachContainerInitialStatusCmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '45f8cf31fc29b829db77f23001f788d6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # The path to the node in the server
    string path
    
    # The desired initial state(s)
    string[] initial_states
    
    # Initial values for the local user data of the state machine
    # A pickled user data structure
    # i.e. the UserData's internal dictionary
    string local_data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SmachContainerInitialStatusCmd(null);
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

    if (msg.local_data !== undefined) {
      resolved.local_data = msg.local_data;
    }
    else {
      resolved.local_data = ''
    }

    return resolved;
    }
};

module.exports = SmachContainerInitialStatusCmd;
