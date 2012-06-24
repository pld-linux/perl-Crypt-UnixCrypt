#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	UnixCrypt
Summary:	Crypt::UnixCrypt - Perl-only implementation of the "crypt" function
Summary(pl):	Crypt::UnixCrypt - czysto perlowa implementacja funkcji "crypt"
Name:		perl-Crypt-UnixCrypt
Version:	1.0
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff007b7fdda2aa626acaca216750c422
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::UnixCrypt module is for all those poor souls whose perl port
answers to the use of "crypt()" with the message `The crypt() function
is unimplemented due to excessive paranoia.'.

%description -l pl
Modu� Crypt::UnixCrypt jest przeznaczony dla tych biednych dusz,
kt�rym u�ywana implementacja Perla na pr�b� u�ycia "crypt()" odpowiada
komunikatem: `The crypt() function is unimplemented due to excessive
paranoia.' [Funkcja crypt() nie zosta�a zaimplementowana z powodu
nadmiernej paranoi.]

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Crypt/UnixCrypt.pm
%{_mandir}/man3/*
