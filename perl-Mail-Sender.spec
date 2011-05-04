%define	module	Mail-Sender
%define	name	perl-%{module}
%define version 0.8.16
%define release %mkrel 3

%define	_requires_exceptions perl(Win32API::Registry)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Module for sending mails with attachments through an SMTP server 
License:	GPL
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/J/JE/JENDA/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Mail-Sender is a Perl module for sending mail with attachments through an
SMTP server.  This module will not work with qmail servers, however.


%prep
%setup -q -n %{module}-%{version}

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


