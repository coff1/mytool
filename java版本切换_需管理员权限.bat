@echo off

echo java_version:
java -version 
echo. 
echo ============================================= 
echo jdk version select:
echo 0:jdk-17.0.4
echo 1:jdk-18.0.2.1
echo 2:jre1.8.0_192
echo 3:jre1.8.0_333
echo ============================================= 

set /p opt=input the number:
if %opt%==0 (
    set TARGET_JAVA_HOME="C:\Program Files\Java\jdk-17.0.4"
)
if %opt%==1 (
    set TARGET_JAVA_HOME="C:\Program Files\Java\jdk-18.0.2.1"
)
if %opt%==2 (
    set TARGET_JAVA_HOME="C:\Program Files\Java\jre1.8.0_192"
)
if %opt%==3 (
    set TARGET_JAVA_HOME="C:\Program Files\Java\jre1.8.0_333"
)

echo target version:%TARGET_JAVA_HOME%

setx -m JAVA_HOME %TARGET_JAVA_HOME%

pause