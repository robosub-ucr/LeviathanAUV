#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include "darknet_ros_msgs/BoundingBoxes.h"
#include <sstream>

//Create a publisher for each value needed for each object
ros::Publisher flat_x;
ros::Publisher flat_y;
ros::Publisher flat_area;


std_msgs::Float64 X_msg;
std_msgs::Float64 Y_msg;
std_msgs::Float64 Area_msg;
void bounding_box_callback(const darknet_ros_msgs::BoundingBoxes::ConstPtr& box)
{
	X_msg.data =  (box->bounding_boxes[0].xmax + box->bounding_boxes[0].xmin)/2;//Gives the center x value
	Y_msg.data =  (box->bounding_boxes[0].ymax + box->bounding_boxes[0].ymin)/2;//Gives the center y value
	//gives the area that the bounding box has
	Area_msg.data = (box->bounding_boxes[0].xmax - box->bounding_boxes[0].xmin) * (box->bounding_boxes[0].ymax - box->bounding_boxes[0].ymin);
	
	//You need to check what object is being detected to publish to the right topic
	if(box->bounding_boxes[0].Class == "Flat_Buoy")
	{
		flat_x.publish(X_msg);
		flat_y.publish(Y_msg);
		flat_area.publish(Area_msg);
	}
}
int main(int argc, char **argv)
{
  	ros::init(argc, argv, "dn_parser");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscribe("/darknet_ros/bounding_boxes", 100, bounding_box_callback);

	//initialize the publishers from earlier
	flat_x = n.advertise<std_msgs::Float64>("/Flat_Buoy_X",10);
	flat_y = n.advertise<std_msgs::Float64>("/Flat_Buoy_Y",10);
	flat_area = n.advertise<std_msgs::Float64>("/Flat_Buoy_Area",10);
	while(ros::ok())
	{
		ros::spinOnce();
		
	}

	return 0;
}
