# $Id: smeserver-phpsysinfo.spec,v 1.1 2013/03/03 21:49:49 unnilennium Exp $
# Authority: darrellmay
# Name: Darrell May

Summary: phpSysInfo for SME Server
%define name smeserver-phpsysinfo
Name: %{name}
%define version 3.1.13
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: SME/addon
Source: %{name}-%{version}.tar.gz
URL: http://phpsysinfo.sourceforge.net
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: smeserver-release => 9.0
BuildRequires: e-smith-devtools 
AutoReqProv: no

%description
%name is an implementation of phpSysInfo on SME Server.
Access with admin login credentials via https://yourdomain/phpsysinfo

%changelog
* Sat Jun 21 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 3.1.13-1.sme
- Initial release to sme9
- upgrade of phpsysinfo to 3.1.13 https://github.com/phpsysinfo/phpsysinfo/releases/tag/v3.1.13

* Mon Apr 21 2008 Shad L. Lords <slords@mail.com>
- Prep for import into buildsys
- Clean up spec

* Fri Oct 19 2007  Darrell May <dmay@myezserver.com>
- accounts and configuration db phpsysinfo defaults added
- default access restricted to private (private|public)
- phpsysinfo-2.5.4
- [2.5.4-0dmay]
* Mon Apr 09 2007  Darrell May <dmay@myezserver.com>
- [2.5.3-1dmay]
* Sun Apr 01 2007  Darrell May <dmay@myezserver.com>
- phpsysinfo-2.5.3
- [2.5.3-0dmay]
* Tue Jan 02 2007  Darrell May <dmay@myezserver.com>
- phpsysinfo-2.5.2
- [2.5.2-0]
* Fri Aug 04 2006  Darrell May <dmay@myezserver.com>
- phpsysinfo-2.5.2-rc3
- [2.5.2-rc3]
* Wed Dec 14 2005 Darrell May <dmay@myezserver.com>
- phpsysinfo-2.5
- [2.5-0]
* Fri Apr 22 2005 Darrell May <dmay@myezserver.com>
- added support for SME Server 7.x
- [2.3-2]
* Mon Nov 15 2004 Darrell May <dmay@myezserver.com>
- updated to release 2.3
- renamed smeserver-phpsysinfo
- updated includes/os/class.Linux.inc.php to recognize SME Server
- [2.3-1]
* Sat Jun 29 2002 Darrell May <dmay@netsourced.com>
- updated to release 2.1
- [2.1-1]
* Sun Mar 10 2002 Darrell May <dmay@netsourced.com>
- updated to release 2.0
- [2.0-1]
* Sun Mar 10 2002 Darrell May <dmay@netsourced.com>
- changed rights/ownership to tighten security
- [1.9-2]
* Tue Mar 05 2002 Darrell May <dmay@netsourced.com>
- changed %post/postun to graceful
- [1.9-1]
* Mon Jan 21 2002 Darrell May <dmay@netsourced.com>
- updated to version 1.9
- [1.9-0]
* Wed Oct 31 2001 Darrell May <dmay@netsourced.com>
- updated to version 1.8
- [1.8-0]
* Sun Sep 23 2001 Darrell May <dmay@netsourced.com>
- name change
* Thu May 30 2001 Darrell May <dmay@netsourced.com>
- 2.1.0-1
- Original version

%prep
%setup

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%clean
/bin/rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre 
/bin/cp /opt/phpsysinfo/phpsysinfo.ini /opt/phpsysinfo/phpsysinfo.ini-$(date +"%H:%M-%b-%d-%Y")

%post
if ! [[ -f /opt/phpsysinfo/phpsysinfo.ini ]]; then
     cp /opt/phpsysinfo/phpsysinfo.ini.new /opt/phpsysinfo/phpsysinfo.ini
fi
