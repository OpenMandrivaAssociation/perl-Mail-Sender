%define	module	Mail-Sender

Summary:	Module for sending mails with attachments through an SMTP server 
Name:		perl-%{module}
Version:	0.903
Release:	3
License:	GPLv2
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CA/CAPOEIRAB/Mail-Sender-%{version}.tar.gz
Url:		https://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
Mail-Sender is a Perl module for sending mail with attachments through an
SMTP server.  This module will not work with qmail servers, however.


%prep
%setup -qn %{module}-%{version}
rm -f lib/Mail/Sender/CType/Win32.pm
sed -i -e '/Win32.pm/d' MANIFEST

%build
%__perl Makefile.PL INSTALLDIRS=vendor
echo "N
" | make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Mail
%{_mandir}/man3/*
