from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QFormLayout, QWidget, QVBoxLayout, QSpinBox, QPushButton, QLabel, QLineEdit, QTabWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QIntValidator, QDoubleValidator, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from .plot import Plotting
from tools.tests_ea_tag import make_dir_a_tag
import paho.mqtt.client as mqtt
import requests
import json
import datetime
from ast import literal_eval









class Run(QGroupBox):

    message = pyqtSignal(str)
    dataSignal = pyqtSignal(bool)

    def __init__(self, parent = None):
        super(QGroupBox, self).__init__(parent)

        
        #self.setFixedSize(250,271)
        self.vbox = QVBoxLayout(self)
        self.form = QFormLayout(self)
        
        self.icon = QPixmap("C:/Users/ZZZZZZ/Desktop/projeto_dashboardApp/src/icons/motor.png")
        self.lbl = QLabel()
        
        self.lbl.setPixmap(self.icon)

        self.motor_label = QLineEdit(self)

        self.pot = QLineEdit(self)
        self.pot.setValidator(QIntValidator())
        

        self.fp = QLineEdit(self)
        self.fp.setValidator(QDoubleValidator(0,1,2))

        self.rot = QLineEdit(self)
        self.rot.setValidator(QIntValidator())

        self.rendimento = QLineEdit(self)
        self.rendimento.setValidator(QDoubleValidator(0,1,2))

        self.create = QPushButton("criar")
        self.create.clicked.connect(self.register)
        self.create.setObjectName("create")
        self.create.setFixedWidth(100)
        
        self.vbox.setSpacing(10)
        
        self.vbox.addWidget(self.lbl, alignment=Qt.AlignCenter)
        self.form.addRow("tag:          ", self.motor_label)
        self.form.addRow("potencia (HP):          ", self.pot)
        self.form.addRow("fp:          ", self.fp)
        self.form.addRow("rotação:          ",self.rot)
        self.form.addRow("rendimento:          ",self.rendimento)
        self.vbox.addLayout(self.form)
        self.vbox.addWidget(self.create, alignment=Qt.AlignHCenter)
        self.vbox.addStretch()
        self.setLayout(self.vbox)
    
        
      
    
    def register(self, mark):
        try:
            time_now = datetime.datetime.now().strftime("%d/%m/%y-%H:%M:%S")
            self.data = {
                            "tag":str(self.motor_label.text()),
                            "potencia":int(self.pot.text()),
                            "fp":float(self.fp.text()),
                            "rotacao":int(self.rot.text()),
                            "rendimento":float(self.rendimento.text()),
                            "data":str(time_now),
                            "ensaios":0
                        }
            
            try:
                
                result = make_dir_a_tag(self.data['tag'])

                if result[1]:
                    mqttc = mqtt.Client('3')
                    mqttc.connect('mqtt.eclipse.org', 1883)
                    mqttc.publish('joelho1', str(self.data))
                

            except:
                self.message.emit(result[0])

            else:
                self.message.emit(result[0])
                
                self.dataSignal.emit(True)
        except:
            self.message.emit('Todos os campos obrigatórios!.')
        
        
     

            

        
            
            

        
 

        




        
  
        
        
 



