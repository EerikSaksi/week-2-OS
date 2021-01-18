### Peripheral actions

def kbdAction(kbdState):
    kbdIrq=False
    return kbdState

def nicAction(nicState):
    nicIrq=False
    return nicState

def ssdAction(ssdState):
    ssdIrq=False
    return ssdState

def gpuAction(gpuState):
    gpuIrq=False
    return gpuState

def timerAction(timerState):
    timerState[0] += 1 
    timerIrq = False
    if timerState[0] == 2: 
        timerIrq = True
    return (timerState, timerIrq)
