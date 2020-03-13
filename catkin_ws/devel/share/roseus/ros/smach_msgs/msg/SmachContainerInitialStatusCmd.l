;; Auto-generated. Do not edit!


(when (boundp 'smach_msgs::SmachContainerInitialStatusCmd)
  (if (not (find-package "SMACH_MSGS"))
    (make-package "SMACH_MSGS"))
  (shadow 'SmachContainerInitialStatusCmd (find-package "SMACH_MSGS")))
(unless (find-package "SMACH_MSGS::SMACHCONTAINERINITIALSTATUSCMD")
  (make-package "SMACH_MSGS::SMACHCONTAINERINITIALSTATUSCMD"))

(in-package "ROS")
;;//! \htmlinclude SmachContainerInitialStatusCmd.msg.html


(defclass smach_msgs::SmachContainerInitialStatusCmd
  :super ros::object
  :slots (_path _initial_states _local_data ))

(defmethod smach_msgs::SmachContainerInitialStatusCmd
  (:init
   (&key
    ((:path __path) "")
    ((:initial_states __initial_states) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:local_data __local_data) "")
    )
   (send-super :init)
   (setq _path (string __path))
   (setq _initial_states __initial_states)
   (setq _local_data (string __local_data))
   self)
  (:path
   (&optional __path)
   (if __path (setq _path __path)) _path)
  (:initial_states
   (&optional __initial_states)
   (if __initial_states (setq _initial_states __initial_states)) _initial_states)
  (:local_data
   (&optional __local_data)
   (if __local_data (setq _local_data __local_data)) _local_data)
  (:serialization-length
   ()
   (+
    ;; string _path
    4 (length _path)
    ;; string[] _initial_states
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _initial_states)) 4
    ;; string _local_data
    4 (length _local_data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _path
       (write-long (length _path) s) (princ _path s)
     ;; string[] _initial_states
     (write-long (length _initial_states) s)
     (dolist (elem _initial_states)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string _local_data
       (write-long (length _local_data) s) (princ _local_data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _initial_states
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _initial_states (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _initial_states i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string _local_data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _local_data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get smach_msgs::SmachContainerInitialStatusCmd :md5sum-) "45f8cf31fc29b829db77f23001f788d6")
(setf (get smach_msgs::SmachContainerInitialStatusCmd :datatype-) "smach_msgs/SmachContainerInitialStatusCmd")
(setf (get smach_msgs::SmachContainerInitialStatusCmd :definition-)
      "# The path to the node in the server
string path

# The desired initial state(s)
string[] initial_states

# Initial values for the local user data of the state machine
# A pickled user data structure
# i.e. the UserData's internal dictionary
string local_data

")



(provide :smach_msgs/SmachContainerInitialStatusCmd "45f8cf31fc29b829db77f23001f788d6")


