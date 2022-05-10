%global pypi_name pytest-repeat
%global _empty_manifest_terminate_build 0

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        2
Summary:        pytest plugin for repeating tests

License:        MPL-2.0
URL:            https://github.com/pytest-dev/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/1e/69/f7411070a07bc8949725b57d9298ac445e59edb26e3b74b4f97d52afe47a/%{pypi_name}-0.9.1.tar.gz
BuildArch:      noarch

Requires:       python3-pytest

%description
pytest-repeat is a plugin for py.test that makes it easy to repeat a single
test, or multiple tests, a specific number of times.


%package -n python3-%{pypi_name}
Summary:        pytest plugin for repeating tests
Provides:       python-%{pypi_name}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
%description -n python3-%{pypi_name}
pytest-repeat is a plugin for py.test that makes it easy to repeat a single
test, or multiple tests, a specific number of times.


%prep
%autosetup -n %{pypi_name}-0.9.1


%build
%py3_build


%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
        find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
        find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
        find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
        find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
        find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .


%files -n python3-%{pypi_name} -f filelist.lst
%doc CHANGES.rst README.rst
%license LICENSE
%dir %{python3_sitelib}/*


%changelog
* Wed May 18 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.9.1-2
- add necessary BuildRequires

* Wed Jul 14 2021 ice-kylin <wminid@yeah.net> - 0.9.1-1
- Initial package
