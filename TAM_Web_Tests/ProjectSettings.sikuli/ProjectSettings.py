import org.sikuli.basics.SikuliXforJython
from sikuli import *
import datetime

bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
startTime=datetime.datetime.now()
print sys.path
#Settings.MoveMouseDelay=0.2