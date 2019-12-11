#ifndef DEPTH_H
#define DEPTH_H

#include <mainwindow.h>

class Depth : MainWindow {

public:
    Depth(int centerX, int centerY);

    int getCenterX();
    int getCenterY();
    int getWidth();
    int getLength();
    int getSWidth();
    int getAngle();

    void setWidth(int sw);
    void setLength(int nw);
    void setAngle(int a);

private:
    int centerX;
    int centerY;
    int width;
    int angle;
    int length;
    int swidth;

};

#endif // DEPTH_H
