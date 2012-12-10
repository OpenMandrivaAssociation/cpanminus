%define upstream_name    App-cpanminus
%define upstream_version 1.5018

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(App::cpanminus::script\\)'
%endif

Name:       cpanminus
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Get, unpack, build and install modules from CPAN
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::Install)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP)
BuildRequires: perl(Module::Build)
BuildRequires: perl-devel

BuildArch: noarch

%description
cpanminus is a script to get, unpack, build and install modules from CPAN.

Why? It's dependency free, requires zero configuration, and stands alone --
but it's maintainable and extensible with plugins and friendly to shell
scripting. When running, it requires only 10MB of RAM.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_bindir}/cpanm
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.1.200-2mdv2011.0
+ Revision: 653549
- rebuild for updated spec-helper

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.200-1mdv2011.0
+ Revision: 575586
- update to 1.0012

* Mon Aug 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 570315
- update to 1.0010

* Thu Apr 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.993.600-1mdv2010.1
+ Revision: 537881
- update to 0.9936

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.993.500-1mdv2010.1
+ Revision: 536128
- update to 0.9935

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.993.200-1mdv2010.1
+ Revision: 532256
- import cpanminus


* Tue Apr 06 2010 cpan2dist 0.9932-1mdv
- initial mdv release, generated with cpan2dist
