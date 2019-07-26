

#ifndef DESIGNERGQ8892_H
#define DESIGNERGQ8892_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionClose;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QGraphicsView *graphicsView;
    QPushButton *startvideo;
    QPushButton *stopvideo;
    QPushButton *captureimage;
    QMenuBar *menubar;
    QMenu *menuThermal_Camera;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(593, 440);
        actionClose = new QAction(MainWindow);
        actionClose->setObjectName(QStringLiteral("actionClose"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        graphicsView = new QGraphicsView(centralwidget);
        graphicsView->setObjectName(QStringLiteral("graphicsView"));

        gridLayout->addWidget(graphicsView, 0, 0, 1, 3);

        startvideo = new QPushButton(centralwidget);
        startvideo->setObjectName(QStringLiteral("startvideo"));

        gridLayout->addWidget(startvideo, 1, 0, 1, 1);

        stopvideo = new QPushButton(centralwidget);
        stopvideo->setObjectName(QStringLiteral("stopvideo"));

        gridLayout->addWidget(stopvideo, 1, 1, 1, 1);

        captureimage = new QPushButton(centralwidget);
        captureimage->setObjectName(QStringLiteral("captureimage"));

        gridLayout->addWidget(captureimage, 1, 2, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 593, 21));
        menuThermal_Camera = new QMenu(menubar);
        menuThermal_Camera->setObjectName(QStringLiteral("menuThermal_Camera"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuThermal_Camera->menuAction());
        menuThermal_Camera->addSeparator();
        menuThermal_Camera->addAction(actionClose);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Thermal Camera", Q_NULLPTR));
        actionClose->setText(QApplication::translate("MainWindow", "Close", Q_NULLPTR));
        startvideo->setText(QApplication::translate("MainWindow", "Start Video", Q_NULLPTR));
        stopvideo->setText(QApplication::translate("MainWindow", "Stop Video", Q_NULLPTR));
        captureimage->setText(QApplication::translate("MainWindow", "Capture Image", Q_NULLPTR));
        menuThermal_Camera->setTitle(QApplication::translate("MainWindow", "File", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // DESIGNERGQ8892_H