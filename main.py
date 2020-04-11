from mongoengine import *
from courses import saveCoursesAndStudents
from subunitys import saveSubunitysAndTeachers
from monographys import saveMonographys

import os

connect(db="openufma", alias="openufma", host=os.getenv("MONGODB_ATLAS_URI"))

saveCoursesAndStudents()
saveSubunitysAndTeachers()
saveMonographys()





