%define srcname python-subunit
%define module  subunit

Name:           python-%{module}
Version:        1.3.0
Release:        %mkrel 5
Summary:        Python implementation of subunit test streaming protocol
Group:          Development/Python
License:        ASL2.0 or BSD
URL:            https://launchpad.net/testrepository
Source0:        https://pypi.io/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
Subunit is a streaming protocol for test results.

%package -n     python3-%{module}
Summary:        Python 3 implementation of subunit test streaming protocol
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}
Obsoletes:      python2-%{module} < 1.3.0-4

%description -n python3-%{module}
Subunit is a streaming protocol for test results.

%prep
%setup -q -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf python_%{module}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%{_bindir}/%{module}*
%{_bindir}/tap2%{module}
%{python3_sitelib}/*
