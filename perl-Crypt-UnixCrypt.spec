%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	UnixCrypt
Summary:	Crypt::UnixCrypt perl module
Summary(pl):	Modu³ perla Crypt::UnixCrypt
Name:		perl-Crypt-UnixCrypt
Version:	1.0
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::UnixCrypt - perl-only implementation of the crypt(3) function.

%description -l pl
Crypt::UnixCrypt - implementacja funkcji crypt(3) wy³±cznie w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_sitelib}/Crypt/UnixCrypt.pm
%{_mandir}/man3/*
