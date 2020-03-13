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

class SmachContainerStructure {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.path = null;
      this.children = null;
      this.internal_outcomes = null;
      this.outcomes_from = null;
      this.outcomes_to = null;
      this.container_outcomes = null;
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
      if (initObj.hasOwnProperty('children')) {
        this.children = initObj.children
      }
      else {
        this.children = [];
      }
      if (initObj.hasOwnProperty('internal_outcomes')) {
        this.internal_outcomes = initObj.internal_outcomes
      }
      else {
        this.internal_outcomes = [];
      }
      if (initObj.hasOwnProperty('outcomes_from')) {
        this.outcomes_from = initObj.outcomes_from
      }
      else {
        this.outcomes_from = [];
      }
      if (initObj.hasOwnProperty('outcomes_to')) {
        this.outcomes_to = initObj.outcomes_to
      }
      else {
        this.outcomes_to = [];
      }
      if (initObj.hasOwnProperty('container_outcomes')) {
        this.container_outcomes = initObj.container_outcomes
      }
      else {
        this.container_outcomes = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SmachContainerStructure
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [path]
    bufferOffset = _serializer.string(obj.path, buffer, bufferOffset);
    // Serialize message field [children]
    bufferOffset = _arraySerializer.string(obj.children, buffer, bufferOffset, null);
    // Serialize message field [internal_outcomes]
    bufferOffset = _arraySerializer.string(obj.internal_outcomes, buffer, bufferOffset, null);
    // Serialize message field [outcomes_from]
    bufferOffset = _arraySerializer.string(obj.outcomes_from, buffer, bufferOffset, null);
    // Serialize message field [outcomes_to]
    bufferOffset = _arraySerializer.string(obj.outcomes_to, buffer, bufferOffset, null);
    // Serialize message field [container_outcomes]
    bufferOffset = _arraySerializer.string(obj.container_outcomes, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SmachContainerStructure
    let len;
    let data = new SmachContainerStructure(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [path]
    data.path = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [children]
    data.children = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [internal_outcomes]
    data.internal_outcomes = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [outcomes_from]
    data.outcomes_from = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [outcomes_to]
    data.outcomes_to = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [container_outcomes]
    data.container_outcomes = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += object.path.length;
    object.children.forEach((val) => {
      length += 4 + val.length;
    });
    object.internal_outcomes.forEach((val) => {
      length += 4 + val.length;
    });
    object.outcomes_from.forEach((val) => {
      length += 4 + val.length;
    });
    object.outcomes_to.forEach((val) => {
      length += 4 + val.length;
    });
    object.container_outcomes.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'smach_msgs/SmachContainerStructure';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3d3d1e0d0f99779ee9e58101a5dcf7ea';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
    # The path to this node in the server
    string path
    
    # The children of this node
    string[] children
    
    # The outcome edges
    # Each index across these arrays denote one edge
    string[] internal_outcomes
    string[] outcomes_from
    string[] outcomes_to
    
    # The potential outcomes from this container
    string[] container_outcomes
    
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
    const resolved = new SmachContainerStructure(null);
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

    if (msg.children !== undefined) {
      resolved.children = msg.children;
    }
    else {
      resolved.children = []
    }

    if (msg.internal_outcomes !== undefined) {
      resolved.internal_outcomes = msg.internal_outcomes;
    }
    else {
      resolved.internal_outcomes = []
    }

    if (msg.outcomes_from !== undefined) {
      resolved.outcomes_from = msg.outcomes_from;
    }
    else {
      resolved.outcomes_from = []
    }

    if (msg.outcomes_to !== undefined) {
      resolved.outcomes_to = msg.outcomes_to;
    }
    else {
      resolved.outcomes_to = []
    }

    if (msg.container_outcomes !== undefined) {
      resolved.container_outcomes = msg.container_outcomes;
    }
    else {
      resolved.container_outcomes = []
    }

    return resolved;
    }
};

module.exports = SmachContainerStructure;
