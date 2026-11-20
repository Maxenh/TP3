from PySide6.QtWidgets import QWidget, QSpinBox, QLabel,QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt
import animation

class AnimationWindow (QWidget):
    def __init__(self):
        #set une boite
        #COULEUR
        super().__init__()

        #always on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle("Animation Creator")
        self.resize(550,550)

        self.layout = QVBoxLayout()
        self.setStyleSheet("""QSpinBox {min-width: 50px; min-height: 20px; font-size: 14px;}""")


        #Title ligne 1
        self.title_first = QHBoxLayout()
        self.title_first.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.title_lenght = QLabel("Paramètres de l'animation:")
        self.title_lenght.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.title_first.addWidget(self.title_lenght)

        #Ligne 1
        self.layout_first = QHBoxLayout()
        self.layout_first.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        

        #DUREE ANIMATION
        self.label_lenght = QLabel("Durée de l'animation: ")
        self.lenght_box = QSpinBox()

        self.layout_first.addWidget(self.label_lenght)
        self.layout_first.addWidget(self.lenght_box)

        self.lenght_box.setMaximum(120)
        self.lenght_box.setWrapping(True)
        

        #ESPACE ENTRE LES KEYS
        self.label_key = QLabel("Espacement entre les clées: ")
        self.key_space = QSpinBox()


        
        self.layout_first.addWidget(self.label_key)
        self.layout_first.addWidget(self.key_space)

        self.key_space.setMaximum(50)
    
        self.key_space.setWrapping(True)

        #Titre ligne 2
        self.title_second = QHBoxLayout()
        self.title_second.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.title_trans = QLabel("Paramètres de translation:")
        self.title_trans.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.title_second.addWidget(self.title_trans)


        #Ligne 2
        self.layout_second = QHBoxLayout()
        self.layout_second.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #LES MINS DE TRANSLATION
        #X
        self.label_min_x = QLabel("Min X: ")
        self.transmin_x = QSpinBox()
        self.transmin_x.setMinimum(-99)

        self.layout_second.addWidget(self.label_min_x)
        self.layout_second.addWidget(self.transmin_x)
        #Y
        self.label_transmin_y = QLabel("Min Y: ")
        self.transmin_y = QSpinBox()
        self.transmin_y.setMinimum(-99)

        self.layout_second.addWidget(self.label_transmin_y)
        self.layout_second.addWidget(self.transmin_y)
        #Z
        self.label_transmin_z = QLabel("Min Z: ")
        self.transmin_z = QSpinBox()
        self.transmin_z.setMinimum(-99)

        self.layout_second.addWidget(self.label_transmin_z)
        self.layout_second.addWidget(self.transmin_z)


        #Ligne 3
        self.layout_third = QHBoxLayout()
        self.layout_third.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #LES MAXS DE TRANSLATION
        #X
        self.label_transmax_x = QLabel("Max X: ")
        self.transmax_x = QSpinBox()
        self.transmax_x.setMinimum(-99)

        self.layout_third.addWidget(self.label_transmax_x)
        self.layout_third.addWidget(self.transmax_x)
        #Y
        self.label_transmax_y = QLabel("Max Y: ")
        self.transmax_y = QSpinBox()
        self.transmax_y.setMinimum(-99)

        self.layout_third.addWidget(self.label_transmax_y)
        self.layout_third.addWidget(self.transmax_y)
        #Z
        self.label_transmax_z = QLabel("Max Z: ")
        self.transmax_z = QSpinBox()
        self.transmax_z.setMinimum(-99)

        self.layout_third.addWidget(self.label_transmax_z)
        self.layout_third.addWidget(self.transmax_z)


        #Titre ligne 4
        self.title_fourth = QHBoxLayout()
        self.title_fourth.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.title_rot = QLabel("Paramètres de rotation:")
        self.title_rot.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.title_fourth.addWidget(self.title_rot)

        #Ligne 4
        self.layout_fourth = QHBoxLayout()
        self.layout_fourth.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #LES MINS DE ROTATION
        #X
        self.label_rotmin_x = QLabel("Min X: ")
        self.rotmin_x = QSpinBox()
        self.rotmin_x.setMinimum(-99)

        self.layout_fourth.addWidget(self.label_rotmin_x)
        self.layout_fourth.addWidget(self.rotmin_x)
        #Y
        self.label_rotmin_y = QLabel("Min Y: ")
        self.rotmin_y = QSpinBox()
        self.rotmin_y.setMinimum(-99)

        self.layout_fourth.addWidget(self.label_rotmin_y)
        self.layout_fourth.addWidget(self.rotmin_y)
        #Z
        self.label_rotmin_z = QLabel("Min Z: ")
        self.rotmin_z = QSpinBox()
        self.rotmin_z.setMinimum(-99)

        self.layout_fourth.addWidget(self.label_rotmin_z)
        self.layout_fourth.addWidget(self.rotmin_z)


        #Ligne 5
        self.layout_fifth = QHBoxLayout()
        self.layout_fifth.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #LES MAXS DE ROTATION
        #X
        self.label_rotmax_x = QLabel("Max X: ")
        self.rotmax_x = QSpinBox()
        self.rotmax_x.setMinimum(-99)

        self.layout_fifth.addWidget(self.label_rotmax_x)
        self.layout_fifth.addWidget(self.rotmax_x)
        #Y
        self.label_rotmax_y = QLabel("Max Y: ")
        self.rotmax_y = QSpinBox()
        self.rotmax_y.setMinimum(-99)

        self.layout_fifth.addWidget(self.label_rotmax_y)
        self.layout_fifth.addWidget(self.rotmax_y)
        #Z
        self.label_rotmax_z = QLabel("Max Z: ")
        self.rotmax_z = QSpinBox()
        self.rotmax_z.setMinimum(-99)

        self.layout_fifth.addWidget(self.label_rotmax_z)
        self.layout_fifth.addWidget(self.rotmax_z)



        #Titre Ligne 6
        self.title_sixth = QHBoxLayout()
        self.title_sixth.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.title_scale = QLabel("Paramètres de taille:")
        self.title_scale.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.title_sixth.addWidget(self.title_scale)


        #Ligne 6
        self.layout_sixth = QHBoxLayout()
        self.layout_sixth.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #LES MINS DE TAILLE 
        #X
        self.label_scalemin_x = QLabel("Min X: ")
        self.scalemin_x = QSpinBox()
        
        self.layout_sixth.addWidget(self.label_scalemin_x)
        self.layout_sixth.addWidget(self.scalemin_x)
        #Y
        self.label_scalemax_y = QLabel("Min Y: ")
        self.scalemin_y = QSpinBox()
        
        self.layout_sixth.addWidget(self.label_scalemax_y)
        self.layout_sixth.addWidget(self.scalemin_y)
        #Z
        self.label_scalemax_z = QLabel("Min Z: ")
        self.scalemin_z = QSpinBox()
        
        self.layout_sixth.addWidget(self.label_scalemax_z)
        self.layout_sixth.addWidget(self.scalemin_z)
        
        
        #Ligne 5
        self.layout_seven = QHBoxLayout()
        self.layout_seven.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        #LES MAXS DE ROTATION
        #X
        self.label_scalemax_x = QLabel("Max X: ")
        self.scalemax_x = QSpinBox()
        
        self.layout_seven.addWidget(self.label_scalemax_x)
        self.layout_seven.addWidget(self.scalemax_x)
        #Y
        self.label_scalemax_y = QLabel("Max Y: ")
        self.scalemax_y = QSpinBox()
        
        self.layout_seven.addWidget(self.label_scalemax_y)
        self.layout_seven.addWidget(self.scalemax_y)
        #Z
        self.label_scalemax_z = QLabel("Max Z: ")
        self.scalemax_z = QSpinBox()
        
        self.layout_seven.addWidget(self.label_scalemax_z)
        self.layout_seven.addWidget(self.scalemax_z)

        



        #BOUTON GÉNÉRATION 
        #Ligne 6
        self.layout_generate = QHBoxLayout()

        self.generate_button = QPushButton("Generation")
        self.generate_button.setFixedSize(250,50)
        self.generate_button.setStyleSheet("""QPushButton {font-size: 15px; font-weight: bold;}""")
        self.layout_generate.addWidget(self.generate_button, alignment=Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.generate_button.clicked.connect(lambda:animation.generation(
            self.lenght_box.value(), self.key_space.value(),
            trans_min=[self.transmin_x.value(),self.transmin_y.value(), self.transmin_z.value()],
            trans_max=[self.transmax_x.value(),self.transmax_y.value(), self.transmax_z.value()],
            rot_min=[self.rotmin_x.value(),self.rotmin_y.value(), self.rotmin_z.value()],
            rot_max=[self.rotmax_x.value(),self.rotmax_y.value(), self.rotmax_z.value()],
            scale_min=[self.scalemin_x.value(),self.scalemin_y.value(), self.scalemin_z.value()],
            scale_max=[self.scalemax_x.value(),self.scalemax_y.value(), self.scalemax_z.value()]
            ))

       







        self.layout.addLayout(self.title_first)
        self.layout.addLayout(self.layout_first)
        self.layout.addLayout(self.title_second)
        self.layout.addLayout(self.layout_second)
        self.layout.addLayout(self.layout_third)
        self.layout.addLayout(self.title_fourth)
        self.layout.addLayout(self.layout_fourth)
        self.layout.addLayout(self.layout_fifth)
        self.layout.addLayout(self.title_sixth)
        self.layout.addLayout(self.layout_sixth)
        self.layout.addLayout(self.layout_seven)
        self.layout.addLayout(self.layout_generate)
        
        
        self.setLayout(self.layout) 