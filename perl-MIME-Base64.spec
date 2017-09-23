#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Base64
Version  : 3.15
Release  : 14
URL      : http://www.cpan.org/CPAN/authors/id/G/GA/GAAS/MIME-Base64-3.15.tar.gz
Source0  : http://www.cpan.org/CPAN/authors/id/G/GA/GAAS/MIME-Base64-3.15.tar.gz
Summary  : 'The RFC 2045 encodings; base64 and quoted-printable'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-MIME-Base64-lib
Requires: perl-MIME-Base64-doc

%description
This package contains a base64 encoder/decoder and a quoted-printable
encoder/decoder.  These encoding methods are specified in RFC 2045 -
MIME (Multipurpose Internet Mail Extensions).

%package doc
Summary: doc components for the perl-MIME-Base64 package.
Group: Documentation

%description doc
doc components for the perl-MIME-Base64 package.


%package lib
Summary: lib components for the perl-MIME-Base64 package.
Group: Libraries

%description lib
lib components for the perl-MIME-Base64 package.


%prep
%setup -q -n MIME-Base64-3.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/MIME/Base64.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/MIME/QuotedPrint.pm

%files doc
%defattr(-,root,root,-)
%exclude /usr/share/man/man3/MIME::Base64.3
%exclude /usr/share/man/man3/MIME::QuotedPrint.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/MIME/Base64/Base64.so
