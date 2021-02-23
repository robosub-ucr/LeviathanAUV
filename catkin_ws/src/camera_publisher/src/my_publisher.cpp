#include <ros/ros.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <sstream> // for converting the command line parameter to integer
#include <std_msgs/Int16.h>
#include <iostream>


int cam_index = 0;
//bool change = false;

void index_callback(const std_msgs::Int16::ConstPtr& msg) {
  //cv::VideoCapture cap(msg.data);
  cam_index = msg->data;
  //change = true;
}

int main(int argc, char** argv)
{
  // Check if video source has been passed as a parameter
  if(argv[1] == NULL) return 1;

  ros::init(argc, argv, "camera_publisher");
  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<sensor_msgs::Image&>("camera/image", 1);
  ros::Subscriber sub = nh.subscribe("camera/index", 1, index_callback);
  //image_transport::ImageTransport it(nh);
  //image_transport::Publisher pub = it.advertise("camera/image", 1);

  // Convert the passed as command line parameter index for the video device to an integer
  std::istringstream video_sourceCmd(argv[1]);

  int video_source;
  // Check if it is indeed a number
  if(!(video_sourceCmd >> video_source)) return 1;
  cam_index = video_source;
  //cv::VideoCapture cap(video_source);
  cv::VideoCapture cap(0);
  cv::VideoCapture cap2(2);
  // Check if video device can be opened with the given index
  if(!cap.isOpened()) return 1;
  cv::Mat frame;
  sensor_msgs::ImagePtr msg;

  ros::Rate loop_rate(5);
  while (nh.ok()) {
    if(cam_index == 0){
      cap >> frame;
    }else{
      cap2>> frame;
    }
    // Check if grabbed frame is actually full with some content
    if(!frame.empty()) {
      msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
      pub.publish(msg);
      cv::waitKey(1);
    }
    ros::spinOnce();
    loop_rate.sleep();
  }
}
