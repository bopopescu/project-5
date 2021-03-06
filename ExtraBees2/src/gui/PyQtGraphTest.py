'''
Created on 06.07.2013

@author: Richard, Maarten
'''

import numpy as np
import pyqtgraph as pg
from PyQt4 import QtGui, QtCore, QtSql
from gui import SlaveClass
from copy import deepcopy
import math

WEEKDAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
WEEKDAYS_SHORT = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

class PyQtGraphTest(QtGui.QFrame,SlaveClass):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        SlaveClass.__init__(self)
        self.setAutoFillBackground(True)
        p = self.palette()
        #p.setColor(self.backgroundRole(), QtGui.QColor(255,255,255,255))
        self.setPalette(p)
        
        self.data = np.zeros(12 * 24 * 7)
        
        self.communicationQuery = QtSql.QSqlQuery()
        self.communicationQuery.prepare("""SELECT Starttime, (SumTotalBytesSrc + SumTotalBytesDest), (SumPacketSrc + SumPacketDest), SumConnections FROM datavis.macro_networkflow WHERE Starttime >= :starttime1
AND Starttime <= DATE_ADD(:starttime2, INTERVAL 7 DAY);""")
        
        self.health_com_query = QtSql.QSqlQuery()
        self.health_com_query.prepare("""SELECT receivedDate, COUNT(*) FROM datavis.healthserverbyesites WHERE  statusVal = :statusVal AND
        receivedDate >= :receivedDate1 AND receivedDate <= DATE_ADD(:receivedDate2, INTERVAL 7 DAY) GROUP BY receivedDate;""")
                
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        
        self.layout = QtGui.QVBoxLayout()
        self.layout.setMargin(2)
        self.setLayout(self.layout)
        self.timeSlots = 12*24*7
        self.plotWidgetBottom = pg.PlotWidget(name="week")
        self.plotWidgetBottom.getPlotItem().hideAxis("top")
        self.plotWidgetBottom.getPlotItem().showAxis("bottom")
        self.plotWidgetBottom.getPlotItem().showAxis("right")
        self.plotWidgetTop = pg.PlotWidget(name="detail")
        self.plotWidgetTop.getPlotItem().showAxis("right")
        self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("log\n byte/5min",units=None)
        self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("log\n byte/5min",units=None)
        dayLabels = []
        date = self.manager.CT.date()
        for i in range(0,len(WEEKDAYS_SHORT)):
            dayLabels.append((i*288,WEEKDAYS_SHORT[i]+" "+date.toString("MM-dd")))
            date = date.addDays(1)
        timeLabels = []
        for i in range(0,self.timeSlots):
            hour = (i/12)%24
            minute = (i % 12)*5
            string = str(hour).zfill(2)+":"+str(minute).zfill(2)
            timeLabels.append((i,string))

        self.plotWidgetBottom.getPlotItem().getAxis("bottom").setTicks([dayLabels])
        #self.plotWidgetTop.getPlotItem().getAxis("bottom").setTicks([timeLabels])
        
        #self.plotWidgetBottom.getPlotItem().hideAxis("left")
        #self.plotWidgetTop.getPlotItem().hideAxis("left")
        
        self.layout.addWidget(self.plotWidgetTop)
        self.layout.addWidget(self.plotWidgetBottom)
                
        self.top_data_plot = self.plotWidgetBottom.plot(self.data, pen=(0,0,0,200))
        
        self.regionSelection = pg.LinearRegionItem([200,400])
        self.regionSelection.setBounds([0,self.timeSlots])
        self.regionSelection.setBrush(QtGui.QBrush(QtGui.QColor(100,100,255,50)))
        self.regionSelection.setZValue(-10)
        
        self.plotWidgetBottom.addItem(self.regionSelection)
        self.bottom_data_plot = self.plotWidgetTop.plot(self.data, pen=(0,0,0,200))
        
        self.line = pg.InfiniteLine(angle=90, movable=True,pen=(255,0,0,200))
        self.line.setBounds([0,self.timeSlots])
        
        self.plotWidgetTop.addItem(self.line)
        
        self.regionSelection.sigRegionChanged.connect(self.updatePlot)
        self.plotWidgetTop.sigXRangeChanged.connect(self.updateRegion)
        self.line.sigDragged.connect(self.setDateTime)
        
        self.updatePlot()
        self.updateData()
        
        
    def updateData(self):
        #self.plotWidgetBottom.removeItem(self.top_data_plot)
        #self.plotWidgetTop.removeItem(self.bottom_data_plot)
        self.plotWidgetTop.getPlotItem().clear()
        self.plotWidgetBottom.getPlotItem().clear()
        self.plotWidgetTop.addItem(self.line)
        self.plotWidgetBottom.addItem(self.regionSelection)
        
        self.data = np.zeros(12 * 24 * 7)
        
        if (self.manager.NetMode == self.manager.NUM_ERRORS or self.manager.NetMode == self.manager.NUM_WARNINGS or self.manager.NetMode == self.manager.NUM_SERVER_NOT_AVAILABLE):
            loc_datetime = QtCore.QDateTime(self.manager.CW, QtCore.QTime(0,0,0))
            self.health_com_query.bindValue(":receivedDate1", loc_datetime)
            self.health_com_query.bindValue(":receivedDate2",loc_datetime)
            if self.manager.NetMode == self.manager.NUM_WARNINGS:
                self.health_com_query.bindValue(":statusVal", 2)
            elif self.manager.NetMode == self.manager.NUM_ERRORS:
                self.health_com_query.bindValue(":statusVal", 3)
            else:
                self.health_com_query.bindValue(":statusVal", 4)
            self.health_com_query.exec_()
            while (self.health_com_query.next()):
                #calc the index of the array using the datetime
                loc_datetime = self.health_com_query.value(0).toDateTime()
                day_of_week_minutes = (loc_datetime.date().dayOfWeek() - 1) * 24 * 12#* 84 # 7 * 12 
                hour_minutes = loc_datetime.time().hour() * 12
                minute = loc_datetime.time().minute() / 5
                loc_index = day_of_week_minutes + hour_minutes + minute
                self.data[loc_index] = self.health_com_query.value(1).toInt()[0]
        
        else:
            loc_datetime = QtCore.QDateTime(self.manager.CW, QtCore.QTime(0,0,0))
            self.communicationQuery.bindValue(":starttime1", loc_datetime)
            self.communicationQuery.bindValue(":starttime2",loc_datetime)
            self.communicationQuery.exec_()
            
            while (self.communicationQuery.next()):
                #print self.communicationQuery.value(1).toDateTime(), self.communicationQuery.value(0).toInt()[0]
                #calc the index of the array using the datetime
                loc_datetime = self.communicationQuery.value(0).toDateTime()
                day_of_week_minutes = (loc_datetime.date().dayOfWeek() - 1) * 24 * 12#* 84 # 7 * 12 
                hour_minutes = loc_datetime.time().hour() * 12
                minute = loc_datetime.time().minute() / 5
                loc_index = day_of_week_minutes + hour_minutes + minute
                if (self.manager.NetMode == self.manager.TOTALBYTES):
                    self.data[loc_index] = math.log(int(self.communicationQuery.value(1).toString()) + 1)
                elif (self.manager.NetMode == self.manager.THROUGHPUT):
                    self.data[loc_index] = math.log(float(self.communicationQuery.value(1).toString()) / 300.0 + 1)
                elif (self.manager.NetMode == self.manager.NUM_PACKAGES):
                    self.data[loc_index] = (float(self.communicationQuery.value(2).toString()) + 1)
                elif (self.manager.NetMode == self.manager.NUM_PACKAGES_PER_SECOND):
                    self.data[loc_index] = (float(self.communicationQuery.value(2).toString()) / 300.0 + 1)
                elif (self.manager.NetMode == self.manager.NUM_CONNECTIONS):
                    self.data[loc_index] = (float(self.communicationQuery.value(3).toString()) + 1)
                    
        if (self.manager.NetMode == self.manager.TOTALBYTES):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("log\n byte/5min",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("log\n byte/5min",units=None)
        elif (self.manager.NetMode == self.manager.THROUGHPUT):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("log\n byte/s",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("log\n byte/s",units=None)
        elif (self.manager.NetMode == self.manager.NUM_PACKAGES):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("Packages",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("Packages",units=None)
        elif (self.manager.NetMode == self.manager.NUM_PACKAGES_PER_SECOND):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("Packages/s",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("Packages/s",units=None)
        elif (self.manager.NetMode == self.manager.NUM_CONNECTIONS):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("Connections",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("Connections",units=None)
        elif (self.manager.NetMode == self.manager.NUM_ERRORS):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("#Errors",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("#Errors",units=None)
        elif (self.manager.NetMode == self.manager.NUM_WARNINGS):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("#Warnings",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("#Warnings",units=None)
        elif (self.manager.NetMode == self.manager.NUM_SERVER_NOT_AVAILABLE):
            self.plotWidgetBottom.getPlotItem().getAxis("left").setLabel("#Server n.a.",units=None)
            self.plotWidgetTop.getPlotItem().getAxis("left").setLabel("#Server n.a.",units=None)
                        
        self.plotWidgetTop.plot(self.data,  pen=(0,0,0,200), fillLevel = 0.1,  fillBrush = QtGui.QBrush(QtGui.QColor(200,200,200, 100)))
        self.plotWidgetBottom.plot(self.data, pen=(0,0,0,200), fillLevel = 0.1,  fillBrush = QtGui.QBrush(QtGui.QColor(200,200,200, 100)))
        
    def updatePlot(self):
        self.plotWidgetTop.setXRange(*self.regionSelection.getRegion(), padding=0)
        linePos = QtCore.QPointF((self.regionSelection.getRegion()[0]+self.regionSelection.getRegion()[1])/2,0)
        self.line.setPos(linePos)
        tickSpacing = (self.regionSelection.getRegion()[1]-self.regionSelection.getRegion()[0])/10
        if tickSpacing < 1.0:
            tickSpacing = 1
        tickLabels = []
        for i in range(int(self.regionSelection.getRegion()[0]),int(self.regionSelection.getRegion()[1]),int(tickSpacing)):
            tickLabels.append((i,self.timeSlotToString(i)))
        self.plotWidgetTop.getPlotItem().getAxis("bottom").setTicks([tickLabels])
        self.setDateTime()
        
    def updateRegion(self):
        self.regionSelection.setRegion(self.plotWidgetTop.getViewBox().viewRange()[0])
        self.setDateTime()
        
    def timeSlotToString(self,timeslot):
        day = timeslot/(12*24)
        hour = (timeslot/12)%24
        minute = (timeslot % 12)*5
        return WEEKDAYS_SHORT[day]+" "+str(hour).zfill(2)+":"+str(minute).zfill(2)

    def setLinePos(self):
        dayOfWeek = deepcopy(self.manager.CT.date().dayOfWeek()-1)
        day = dayOfWeek*(24*12)
        hour = deepcopy(self.manager.CT.time().hour() *12)
        minute = deepcopy(self.manager.CT.time().minute()/5)
        pos = int(day)+int(hour)+int(minute)
        self.regionSelection.setRegion([pos-144,pos+144])
    
    def setDateTime(self):
        timeslot = self.line.getPos()[0]
        day = self.manager.CW.day() + int(timeslot/(12*24)) 
        month = self.manager.CW.month()
        year = self.manager.CW.year()
        hour = int((timeslot/12)%24)
        minute = int((timeslot) % 12)*5
#       print self.manager.CT  
        self.manager.CT = QtCore.QDateTime(QtCore.QDate(year, month, day), QtCore.QTime(hour,minute,0))
        self.emit(QtCore.SIGNAL('update'))

