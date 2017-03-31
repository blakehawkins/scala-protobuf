#! /usr/bin/env python
# Use the python from environment - ensure venv is activated first!

if __name__ == "__main__":
    import os, sys

    import subprocess

    java_class_name = 'com.jeffplaisance.protobuf.compiler.ScalaProtoWrapperGenerator'

    SCRIPT     = subprocess.check_output(['readlink', '-f', sys.argv[0]]).decode('utf-8').strip()
    SCRIPTPATH = subprocess.check_output(['dirname', SCRIPT]).decode('utf-8').strip()

    SCALA_HOME = os.environ['SCALA_HOME']
    CLASSPATH  = os.path.join(SCALA_HOME, 'lib', 'scala-library.jar')

    walk_path = os.path.join(SCRIPTPATH, "..")
    saved_paths = []
    for dirpath, _, fileList in os.walk(walk_path):
        for fname in fileList:
            check_path = os.path.join(dirpath, fname)
            if fname[-4:] == ".jar":
                saved_paths.append(check_path)
                CLASSPATH = "{}:{}".format(CLASSPATH, check_path)

    with open('scala-protobuf-wrapper.log', 'w') as log:
        log.write("saved_paths = {}\n".format(saved_paths))
        log.write("walk_path   = {}\n".format(walk_path))
        log.write("SCRIPT      = {}\n".format(SCRIPT))
        log.write("SCRIPTPATH  = {}\n".format(SCRIPTPATH))
        log.write("SCALA_HOME  = {}\n".format(SCALA_HOME))
        log.write("CLASSPATH   = {}\n".format(CLASSPATH))
        log.write("java_class_name = {}\n".format(java_class_name))

    subprocess.call(['java', '-Xmx512M', '-cp', CLASSPATH, java_class_name])

