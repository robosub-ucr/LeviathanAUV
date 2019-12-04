#ifndef CAMERA_H
#define CAMERA_H
#include <mainwindow.h>
#include <QPainter>

#endif // CAMERA_H

class camera : MainWindow {
public:
    camera(int x, int y);
    int getLength();
    int getWidth();
private:
    int length;
    int width;

};
