%define		_class		Console
%define		_subclass	Table
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.5
Release:	2
Summary:	Makes it easy to build console style tables
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Console_Table/
Source0:	http://download.pear.php.net/package/Console_Table-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Provides methods such as addRow(), insertRow(), addCol() etc to build
Console tables. Can be with or without headers, and has various
configurable options.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2mdv2011.0
+ Revision: 667489
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.4-1mdv2011.0
+ Revision: 594484
- update to new version 1.1.4

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.3-4mdv2010.1
+ Revision: 478294
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1.3-3mdv2010.0
+ Revision: 426606
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2mdv2009.1
+ Revision: 321803
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.3-1mdv2009.1
+ Revision: 305782
- update to new version 1.1.3

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1mdv2009.0
+ Revision: 272582
- 1.1.2

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.7-3mdv2009.0
+ Revision: 224690
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2mdv2008.1
+ Revision: 178503
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-1mdv2008.0
+ Revision: 28875
- 1.0.7

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-1mdv2008.0
+ Revision: 15643
- 1.0.6


* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2007.0
+ Revision: 83320
- rebuild

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdv2007.0
+ Revision: 81412
- Import php-pear-Console_Table

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdk
- 1.0.4

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdk
- 1.0.2

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- initial Mandriva package (PLD import)


