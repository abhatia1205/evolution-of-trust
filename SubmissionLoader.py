from Submissions import *
import glob

classNames = [c[14:-3] for c in glob.glob('./Submissions/*.py') if not '__init__.py' in c]
print(classNames)