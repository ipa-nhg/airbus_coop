#!/usr/bin/env python
################################################################################
#
# Copyright Airbus Group SAS 2015
# All rigths reserved.
#
# File Name : message_box.py
# Authors : Martin Matignon
#
# If you find any bug or if you have any question please contact
# Adolfo Suarez Roos <adolfo.suarez@airbus.com>
# Martin Matignon <martin.matignon.external@airbus.com>
#
#
################################################################################

import rospy

from python_qt_binding.QtGui import *
from python_qt_binding.QtCore import *

from pyqt_agi_extend.QtAgiCore import loadRsc

rsc = loadRsc("pyqt_agi_extend")

## @package: message_box
##
## @version 1.0
## @author  Matignon Martin
## @date    Last modified 22/03/2016
## @class QPopup
## @brief Popup object.
## @class MessageBox
## @brief Class for redefine QMessageBox.
class QAgiMessageBox(QMessageBox):
    
    STYLE = "QLabel{font-size: 18pt; font-weight:40; color: #000000;} \
             QPushButton{ background-color:qlineargradient(x1: 0, \
                                                           y1: 0, \
                                                           x2: 0, \
                                                           y2: 1, \
                                                           stop: 0 #2ca1cf, \
                                                           stop: 1 #0482bb); \
                          border: 2px #616763; border-radius: 5px; \
                          font-size: 16pt; font-weight:40; color: #000000;\
                          width:100px; \
                          height:40px}"
                          
    INFO     = QMessageBox.Information
    WARN     = QMessageBox.Warning
    CRITICAL = QMessageBox.Critical
    QUESTION = QMessageBox.Question
     
    def __init__(self, type=None, msg=None):
        """! The constructor."""
        
        QMessageBox.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(QSize(600,300))
        
        style_base = ""
        
        if type == QMessageBox.Information:
            self.setIcon(QMessageBox.Information)
            style_base = "QMessageBox{ border: 2px solid bleu;}"
        elif type == QMessageBox.Warning:
            self.setIcon(QMessageBox.Warning)
            style_base = "QMessageBox{ border: 2px solid yellow;}"
        elif type == QMessageBox.Critical:
            self.setIcon(QMessageBox.Critical)
            style_base = "QMessageBox{ border: 2px solid red;}"
        elif type == QMessageBox.Question:
            self.setIcon(QMessageBox.Question)
            style_base = "QMessageBox{ border: 2px solid blue;}"
        else:
            self.setIcon(QMessageBox.NoIcon)
            
        self.setStyleSheet(style_base+self.STYLE)
        
        if msg is not None:
            self.setText(msg)
            
    def setStyle(self, style):
        self.STYLE = style
        
    
#End of file