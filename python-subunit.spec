%global __requires_exclude testtools

%define srcname python-subunit
%define module  subunit

Name:           python-%{module}
Version:        1.4.0
Release:        2
Summary:        Python implementation of subunit test streaming protocol
Group:          Development/Python
License:        ASL2.0 or BSD
URL:            https://launchpad.net/testrepository
Source0:        https://pypi.io/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python-extras
%{?python_provide:%python_provide python3-%{module}}

%description
Subunit is a streaming protocol for test results.

%prep
%setup -q -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf python_%{module}.egg-info

%build
%py_build

%install
%py_install

%files
%{_bindir}/%{module}*
%{_bindir}/tap2%{module}
%{python_sitelib}/*
