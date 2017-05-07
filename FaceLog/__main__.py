# file app/__main__.py
import sys
import os

length=len(sys.argv)
if length < 2:
    sys.exit('\nAt least one argument required')
goto = sys.argv[1]
def main():
  if goto=="-c":
    os.system("python savefaces.py "+(' '.join(sys.argv[2:])))
  if goto=="-t":
    os.system("python face_train.py "+(' '.join(sys.argv[2:])))
  if goto=="-r":
    os.system("python recognizefaces.py "+(' '.join(sys.argv[2:])))

if __name__ == '__main__':
  main()