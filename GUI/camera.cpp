#include "mainwindow.h"
#include "camera.h"
#include "ui_mainwindow.h"

#include <QPushButton>
#include <QLabel>
#include <QFrame>
#include <QTextBrowser>
#include <QTimer>
#include <QDateTime>

camera::camera(int x, int y)
{
    int length = x;
    int width = y;

}
int camera::getLength()
{
    return length;
}
int camera::getWidth()
{
    return width;
}
