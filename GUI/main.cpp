#include "mainwindow.h"

#include <QApplication>
#include <stdio.h>
#include <time.h>
#include <chrono>
#include <unistd.h>
#include <iostream>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    w.redraw();




    /*
    //WIP, probably going to use timer function as this is not effective
    auto start = std::chrono::system_clock::now();

    //Needs to sleep main thread and recall w.update() every few milliseconds

    while(1)
    {
        auto end = std::chrono::system_clock::now();
        std::chrono::duration<double> elapsed_seconds = end - start;
        if (elapsed_seconds > std::chrono::seconds{5}){
            start = std::chrono::system_clock::now();
            w.redraw();
        }
    }
    */



    return a.exec();
}
