;; Auto-generated. Do not edit!


(when (boundp 'smach_msgs::SmachContainerStatus)
  (if (not (find-package "SMACH_MSGS"))
    (make-package "SMACH_MSGS"))
  (shadow 'SmachContainerStatus (find-package "SMACH_MSGS")))
(unless (find-package "SMACH_MSGS::SMACHCONTAINERSTATUS")
  (make-package "SMACH_MSGS::SMACHCONTAINERSTATUS"))

(in-package "ROS")
;;//! \htmlinclude SmachContainerStatus.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass smach_msgs::SmachContainerStatus
  :super ros::object
  :slots (_header _path _initial_states _active_states _local_data _info ))

(defmethod smach_msgs::SmachContainerStatus
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:path __path) "")
    ((:initial_states __initial_states) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:active_states __active_states) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:local_data __local_data) "")
    ((:info __info) "")
    )
   (send-super :init)
   (setq _header __header)
   (setq _path (string __path))
   (setq _initial_states __initial_states)
   (setq _active_states __active_states)
   (setq _local_data (string __local_data))
   (setq _info (string __info))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:path
   (&optional __path)
   (if __path (setq _path __path)) _path)
  (:initial_states
   (&optional __initial_states)
   (if __initial_states (setq _initial_states __initial_states)) _initial_states)
  (:active_states
   (&optional __active_states)
   (if __active_states (setq _active_states __active_states)) _active_states)
  (:local_data
   (&optional __local_data)
   (if __local_data (setq _local_data __local_data)) _local_data)
  (:info
   (&optional __info)
   (if __info (setq _info __info)) _info)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; string _path
    4 (length _path)
    ;; string[] _initial_states
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _initial_states)) 4
    ;; string[] _active_states
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _active_states)) 4
    ;; string _local_data
    4 (length _local_data)
    ;; string _info
    4 (length _info)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; string _path
       (write-long (length _path) s) (princ _path s)
     ;; string[] _initial_states
     (write-long (length _initial_states) s)
     (dolist (elem _initial_states)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _active_states
     (write-long (length _active_states) s)
     (dolist (elem _active_states)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string _local_data
       (write-long (length _local_data) s) (princ _local_data s)
     ;; string _info
       (write-long (length _info) s) (princ _info s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; string _path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _initial_states
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _initial_states (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _initial_states i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _active_states
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _active_states (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _active_states i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string _local_data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _local_data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _info
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _info (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get smach_msgs::SmachContainerStatus :md5sum-) "5ba2bb79ac19e3842d562a191f2a675b")
(setf (get smach_msgs::SmachContainerStatus :datatype-) "smach_msgs/SmachContainerStatus")
(setf (get smach_msgs::SmachContainerStatus :definition-)
      "Header header

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

")



(provide :smach_msgs/SmachContainerStatus "5ba2bb79ac19e3842d562a191f2a675b")


