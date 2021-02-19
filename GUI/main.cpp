#include "mainwindow.h"

#include <QApplication>
#include <stdio.h>
#include <time.h>
#include <chrono>
#include <thread>

void updatesGUI(MainWindow w)
{
    w.update();
}

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;


    w.show();

    auto start = std::chrono::system_clock::now();

    thread first(updatesGUI(), w);
    first.join();
    //WIP, probably going to use timer function as this is not effective

    //Needs to sleep main thread and recall w.update() every few milliseconds


    /*
    while(true)
    {

        /*
        auto current = std::chrono::system_clock::now();
        std::chrono::duration<int> elapsed_seconds = current-start;
        if(elapsed_seconds.count() % 2 == 0){
            w.update();
        }
         */

    }
    */


    return a.exec();
}
