#include "mainwindow.h"
#include "Depth.h"
#include "ui_mainwindow.h"

#include <QPushButton>
#include <QLabel>
#include <QFrame>
#include <QTextBrowser>
#include <QTimer>
#include <QDateTime>

Depth::Depth(int centX, int centY) {
    centerX = centX;
    centerY = centY;

}

int Depth::getCenterX() {
    return centerX;
}

int Depth::getCenterY() {
    return centerY;
}

int Depth::getWidth(){
    return width;
}

int Depth::getLength(){
    return length;
}

int Depth::getSWidth(){
    return swidth;
}

int Depth::getAngle(){
    return angle;
}

void Depth::setWidth(int w){
    width = w;
    swidth = w/4;
}

void Depth::setLength(int l){
    length = l;
}

void Depth::setAngle(int a){
    angle = a;
}
