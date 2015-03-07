Summary:    MySQL database connector for C++
Name:       mysql-connector-c++
Version:    1.1.5
Release:    1%{?dist}
Group:      System Environment/Libraries
License:    GPLv2 with exceptions

URL:        http://dev.mysql.com/downloads/connector/cpp/

# Upstream has a mirror redirector for downloads, so the URL is hard to
# represent statically.  You can get the tarball by following a link from
# http://dev.mysql.com/downloads/connector/cpp
Source0:    %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: cmake mysql-devel boost-devel


%description
MySQL Connector/C++ is a MySQL database connector for C++. 

The MySQL Driver for C++ mimics the JDBC 4.0 API. 
However, Connector/C++ does not implement all of the JDBC 4.0 API.

The Connector/C++ preview features the following classes:
* Connection
* DatabaseMetaData
* Driver
* PreparedStatement
* ResultSet
* ResultSetMetaData
* Savepoint
* Statement 


%package devel
Summary:   MySQL Connector/C++ developer files (headers, examples, etc.)
Group:     Development/Libraries
Requires:  mysql-connector-c++ = %{version}-%{release}
Requires:  mysql-devel

%description devel
These are the files needed to compile programs using MySQL Connector/C++.


%prep
%setup -q

sed -i -e 's/MYSQL_VERSION_ID >= 50703/0/' driver/nativeapi/libmysql_static_proxy.cpp

# Workaround for http://bugs.mysql.com/bug.php?id=68320
sed -i -e 's/lib$/%{_lib}/' driver/CMakeLists.txt
chmod -x examples/*.cpp examples/*.txt

# Save examples to keep directory clean (for doc)
mkdir _doc_examples
cp -pr examples _doc_examples


%build
%{cmake} -DMYSQLCPPCONN_BUILD_EXAMPLES:BOOL=0

make


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}


%check
# for documentation purpose only (A MySQL server is required)
# cd test
# ./static_test tcp://127.0.0.1 user password test_database
# Should output : Loops= 2 Tests=  798 Failures=   0
# ./driver_test tcp://127.0.0.1 user password test_database
# Should output :  Loops= 2 Tests=  592 Failures=   0


%clean
rm -rf %{buildroot} 


%post -p /sbin/ldconfig 

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ANNOUNCEMEN* COPYING README CHANGES Licenses_for_Third-Party_Components.txt
%{_libdir}/libmysqlcppconn.so.7*
%exclude %{_libdir}/libmysqlcppconn-static.a
%exclude %{_prefix}/ANNOUNCEMENT
%exclude %{_prefix}/COPYING
%exclude %{_prefix}/INSTALL
%exclude %{_prefix}/Licenses_for_Third-Party_Components.txt
%exclude %{_prefix}/README

%files devel
%defattr(-,root,root,-)
%doc _doc_examples/examples
%{_libdir}/libmysqlcppconn.so
%{_includedir}/mysql*
%{_includedir}/cppconn


%changelog
* Sat Feb  9 2013 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- version 1.1.2 (GA)

* Wed Aug  8 2012 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- version 1.1.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.9.bzr895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.8.bzr895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Remi Collet <Fedora@famillecollet.com> 1.1.0-0.7.bzr895
- rebuild for new MySQL client library

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.6.bzr895
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Remi Collet <Fedora@famillecollet.com> 1.1.0-0.5.bzr895
- rebuilt for MySQL 5.5.8

* Wed Sep 29 2010 jkeating - 1.1.0-0.4.bzr895
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Remi Collet <Fedora@famillecollet.com> 1.1.0-0.3.bzr895
- update to 1.1.0 from bzr snapshot 895 (for Workbench 5.2.28)

* Mon Aug 09 2010 Remi Collet <Fedora@famillecollet.com> 1.1.0-0.2.bzr888
- Changes from review (#622272)

* Sun Aug 08 2010 Remi Collet <Fedora@famillecollet.com> 1.1.0-0.1.bzr888
- update to 1.1.0 from bzr snapshot 888 (for Workbench 5.2.26)
- initial package for fedora review

* Fri Jun 04 2010 Remi Collet <RPMS@famillecollet.com> 1.1.0-0.1.bzr819
- update to 1.1.0 from bzr snapshot 819

* Sat Apr 03 2010 Remi Collet <RPMS@famillecollet.com> 1.1.0-0.1.bzr818
- update to 1.1.0 from bzr snapshot 818

* Sat Apr 03 2010 Remi Collet <RPMS@famillecollet.com> 1.0.6-0.1.bzr814
- update to 1.0.6 from bzr snapshot 814

* Sat Jan 23 2010 Remi Collet <RPMS@famillecollet.com> 1.0.6-0.1.bzr813
- update to 1.0.6 from bzr snapshot 813

* Sun Jan 10 2010 Remi Collet <RPMS@famillecollet.com> 1.0.6-0.1.bzr812
- update to 1.0.6 from bzr snapshot

* Tue Nov 24 2009 Remi Collet <RPMS@famillecollet.com> 1.0.5-1.1
- rebuild

* Sun Jun 28 2009 Remi Collet <RPMS@famillecollet.com> 1.0.5-1
- initial RPM

