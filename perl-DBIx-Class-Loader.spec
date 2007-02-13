#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Class-Loader
Summary:	DBIx::Class::Loader - Dynamic definition of DBIx::Class subclasses
Summary(pl.UTF-8):	DBIx::Class::Loader - dynamiczne definiowanie podklas DBIx::Class
Name:		perl-DBIx-Class-Loader
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SR/SRI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f7c20cdb7fb6f3594e5ac8de72560594
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBIx-Class >= 0.03001
BuildRequires:	perl-Lingua-EN-Inflect
BuildRequires:	perl-Text-Balanced
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Class::Loader automates the definition of DBIx::Class
subclasses. It scans table schemas and setup columns and primary key
information.

%description -l pl.UTF-8
DBIx::Class::Loader automatyzuje definiowanie podklas DBIx::Class.
Skanuje schematy tabel i ustawia informacje o kolumnach oraz kluczu
głównym.

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
%doc Changes
%{perl_vendorlib}/DBIx/Class/*.pm
%{perl_vendorlib}/DBIx/Class/Loader
%{_mandir}/man3/*
