import maya.cmds as cmds
import random

def random_generator(min_value, max_value):
    return random.uniform(min_value,max_value)

def generation(duration,key_spacing,trans_min,trans_max,rot_min,rot_max,scale_min,scale_max):
    #cmds.undoInfo(openChunk=True, chunkName="TheAnimation")
    
    selection = cmds.ls(selection=True, long=True) or []

    #élimination des erreurs possibles
    if not selection:
        cmds.warning("Nothing Selected")
        return

    if key_spacing <= 0:
        cmds.warning("Add more space between keys")
        return

    if duration <=0:
        cmds.warning("Animation time cannot be 0")
        return

    cmds.undoInfo(state=True)
    cmds.undoInfo(openChunk=True, chunkName="TheAnimation")

    try:

        for h in selection:
            cmds.cutKey(h, clear=True)
        initial_value = {}


        cmds.playbackOptions(minTime=0, maxTime=duration,animationStartTime=0,animationEndTime=duration)

        for i in selection:
            for j in range(0, duration +1, key_spacing):

                if j==0:


                    translation=[random_generator(trans_min[k],trans_max[k]) for k in range(3)]

                    rotation=[random_generator(rot_min[m],rot_max[m]) for m in range(3)]

                    scale=[random_generator(scale_min[n],scale_max[n]) for n in range(3)]

                    initial_value[i] = {"translate":translation,"rotate":rotation,"scale":scale}

                elif j == duration:
                    #si on est a la fin, remet la premiere valeur comme valeur finale.
                    translation=initial_value[i]["translate"]
                    rotation=initial_value[i]["rotate"]
                    scale=initial_value[i]["scale"]
                    
                else:   
                    translation=[random_generator(trans_min[k],trans_max[k]) for k in range(3)]
                    
                    rotation=[random_generator(rot_min[m],rot_max[m]) for m in range(3)]
                    
                    scale=[random_generator(scale_min[n],scale_max[n]) for n in range(3)]

                movement_update={"translate":translation,"rotate":rotation,"scale":scale}

                for o, values in movement_update.items():
                    for axis, value in zip("XYZ", values):
                        cmds.setKeyframe(i,attribute=o+axis,time=j,value=value)
    finally:
        cmds.undoInfo(closeChunk=True)
         


