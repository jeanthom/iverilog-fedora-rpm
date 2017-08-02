%global commit 6d0ab9978f036e6029858e0d1b0bdab52e3fbad7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
 
Name:        iverilog
Version:     10
Release:     6%{?dist}
Summary:     Icarus Verilog is a verilog compiler and simulator
 
Group:       Applications/Engineering
License:     GPLv2
URL:         http://iverilog.icarus.com
 
Source0:       http://github.com/steveicarus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
 
BuildRequires: autoconf
BuildRequires: zlib-devel bzip2-devel bison flex gperf gcc-c++ readline-devel
#Provides:      iverilog-devel = %{version}-%{release}
#Obsoletes:     iverilog-devel < 0.9.20100911-1
 
%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.
 
%prep
%setup -q -n %{name}-%{commit}
 
# Clean junks from tarball
find . -type f -name ".git" -exec rm '{}' \;
rm -rf `find . -type d -name "autom4te.cache" -exec echo '{}' \;`
 
 
%build
 
chmod +x autoconf.sh


./autoconf.sh

CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
 
# Add configure to get good results
%configure
 
# Try to build across three CPUs.
make %{?_smp_mflags}
 
%install
 
# Make a clean install
rm -rf %{buildroot}
 
%{__make}    prefix=%{buildroot}%{_prefix} \
             bindir=%{buildroot}%{_bindir} \
             libdir=%{buildroot}%{_libdir} \
             libdir64=%{buildroot}%{_libdir} \
             includedir=%{buildroot}%{_includedir} \
             mandir=%{buildroot}%{_mandir}  \
             vpidir=%{buildroot}%{_libdir}/ivl/ \
             INSTALL="install -p" \
install
 
%check
make check
 
%clean
#rm -rf %{buildroot}
 
%files
%defattr(-,root,root,-)
%doc BUGS.txt COPYING README.txt QUICK_START.txt  
%doc ieee1364-notes.txt mingw.txt swift.txt netlist.txt
%doc t-dll.txt vpi.txt cadpli/cadpli.txt
%doc xilinx-hint.txt examples/
%doc va_math.txt tgt-fpga/fpga.txt extensions.txt glossary.txt attributes.txt
%{_bindir}/*
%{_libdir}/ivl
%{_mandir}/man1/*
# headers for PLI: This is intended to be used by the user.
%{_includedir}/*.h
# RHBZ 480531
%{_libdir}/*.a
 
 
%changelog
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 10-3
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Kiara Navarro <sophiekovalevsky@fedoraproject.org> - 10-1
- Bump to upstream version.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.20120609-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20120609-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20120609-1
- new stable upstream release 0.9.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20111101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20111101-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20111101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20111101-1
- new stable upstream release 0.9.5

* Sat May 28 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20110317-1
- new stable upstream release 0.9.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20100928-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 28 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20100928-1
- new stable upstream release

* Sat Sep 11 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20100911-1
- New sources for upcoming  - 0.9.3 - for testing repos only
- removing useless -devel subpackage

* Wed Dec 30 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091230-1
- New stable snapshot - 0.9.2

* Sat Dec 12 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091212-1
- New development snapshot - 0.9.2 final prerelease snapshot

* Sat Dec 05 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091205-1
- New development snapshot - 0.9.2 prerelease snapshot

* Fri Dec 04 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091204-1
- New development snapshot - 0.9.2 prerelease snapshot

* Sat Nov 28 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20091130-1
- New development snapshot

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20090423-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 13 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20090423-5
- Improved VPI support

* Mon Mar 23 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.9.20081118-4
- new development release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.20081118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 07 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20081118-1
- new snapshot release upstream.

* Fri Sep 12 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20080905-1
- new snapshot release upstream.

* Mon May 26 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20080429-1
- new snapshot release upstream.

* Fri Mar 28 2008 Balint Cristian <rezso@rdsor.ro> 0.9.20080314-1
- new snapshot release upstream.
- add check section for some tests

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.20070608-2
- Autorebuild for GCC 4.3

* Sun Jun 10 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070608-1
- new snapshot release upstream.

* Mon Apr 23 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070421-1
- new snapshot release upstream.

* Thu Feb 27 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070227-1
- new snapshot release.

* Thu Feb 27 2007 Balint Cristian <cbalint@redhat.com> 0.9.20070123-5
- clean junks from tarball
- exlude static library
- smp build seems fine
- use snapshot instead of cvsver macro
- follow package n-v-r from fedora standard

* Thu Feb 23 2007 Balint Cristian <cbalint@redhat.com> 20070123-4
- use cvsver macro
- move examples in main.
- more spec cleanup

* Thu Feb 23 2007 Balint Cristian <cbalint@redhat.com> 20070123-3
- buildroot coherency in spec

* Thu Feb 22 2007 Balint Cristian <cbalint@redhat.com> 20070123-2
- first build for fedora-extras
- request gnu/stubs-32.h to force working gcc in 32 bit enviroment
- fix PAGE_SIZE wich is missing on some arch
- dont use libdir macro, all library always will be 32 bit

* Thu Feb 22 2007 Balint Cristian <cbalint@redhat.com> 20070123-1
- initial release