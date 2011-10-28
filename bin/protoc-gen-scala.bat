@echo off
set CLASSPATH=%SCALA_HOME%\lib\scala-library.jar
set SCRIPTPATH=%~dp0
for %%i in (%SCRIPTPATH%..\lib\*.jar) do set CLASSPATH=%CLASSPATH%;%%i
for %%i in (%SCRIPTPATH%..\target\scala-2.9.1\*.jar) do set CLASSPATH=%CLASSPATH%;%%i
java -Xmx512M -cp %CLASSPATH% com.jeffplaisance.protobuf.compiler.ScalaProtoWrapperGenerator
