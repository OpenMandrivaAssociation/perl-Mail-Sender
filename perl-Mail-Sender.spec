%define	module	Mail-Sender

Name:		perl-%module
Version:	0.8.16
Release:	6
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


