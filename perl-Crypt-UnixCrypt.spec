%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	UnixCrypt
Summary:	Crypt::UnixCrypt perl module
Summary(pl):	Modu� perla Crypt::UnixCrypt
Name:		perl-Crypt-UnixCrypt
Version:	1.0
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff007b7fdda2aa626acaca216750c422
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::UnixCrypt - perl-only implementation of the crypt(3) function.

%description -l pl
Crypt::UnixCrypt - implementacja funkcji crypt(3) wy��cznie w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Crypt/UnixCrypt.pm
%{_mandir}/man3/*
