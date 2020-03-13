; Auto-generated. Do not edit!


(cl:in-package smach_msgs-msg)


;//! \htmlinclude SmachContainerInitialStatusCmd.msg.html

(cl:defclass <SmachContainerInitialStatusCmd> (roslisp-msg-protocol:ros-message)
  ((path
    :reader path
    :initarg :path
    :type cl:string
    :initform "")
   (initial_states
    :reader initial_states
    :initarg :initial_states
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (local_data
    :reader local_data
    :initarg :local_data
    :type cl:string
    :initform ""))
)

(cl:defclass SmachContainerInitialStatusCmd (<SmachContainerInitialStatusCmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SmachContainerInitialStatusCmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SmachContainerInitialStatusCmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name smach_msgs-msg:<SmachContainerInitialStatusCmd> is deprecated: use smach_msgs-msg:SmachContainerInitialStatusCmd instead.")))

(cl:ensure-generic-function 'path-val :lambda-list '(m))
(cl:defmethod path-val ((m <SmachContainerInitialStatusCmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smach_msgs-msg:path-val is deprecated.  Use smach_msgs-msg:path instead.")
  (path m))

(cl:ensure-generic-function 'initial_states-val :lambda-list '(m))
(cl:defmethod initial_states-val ((m <SmachContainerInitialStatusCmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smach_msgs-msg:initial_states-val is deprecated.  Use smach_msgs-msg:initial_states instead.")
  (initial_states m))

(cl:ensure-generic-function 'local_data-val :lambda-list '(m))
(cl:defmethod local_data-val ((m <SmachContainerInitialStatusCmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader smach_msgs-msg:local_data-val is deprecated.  Use smach_msgs-msg:local_data instead.")
  (local_data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SmachContainerInitialStatusCmd>) ostream)
  "Serializes a message object of type '<SmachContainerInitialStatusCmd>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'path))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'initial_states))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'initial_states))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'local_data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'local_data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SmachContainerInitialStatusCmd>) istream)
  "Deserializes a message object of type '<SmachContainerInitialStatusCmd>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'path) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'path) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'initial_states) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'initial_states)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'local_data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'local_data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SmachContainerInitialStatusCmd>)))
  "Returns string type for a message object of type '<SmachContainerInitialStatusCmd>"
  "smach_msgs/SmachContainerInitialStatusCmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SmachContainerInitialStatusCmd)))
  "Returns string type for a message object of type 'SmachContainerInitialStatusCmd"
  "smach_msgs/SmachContainerInitialStatusCmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SmachContainerInitialStatusCmd>)))
  "Returns md5sum for a message object of type '<SmachContainerInitialStatusCmd>"
  "45f8cf31fc29b829db77f23001f788d6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SmachContainerInitialStatusCmd)))
  "Returns md5sum for a message object of type 'SmachContainerInitialStatusCmd"
  "45f8cf31fc29b829db77f23001f788d6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SmachContainerInitialStatusCmd>)))
  "Returns full string definition for message of type '<SmachContainerInitialStatusCmd>"
  (cl:format cl:nil "# The path to the node in the server~%string path~%~%# The desired initial state(s)~%string[] initial_states~%~%# Initial values for the local user data of the state machine~%# A pickled user data structure~%# i.e. the UserData's internal dictionary~%string local_data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SmachContainerInitialStatusCmd)))
  "Returns full string definition for message of type 'SmachContainerInitialStatusCmd"
  (cl:format cl:nil "# The path to the node in the server~%string path~%~%# The desired initial state(s)~%string[] initial_states~%~%# Initial values for the local user data of the state machine~%# A pickled user data structure~%# i.e. the UserData's internal dictionary~%string local_data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SmachContainerInitialStatusCmd>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'path))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'initial_states) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:length (cl:slot-value msg 'local_data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SmachContainerInitialStatusCmd>))
  "Converts a ROS message object to a list"
  (cl:list 'SmachContainerInitialStatusCmd
    (cl:cons ':path (path msg))
    (cl:cons ':initial_states (initial_states msg))
    (cl:cons ':local_data (local_data msg))
))
