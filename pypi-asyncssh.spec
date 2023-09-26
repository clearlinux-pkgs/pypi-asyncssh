#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-asyncssh
Version  : 2.13.2
Release  : 14
URL      : https://files.pythonhosted.org/packages/9a/01/3ec7ff6eafc0512a927ca2e047f0abd1636602b73ede09d4a7f41063db99/asyncssh-2.13.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9a/01/3ec7ff6eafc0512a927ca2e047f0abd1636602b73ede09d4a7f41063db99/asyncssh-2.13.2.tar.gz
Summary  : AsyncSSH: Asynchronous SSHv2 client and server library
Group    : Development/Tools
License  : EPL-2.0
Requires: pypi-asyncssh-license = %{version}-%{release}
Requires: pypi-asyncssh-python = %{version}-%{release}
Requires: pypi-asyncssh-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cryptography)
BuildRequires : pypi(typing_extensions)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://readthedocs.org/projects/asyncssh/badge/?version=latest
:target: https://asyncssh.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status

%package license
Summary: license components for the pypi-asyncssh package.
Group: Default

%description license
license components for the pypi-asyncssh package.


%package python
Summary: python components for the pypi-asyncssh package.
Group: Default
Requires: pypi-asyncssh-python3 = %{version}-%{release}

%description python
python components for the pypi-asyncssh package.


%package python3
Summary: python3 components for the pypi-asyncssh package.
Group: Default
Requires: python3-core
Provides: pypi(asyncssh)
Requires: pypi(cryptography)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-asyncssh package.


%prep
%setup -q -n asyncssh-2.13.2
cd %{_builddir}/asyncssh-2.13.2
pushd ..
cp -a asyncssh-2.13.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695772307
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-asyncssh
cp %{_builddir}/asyncssh-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-asyncssh/b086d72d0fe9af38418dab524fe76eea3cb1eec3 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-asyncssh/b086d72d0fe9af38418dab524fe76eea3cb1eec3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
