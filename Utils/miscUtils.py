import os
import sys

## Function: Return the path of supplied file
#
#  @param pgm The file or program name (ex. "sound.mp3")
#  @return The path (if any) to the supplied program
#
def which(pgm):

    # Check system path first
    path = sys.path
    for p in path:
        p=os.path.join(p,pgm)
        if os.path.exists(p) and os.access(p,os.X_OK):
            return p        

    # Check OS path next
    path=os.getenv('PATH')
    for p in path.split(os.path.pathsep):
        p=os.path.join(p,pgm)
        if os.path.exists(p) and os.access(p,os.X_OK):
            return p
