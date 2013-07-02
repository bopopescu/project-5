'''
Created on 2013-6-18

@author: sijia
'''

from PyQt4 import QtGui,QtCore
from atomicBubble import atomicBubble
from bubbleAnimation import bubbleAnimation
from math import sqrt
from random import randint


bubble1 = atomicBubble(20,20,10,'1st')
bubble1Animation = bubbleAnimation(bubble1)

bubble2 = atomicBubble(0,0,10,'2nd')
bubble2Animation = bubbleAnimation(bubble2)

bubble3 = atomicBubble(0,0,10,'3rd')
bubble3Animation = bubbleAnimation(bubble3)

bubble4 = atomicBubble(0,0,10)
bubble4Animation = bubbleAnimation(bubble4)

bubble5 = atomicBubble(0,0,10)
bubble5Animation = bubbleAnimation(bubble5)

bubble6 = atomicBubble(0,0,10)
bubble6Animation = bubbleAnimation(bubble6)

bubble7 = atomicBubble(0,0,10)
bubble7Animation = bubbleAnimation(bubble7)

bubble8 = atomicBubble(0,0,10)
bubble8Animation = bubbleAnimation(bubble8)

bubble9 = atomicBubble(0,0,10)
bubble9Animation = bubbleAnimation(bubble9)

bubble10 = atomicBubble(0,0,10)
bubble10Animation = bubbleAnimation(bubble10)

bubble11 = atomicBubble(0,0,10)
bubble11Animation = bubbleAnimation(bubble11)

bubble12 = atomicBubble(0,0,10)
bubble12Animation = bubbleAnimation(bubble12)
bubble13 = atomicBubble(0,0,10)
bubble13Animation = bubbleAnimation(bubble13)
bubble14 = atomicBubble(0,0,10)
bubble14Animation = bubbleAnimation(bubble14)
bubble15 = atomicBubble(0,0,10)
bubble15Animation = bubbleAnimation(bubble15)
bubble16 = atomicBubble(0,0,10)
bubble16Animation = bubbleAnimation(bubble16)
bubble17 = atomicBubble(0,0,10)
bubble17Animation = bubbleAnimation(bubble17)
bubble18 = atomicBubble(0,0,10)
bubble18Animation = bubbleAnimation(bubble18)
bubble19 = atomicBubble(0,0,10)
bubble19Animation = bubbleAnimation(bubble19)
bubble20 = atomicBubble(0,0,10)
bubble20Animation = bubbleAnimation(bubble20)
bubble21 = atomicBubble(0,0,10)
bubble21Animation = bubbleAnimation(bubble21)
bubble22 = atomicBubble(0,0,10)
bubble22Animation = bubbleAnimation(bubble22)
bubble23 = atomicBubble(0,0,10)
bubble23Animation = bubbleAnimation(bubble23)
bubble24 = atomicBubble(0,0,10)
bubble24Animation = bubbleAnimation(bubble24)
bubble25 = atomicBubble(0,0,10)
bubble25Animation = bubbleAnimation(bubble25)
bubble26 = atomicBubble(0,0,10)
bubble26Animation = bubbleAnimation(bubble26)
bubble27 = atomicBubble(0,0,10)
bubble27Animation = bubbleAnimation(bubble27)
bubble28 = atomicBubble(0,0,10)
bubble28Animation = bubbleAnimation(bubble28)
bubble29 = atomicBubble(0,0,10)
bubble29Animation = bubbleAnimation(bubble29)
bubble30 = atomicBubble(0,0,10)
bubble30Animation = bubbleAnimation(bubble30)
bubble31 = atomicBubble(0,0,10)
bubble31Animation = bubbleAnimation(bubble31)
bubble32 = atomicBubble(0,0,10)
bubble32Animation = bubbleAnimation(bubble32)
bubble33 = atomicBubble(0,0,10)
bubble33Animation = bubbleAnimation(bubble33)
bubble34 = atomicBubble(0,0,10)
bubble34Animation = bubbleAnimation(bubble34)
bubble35 = atomicBubble(0,0,10)
bubble35Animation = bubbleAnimation(bubble35)
bubble36 = atomicBubble(0,0,10)
bubble36Animation = bubbleAnimation(bubble36)
bubble37 = atomicBubble(0,0,10)
bubble37Animation = bubbleAnimation(bubble37)
bubble38 = atomicBubble(0,0,10)
bubble38Animation = bubbleAnimation(bubble38)
bubble39 = atomicBubble(0,0,10)
bubble39Animation = bubbleAnimation(bubble39)
bubble40 = atomicBubble(0,0,10)
bubble40Animation = bubbleAnimation(bubble40)
bubble41 = atomicBubble(0,0,10)
bubble41Animation = bubbleAnimation(bubble41)
bubble42 = atomicBubble(0,0,10)
bubble42Animation = bubbleAnimation(bubble42)
bubble43 = atomicBubble(0,0,10)
bubble43Animation = bubbleAnimation(bubble43)
bubble44 = atomicBubble(0,0,10)
bubble44Animation = bubbleAnimation(bubble44)
bubble45 = atomicBubble(0,0,10)
bubble45Animation = bubbleAnimation(bubble45)
bubble46 = atomicBubble(0,0,10)
bubble46Animation = bubbleAnimation(bubble46)
bubble47 = atomicBubble(0,0,10)
bubble47Animation = bubbleAnimation(bubble47)
bubble48 = atomicBubble(0,0,10)
bubble48Animation = bubbleAnimation(bubble48)
bubble49 = atomicBubble(0,0,10)
bubble49Animation = bubbleAnimation(bubble49)
bubble50 = atomicBubble(0,0,10)
bubble50Animation = bubbleAnimation(bubble50)




bubblelist = [bubble1, bubble2, bubble3, bubble4, bubble5, bubble6, bubble7, bubble8, bubble9, bubble10, bubble11, bubble12, bubble13, bubble14, bubble15, bubble16, bubble17, bubble18, bubble19, bubble20, bubble21, bubble22, bubble23, bubble24, bubble25, bubble26, bubble27, bubble28, bubble29, bubble30, bubble31, bubble32, bubble33, bubble34, bubble35, bubble36, bubble37, bubble38, bubble39, bubble40, bubble41, bubble42, bubble43, bubble44, bubble45, bubble46, bubble47, bubble48, bubble49, bubble50]
bubbleAnimationlist = [bubble1Animation, bubble2Animation, bubble3Animation, bubble4Animation, bubble5Animation, bubble6Animation, bubble7Animation, bubble8Animation, bubble9Animation, bubble10Animation, bubble11Animation, bubble12Animation, bubble13Animation, bubble14Animation, bubble15Animation, bubble16Animation, bubble17Animation, bubble18Animation, bubble19Animation, bubble20Animation, bubble21Animation, bubble22Animation, bubble23Animation, bubble24Animation, bubble25Animation, bubble26Animation, bubble27Animation, bubble28Animation, bubble29Animation, bubble30Animation, bubble31Animation, bubble32Animation, bubble33Animation, bubble34Animation, bubble35Animation, bubble36Animation, bubble37Animation, bubble38Animation, bubble39Animation, bubble40Animation, bubble41Animation, bubble42Animation, bubble43Animation, bubble44Animation, bubble45Animation, bubble46Animation, bubble47Animation, bubble48Animation, bubble49Animation, bubble50Animation]


bubbledict = {'bubble1':'1st','bubble2':'2nd','bubble3':'3rd','bubble4':'4th'}
bubbleAnimationdict = {'bubble1Animation':'bubble1',
                       'bubble2Animation':'bubble2','bubble3Animation':'bubble3','bubble4Animation':'bubble4'}
bubblenumber = [x for x in range(1,4)]
bubblenamelist = ["1st","2nd","3rd"]
class cloudBubbleScene(QtGui.QGraphicsScene):
    '''
    This class is used to specify the bubble scene. 
    '''

    def __init__(self):
        '''
        Constructor
        ''' 
        super(cloudBubbleScene, self).__init__()
        global bubblelist
#add first bubble into the scene        
        
        for eachbubble in bubblelist:
            self.addItem(eachbubble)
            
#        self.detectCollides()
#assign some animation to the first bubble
#        self.addItem(self.bubble)
#        self.animation = bubbleAnimation(self.bubble)
        
#         self.animation.setbubbleloc(1000000000, QtCore.QPoint(100,-100))
#         self.animation.setbubbleloc(1000000000, QtCore.QPoint(100,100))
#         self.animation.setbubblesize(1000000000, 0.01)
#        self.addAllBubble()
        '''
        Add new bubbles to the scene
        '''
    def addAllBubble(self):
        global bubbledict
        i=0
        for i in range(0,3):
            print 'bubble'+str(i)
#            'bubble'+str(i)=atomicBubble(5+i,5+i,5)
#            self.addItem(self.('bubble'+str(i)))
#            print 'key=%s, value=' % (bubbledict[i])
#            i=i+4

#     def detectCollides(self,radiuslist,locationlist):
#         collidesBubble = []
#         i=0
#         k=1
#         for i in range(0,len(bubblelist)-1):       
#             for k in range(i+1,len(bubblelist)):
#                 j=bubblelist[i].collidesWithItem(bubblelist[k])
#                 if j:
#                     collidesBubble.append(i)
#                     collidesBubble.append(k)
#                     print 'bubble %s collides with bubble %s' % (bubblelist[i].toolTip(),bubblelist[k].toolTip())
#         if len(collidesBubble)==0:
#             print 'Collides Bubbles is zero.'
#         return collidesBubble
    
          
    '''
    Get All bubbles Current Location .
    @return: List of QtCore.QPointF
    '''
            
    def refreshAllBubblesCurrentLoc(self):
        currentbubbleloc=[]
        i=0
        for i in range(0,len(bubblelist)):
            currentbubbleloc.append(bubblelist[i].getCurrentloc())            
        return currentbubbleloc  
    
      
    '''
    Get All bubbles Current Radius .
    @return: List of float
    '''    
    def refreshAllBubblesCurrentRadius(self):
        currentbubbleradius=[]
        i=0
        for i in range(0,len(bubblelist)):
            currentbubbleradius.append(bubblelist[i].getCurrentRadius())   
        return currentbubbleradius
    '''
    Keep all bubble tight.
    '''     
    def keepTight(self):
        global bubblelist
        global bubbleAnimationlist
        
        fakedata=self.getFakeData()
        print fakedata[2]
        self.setAllBubblesNextRadius(fakedata)
#         for i in range(0,50):
#             bubblelist[i].setNextRadius(fakedata[i])
        self.locatefirstandsecondbubble(fakedata[0],fakedata[1])
        nextlocations=[bubblelist[0].nextlocation,bubblelist[1].nextlocation]
        errorbubble=[]

        for i in range(2,50):
            insectionpoints=self.insect(bubblelist[i-2], bubblelist[i-1], fakedata[i])
            if len(insectionpoints)==0:
                errorbubble.append(i)
                nextlocations.append(QtCore.QPointF(0,0))
               #print '+1'
            elif len(insectionpoints)==1:
                
                nextlocations.append(insectionpoints[0])
            else:
                nextlocations.append(insectionpoints[1])
            bubblelist[i].setNextLocation(nextlocations[i])
            while bubblelist[i].detectCollideInNextLocation(fakedata,nextlocations,i):
                bubblelist[i].setNextLocation(QtCore.QPointF(nextlocations[i].x()+1,nextlocations[i].y()+1))
            nextlocations.insert(i, bubblelist[i].getNextLocation())
        scale=[]
         
        for k in range(0,50):
            eachscale=fakedata[k]/bubblelist[k].radius
            scale.append(eachscale)
         
        for j in range(0,50):
            bubbleAnimationlist[j].setbubbleloc(1000000000,nextlocations[j])
            bubbleAnimationlist[j].setbubblesize(1000000000,scale[j])
        
        def newkeeptight(self):
            global bubblelist
            global bubbleAnimationlist
            fakedata = self.getFakeData()
                     
            
            
        
    '''
    Get an empty space for the third bubble
    @param firstbubble:cloudBubble.atomicBubble
    @param secondbubble:cloudBubble.atomicBubble
    @param thirdBubbleradius: float   
    @return: list of QtCore.QPointF. The third bubble center points 
    '''    
    def insect(self,firstbubble,secondbubble,thirdBubbleradius):
        firstbubbleradius=firstbubble.nextradius+thirdBubbleradius
        secondbubbleradius=secondbubble.nextradius+thirdBubbleradius
        insectionPoints=[]
        if self.double_equals(firstbubble.nextlocation.x(),secondbubble.nextlocation.x()) and self.double_equals(firstbubble.nextlocation.y(),secondbubble.nextlocation.y()):
            return insectionPoints
        d = firstbubble.getCenterDistanceWithOtherBubble(secondbubble)
        if d>firstbubbleradius+secondbubbleradius or d<abs(firstbubbleradius-secondbubbleradius):
            insectionPoint = QtCore.QPointF((firstbubble.nextlocation.x()+secondbubble.nextlocation.x())/2,(firstbubble.nextlocation.y()+secondbubble.nextlocation.y())/2)
            print 'Third bubble size is 0'
            insectionPoints = [insectionPoint]
            return insectionPoints        
        a = 2.0 * firstbubbleradius * (firstbubble.nextlocation.x() - secondbubble.nextlocation.x());
        b = 2.0 * secondbubbleradius * (firstbubble.nextlocation.y() - secondbubble.nextlocation.y());
        c = secondbubbleradius * secondbubbleradius - firstbubbleradius * firstbubbleradius- self.distance_sqr(firstbubble.nextlocation, secondbubble.nextlocation)
        p = a * a + b * b
        q = -2.0 * a * c
        
        #if only one insection
        if not self.double_equals(d,firstbubbleradius+secondbubbleradius) or self.double_equals(d,abs(firstbubbleradius-secondbubbleradius)):
            cos_value=-q / p / 2.0;
            sin_value=sqrt(1 - (cos_value * cos_value))
            insectionPoint = QtCore.QPointF(firstbubbleradius*cos_value+firstbubble.nextlocation.x(),firstbubbleradius*sin_value+firstbubble.nextlocation.y())
            if self.double_equals(self.distance_sqr(insectionPoint,secondbubble.nextlocation),secondbubbleradius*secondbubbleradius):
                insectionPoint=QtCore.QPointF(firstbubbleradius*cos_value+firstbubble.nextlocation.x(),firstbubble.nextlocation.y()-firstbubbleradius*sin_value)
            insectionPoints=[insectionPoint]
            return insectionPoints
        
        r = c * c - b * b
        cos_value=[(sqrt(q * q - 4.0 * p * r) - q) / p / 2.0,(-sqrt(q * q - 4.0 * p * r) - q) / p / 2.0]  
        sin_value=[sqrt(1 - cos_value[0] * cos_value[0]),sqrt(1 - cos_value[1] * cos_value[1])]
        insectionPoints1=QtCore.QPointF(firstbubbleradius * cos_value[0] + firstbubble.nextlocation.x(),firstbubbleradius * sin_value[0] + firstbubble.nextlocation.y())
        insectionPoints2=QtCore.QPointF(firstbubbleradius * cos_value[1] + firstbubble.nextlocation.x(),firstbubbleradius * sin_value[1] + firstbubble.nextlocation.y())
        if not self.double_equals(self.distance_sqr(insectionPoints1,secondbubble.nextlocation),secondbubbleradius*secondbubbleradius):
            insectionPoints1=QtCore.QPointF(firstbubbleradius * cos_value[0] + firstbubble.nextlocation.x(),firstbubble.nextlocation.y()-firstbubbleradius*sin_value[0])
        if not self.double_equals(self.distance_sqr(insectionPoints2,secondbubble.nextlocation),secondbubbleradius*secondbubbleradius):
            insectionPoints2=QtCore.QPointF(firstbubbleradius * cos_value[1] + firstbubble.nextlocation.x(), firstbubble.nextlocation.y()-firstbubbleradius * sin_value[1])
        if self.double_equals(insectionPoints1.y(),insectionPoints2.y()) and self.double_equals(insectionPoints1.x(),insectionPoints2.x()):
            if insectionPoints1.y()>0:
                insectionPoints2.setY(-insectionPoints2.y())
            else:
                insectionPoints1.setY(-insectionPoints1.y())
        insectionPoints=[insectionPoints1,insectionPoints2]
        return insectionPoints

    def distance_sqr(self,firstpoint,secondpoint):
        return pow(firstpoint.x()-secondpoint.x(), 2)+pow(firstpoint.y()-secondpoint.y(), 2)
    
    def double_equals(self,a,b):
        ZERO =1e-9
        return abs(a-b)<ZERO

    
    '''
    For testing
    '''
    def getFakeData(self):
        data=[]
        for i in range(0,50):
            x=randint(10,20)
            data.append(x)
        return data 
    
    def locatefirstandsecondbubble(self,firstbubblenextradius,secondbubblenextradius):
        global bubble1
        global bubble2
        bubble1.setNextLocation(QtCore.QPointF(0,0))
        bubble2.setNextLocation(QtCore.QPointF(firstbubblenextradius+secondbubblenextradius,firstbubblenextradius+secondbubblenextradius))
    
    def setAllBubblesNextRadius(self,radiuslist):
        global bubblelist
        for i in range(0,50):
            bubblelist[i].setNextRadius(radiuslist[i])