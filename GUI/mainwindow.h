#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPainter>

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

    void redraw();
private slots:
    void showTime();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
