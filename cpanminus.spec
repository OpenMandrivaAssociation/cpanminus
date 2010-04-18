%define upstream_name    App-cpanminus
%define upstream_version 0.9935

Name:       cpanminus
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Get, unpack, build and install modules from CPAN
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::Install)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP)
BuildRequires: perl(Module::Build)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
cpanminus is a script to get, unpack, build and install modules from CPAN.

Why? It's dependency free, requires zero configuration, and stands alone --
but it's maintainable and extensible with plugins and friendly to shell
scripting. When running, it requires only 10MB of RAM.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_bindir}/cpanm
%{_mandir}/man3/*
%perl_vendorlib/*


