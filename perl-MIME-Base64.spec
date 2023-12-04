#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-MIME-Base64
Version  : 3.16
Release  : 37
URL      : https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/MIME-Base64-3.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/MIME-Base64-3.16.tar.gz
Summary  : 'Encoding and decoding of base64 strings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MIME-Base64-license = %{version}-%{release}
Requires: perl-MIME-Base64-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
MIME::Base64 - Encoding and decoding of base64 strings
SYNOPSIS
use MIME::Base64;

%package license
Summary: license components for the perl-MIME-Base64 package.
Group: Default

%description license
license components for the perl-MIME-Base64 package.


%package perl
Summary: perl components for the perl-MIME-Base64 package.
Group: Default
Requires: perl-MIME-Base64 = %{version}-%{release}

%description perl
perl components for the perl-MIME-Base64 package.


%prep
%setup -q -n MIME-Base64-3.16
cd %{_builddir}/MIME-Base64-3.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MIME-Base64
cp %{_builddir}/MIME-Base64-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-MIME-Base64/1c9f348d290d4fd3ac8b5b09c29275b47b20f4e4 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
## Remove excluded files
rm -f %{buildroot}*/usr/share/man/man3/MIME::QuotedPrint.3
rm -f %{buildroot}*/usr/share/man/man3/MIME::Base64.3

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MIME-Base64/1c9f348d290d4fd3ac8b5b09c29275b47b20f4e4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
