#! /usr/bin/env python
# Use the python from environment - ensure venv is activated first!

if __name__ == "__main__":
    import os, sys

    import subprocess

    java_class_name = 'com.jeffplaisance.protobuf.compiler.ScalaProtoWrapperGenerator'

    SCRIPT     = subprocess.check_output(['readlink', '-f', sys.argv[0]])
    SCRIPTPATH = subprocess.check_output(['dirname', SCRIPT])

    SCALA_HOME = os.environ['SCALA_HOME']
    CLASSPATH  = os.path.join(SCALA_HOME, 'lib', 'scala-library.jar')

    for _, _, fileList in os.walk(os.path.join(SCRIPTPATH, b"..")):
        for fname in fileList:
            if fname[-4:] == ".jar":
                CLASSPATH = CLASSPATH + fname

    with open('scala-protobuf-wrapper.log', 'w') as log:
        log.write("{}\n".format(CLASSPATH))
        log.write("{}\n".format(java_class_name))

    subprocess.call(['java', '-Xmx512M', '-cp', CLASSPATH, java_class_name])

