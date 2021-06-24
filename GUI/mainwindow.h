#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include "camera.h"
#include <QMainWindow>
#include <QPainter>
#include <QScopedPointer>
#include <QCamera>
#include <QCameraInfo>
#include <QAction>
#include <QMediaRecorder>
#include <QCameraViewfinder>
#include <QPushButton>
#include "dialog.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT


public:
    MainWindow(QWidget *parent = nullptr);

    ~MainWindow();

    virtual void paintEvent(QPaintEvent *event);
    void videoFeed();
    void update();
    void redraw();




    public slots:




private slots:
        void showTime();

private:
     Ui::MainWindow *ui;

};
#endif // MAINWINDOW_H

