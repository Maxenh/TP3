import maya.cmds as cmds
import ui
import animation
import importlib
import PySide6
import sys
from PySide6.QtWidgets import QWidget, QApplication, QSpinBox, QLabel,QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt

#fait les mises à jour
importlib.reload(ui)
importlib.reload(animation)

#création de la fenêtre
AnimationWindow = ui.AnimationWindow
window = AnimationWindow()
window.show()

#Get objet sélectionner et update en temps réel
def update_select():
    selection= cmds.ls(sl=True, long=True)

cmds.scriptJob(event=["SelectionChanged", update_select])





