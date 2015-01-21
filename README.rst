Feel free the use the pre-build RPMS from the RPMS directory.

How to build:

 * Download mysql-workbench-community-6.2.4-1.fc20.src.rpm from http://dev.mysql.com/downloads/workbench/ by choosing Source Code

 * rpm -i mysql-workbench-community-6.2.4-1.fc20.src.rpm

 * Download mysql-connector-c++-1.1.5.tar.gz from http://dev.mysql.com/downloads/connector/cpp/ by choosing Source Code to ~/rpmbuild/SOURCES

 * Download antlr-3.4-complete.jar from http://www.antlr3.org/download/ to ~/rpmbuild/SOURCES

 * copy mysql-connector-c++.spec from this repository to ~/rpmbuild/SPECS

 * rpmbuild -bs ~/rpmbuild/SPECS/mysql-connector-c++.spec

 * mock mysql-connector-c++-1.1.5-1.fc21.src.rpm

 * cp /var/lib/mock/fedora-21-x86_64/result/\*.rpm .

 * mock --clean

 * copy mysql-workbench.spec from this repository to ~/rpmbuild/SPEC

 * rpmbuild -bs ~/rpmbuild/SPECS/mysql-workbench.spec --define 'release 1'

 * mock -r fedora-21-x86_64 --install mysql-connector-c++-1.1.5-1.fc21.x86_64.rpm mysql-connector-c++-devel-1.1.5-1.fc21.x86_64.rpm

 * mock -r fedora-21-x86_64 --no-clean ~/rpmbuild/SRPMS/mysql-workbench-community-6.2.4-1.fc21.src.rpm --define 'release 1'

 * Now you should have a RPM in /var/lib/mock/fedora-21-x86_64/result/
