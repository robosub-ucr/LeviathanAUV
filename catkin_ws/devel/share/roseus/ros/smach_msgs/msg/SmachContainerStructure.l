;; Auto-generated. Do not edit!


(when (boundp 'smach_msgs::SmachContainerStructure)
  (if (not (find-package "SMACH_MSGS"))
    (make-package "SMACH_MSGS"))
  (shadow 'SmachContainerStructure (find-package "SMACH_MSGS")))
(unless (find-package "SMACH_MSGS::SMACHCONTAINERSTRUCTURE")
  (make-package "SMACH_MSGS::SMACHCONTAINERSTRUCTURE"))

(in-package "ROS")
;;//! \htmlinclude SmachContainerStructure.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass smach_msgs::SmachContainerStructure
  :super ros::object
  :slots (_header _path _children _internal_outcomes _outcomes_from _outcomes_to _container_outcomes ))

(defmethod smach_msgs::SmachContainerStructure
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:path __path) "")
    ((:children __children) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:internal_outcomes __internal_outcomes) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:outcomes_from __outcomes_from) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:outcomes_to __outcomes_to) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:container_outcomes __container_outcomes) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _path (string __path))
   (setq _children __children)
   (setq _internal_outcomes __internal_outcomes)
   (setq _outcomes_from __outcomes_from)
   (setq _outcomes_to __outcomes_to)
   (setq _container_outcomes __container_outcomes)
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
  (:children
   (&optional __children)
   (if __children (setq _children __children)) _children)
  (:internal_outcomes
   (&optional __internal_outcomes)
   (if __internal_outcomes (setq _internal_outcomes __internal_outcomes)) _internal_outcomes)
  (:outcomes_from
   (&optional __outcomes_from)
   (if __outcomes_from (setq _outcomes_from __outcomes_from)) _outcomes_from)
  (:outcomes_to
   (&optional __outcomes_to)
   (if __outcomes_to (setq _outcomes_to __outcomes_to)) _outcomes_to)
  (:container_outcomes
   (&optional __container_outcomes)
   (if __container_outcomes (setq _container_outcomes __container_outcomes)) _container_outcomes)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; string _path
    4 (length _path)
    ;; string[] _children
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _children)) 4
    ;; string[] _internal_outcomes
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _internal_outcomes)) 4
    ;; string[] _outcomes_from
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _outcomes_from)) 4
    ;; string[] _outcomes_to
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _outcomes_to)) 4
    ;; string[] _container_outcomes
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _container_outcomes)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; string _path
       (write-long (length _path) s) (princ _path s)
     ;; string[] _children
     (write-long (length _children) s)
     (dolist (elem _children)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _internal_outcomes
     (write-long (length _internal_outcomes) s)
     (dolist (elem _internal_outcomes)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _outcomes_from
     (write-long (length _outcomes_from) s)
     (dolist (elem _outcomes_from)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _outcomes_to
     (write-long (length _outcomes_to) s)
     (dolist (elem _outcomes_to)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _container_outcomes
     (write-long (length _container_outcomes) s)
     (dolist (elem _container_outcomes)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; string _path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _children
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _children (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _children i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _internal_outcomes
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _internal_outcomes (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _internal_outcomes i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _outcomes_from
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _outcomes_from (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _outcomes_from i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _outcomes_to
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _outcomes_to (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _outcomes_to i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _container_outcomes
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _container_outcomes (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _container_outcomes i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get smach_msgs::SmachContainerStructure :md5sum-) "3d3d1e0d0f99779ee9e58101a5dcf7ea")
(setf (get smach_msgs::SmachContainerStructure :datatype-) "smach_msgs/SmachContainerStructure")
(setf (get smach_msgs::SmachContainerStructure :definition-)
      "Header header

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

")



(provide :smach_msgs/SmachContainerStructure "3d3d1e0d0f99779ee9e58101a5dcf7ea")


