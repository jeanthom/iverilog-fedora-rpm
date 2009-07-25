%define      snapshot 20090423

Name:        iverilog
Version:     0.9.%{snapshot}
Release:     6%{?dist}
Summary:     Icarus Verilog is a verilog compiler and simulator
Group:       Applications/Engineering
License:     GPLv2
URL:         http://www.icarus.com/eda/verilog/index.html
Source0:     ftp://icarus.com/pub/eda/verilog/snapshots/verilog-0.9.1.tar.gz
Patch0:      %{name}-pagesize.patch
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: zlib-devel bzip2-devel bison flex gperf

%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.

%package devel
Summary:     Icarus Verilog devel files
Group:       Development/Libraries
Requires:    %{name} = %{version}-%{release}

%description devel
Icarus Verilog devel files.

%prep
%setup -q -n verilog-0.9.1
%patch0 -p0 -b .pagesize~

# clean junks from tarball
find . -type f -name ".cvsignore" -exec rm '{}' \;
rm -rf `find . -type d -name "autom4te.cache" -exec echo '{}' \;`

%build

CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
%configure

make %{?_smp_mflags}

%install
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
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# contents of QUICK_START.txt can be found also on README.txt, hence omitted
%doc attributes.txt BUGS.txt COPYING extensions.txt glossary.txt ieee1364-notes.txt
%doc README.txt swift.txt netlist.txt t-dll.txt vpi.txt tgt-fpga/fpga.txt
%doc va_math.txt cadpli/cadpli.txt xilinx-hint.txt examples/
%{_bindir}/*
%{_libdir}/ivl
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
# headers for PLI: This is intended to be used by the user.
%{_includedir}/*.h
# RHBZ 480531
%{_libdir}/*.a


%changelog
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
