#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "compass.h"

#include <QPushButton>
#include <QLabel>
#include <QFrame>
#include <QTextBrowser>
#include <QTimer>
#include <QDateTime>

//temporary resize fix
const double RESIZE_CONSTANT(0.75);

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->pushButton->setText("System View");
    ui->pushButton_2->setText("Roscore");
    ui->pushButton_3->setText("AHRS");
    ui->pushButton_4->setText("TEST");
    ui->pushButton_5->setText("STM32");
    ui->pushButton_6->setText("Camera 1");
    ui->pushButton_7->setText("Camera 2");
    ui->pushButton_8->setText("SM's");
    QTimer *timer = new QTimer(this);
    connect(timer , SIGNAL(timeout()) , this, SLOT(showTime()));
    timer->start();



}
void MainWindow::paintEvent(QPaintEvent *event){

    //draws compass
    //currently trying to figure out how to move this to a seperate class
    //to make it much more easily customizable
    //work in progress



    //creates a painter
    QPainter painter(this);

    //creates the compass
    Compass c(600 * RESIZE_CONSTANT,400 * RESIZE_CONSTANT);

    //sets fill to be blue
    painter.setBrush(Qt::blue);

    //sets the center to be 600, 400
    painter.translate(c.getCenterX(),c.getCenterY());

    //creates a brush, more on that later
    QBrush brush;

    //creates a pen, which dictates the color and style of the lines
    QPen pen;
    pen.setColor(Qt::white);
    pen.setWidth(5);

    //puts pen into painter
    painter.setPen(pen);

    //draws a rectagle from the top left corner (x,y, width, height)
    c.setSquareWidth(200 * RESIZE_CONSTANT);
    painter.drawRect(QRect(-c.getSquareWidth()/2, -c.getSquareWidth()/2, c.getSquareWidth(), c.getSquareWidth()));

    painter.setBrush(Qt::black);

    //draws an ellepse from top left corner (x,y, center width, center height)
    painter.drawEllipse(-c.getSquareWidth()/2, -c.getSquareWidth()/2, c.getSquareWidth(), c.getSquareWidth());


    //defines a the points of a polygon
    c.setNeedleWidth(10 * RESIZE_CONSTANT);
    c.setNeedleHeight(100 * RESIZE_CONSTANT);
    QPolygon pointer;
    pointer << QPoint(0, -c.getNeedleHeight()) << QPoint(-c.getNeedleWidth(), 0) << QPoint(c.getNeedleWidth(), 0);

    // defines a path for the brush to take to draw the polygon
    QPainterPath path;
    path.addPolygon(pointer);


    //rotates the orientation of the painter so that the next objects will be rotated
    c.setNeedleAngle(-45);
    painter.rotate(c.getNeedleAngle());
    painter.drawPolygon(pointer);
    painter.fillPath(path, brush); //fills the polygon

    painter.rotate(-c.getNeedleAngle()); //resets orientation of painter

    //draw target
    c.setTargetAngle(80);
    pen.setBrush(Qt::red);
    painter.setBrush(Qt::red);
    painter.rotate(c.getTargetAngle());
    painter.drawEllipse(-10 * RESIZE_CONSTANT, -c.getNeedleHeight() + -10 , 20 * RESIZE_CONSTANT, 20 * RESIZE_CONSTANT);
    painter.rotate(-c.getTargetAngle());

    //reset translate
    painter.translate(-c.getCenterX(),-c.getCenterY());



    //draw depth table (WIP)
    painter.translate(800 * RESIZE_CONSTANT, 250 * RESIZE_CONSTANT);
    pen.setColor(Qt::black);
    painter.setPen(pen);
    painter.setBrush(Qt::black);

    painter.drawLine(0, 0, 600 * RESIZE_CONSTANT, 0);
    painter.drawLine(0, 0, 0, -200 * RESIZE_CONSTANT);

    pen.setColor(Qt::red);
    painter.setPen(pen);
    painter.setBrush(Qt::blue);

    int points = 4;
    int cake[4][2];
    int xStep = 100 * RESIZE_CONSTANT;
    int yStep = 10 * RESIZE_CONSTANT;

    for (int i = 1; i <= points; i++){
        painter.drawEllipse(xStep * i, yStep * -i, 10 * RESIZE_CONSTANT, 10 * RESIZE_CONSTANT);
        cake[i - 1][0] = xStep * i + 5;
        cake[i - 1][1] = yStep * -i + 5;
        yStep = yStep * 1.7;
    }

    pen.setColor(Qt::blue);
    painter.setPen(pen);

    for (int j = 0; j < points - 1; j++){
        painter.drawLine(cake[j][0], cake[j][1], cake[j + 1][0], cake[j + 1][1]);
    }

    painter.translate(-800 * RESIZE_CONSTANT,-250 * RESIZE_CONSTANT);



    //depth gauge (WIP)
    painter.translate(600 * RESIZE_CONSTANT, 150 * RESIZE_CONSTANT);
    painter.rotate(-50);
    pen.setColor(Qt::black);
    painter.setPen(pen);
    painter.drawLine(0, 0, -115, 0);
    painter.drawLine(0, 0, 115, 0);
    pen.setColor(Qt::blue);
    painter.setPen(pen);
    painter.setBrush(Qt::white);
    painter.drawEllipse(-60, -30, 120, 60);
    painter.setBrush(Qt::red);
    painter.drawEllipse(-30, -7, 15, 15);
    pen.setColor(Qt::black);
    painter.setPen(pen);
    painter.rotate(-50);
    painter.translate(-650,-150);

}



void MainWindow::showTime(){

    QTime time = QTime::currentTime();

    QString time_text = time.toString("hh : mm : ss");
    if ((time.second() % 2) == 0){
        time_text[3] = ' ';
        time_text[8] = ' ';

    }
    ui->Clock->setText(time_text);

}

MainWindow::~MainWindow()
{
    delete ui;
}

