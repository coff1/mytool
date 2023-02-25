# kali添加Java环境，./java_add.sh + jdk文件夹
mv $1 /opt/$1
update-alternatives --install /usr/bin/java java /opt/$1/bin/java 300
update-alternatives --set java /opt/$1/bin/java
update-alternatives --install /usr/bin/javac javac /opt/$1/bin/javac 300
update-alternatives --set javac /opt/$1/bin/javac
update-alternatives --config java
