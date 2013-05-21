%define	module	Mail-Sender

Name:		perl-%module
Version:	0.8.16
Release:	7
Summary:	Module for sending mails with attachments through an SMTP server 
License:	GPL
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/J/JE/JENDA/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
Buildarch:	noarch

%description
Mail-Sender is a Perl module for sending mail with attachments through an
SMTP server.  This module will not work with qmail servers, however.


%prep
%setup -q -n %{module}-%{version}
rm -f Sender/CType/Win32.pm
sed -i -e '/Win32.pm/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
echo "N
" | %make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%{perl_vendorlib}/Mail
%{_mandir}/*/*




%changelog
* Fri Jul 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.8.16-6
+ Revision: 810445
- Adjust buildrequirements
- Don't package Win32 specific files

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.8.16-5
+ Revision: 765432
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.8.16-4
+ Revision: 763947
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.16-3
+ Revision: 667254
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.16-2mdv2011.0
+ Revision: 426523
- rebuild

* Tue Jul 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.16-1mdv2009.0
+ Revision: 235776
- update to new version 0.8.16

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.8.13-4mdv2009.0
+ Revision: 223810
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.13-3mdv2008.1
+ Revision: 180469
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.8.13-2mdv2008.0
+ Revision: 23365
- make build non interactive

