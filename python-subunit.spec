%global __requires_exclude testtools

%define srcname python-subunit
%define module  subunit

Name:           python-%{module}
Version:        1.4.6
Release:        1
Summary:        Python implementation of subunit test streaming protocol
Group:          Development/Python
License:        ASL2.0 or BSD
URL:            https://launchpad.net/testrepository
# Also https://pypi.org/project/python-subunit/
Source0:        https://pypi.io/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
# setuptools reads subunit.version_string while generating metadata
Patch0:         python-subunit-1.4.6-version-literal.patch
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(extras)
BuildRequires:  python%{pyver}dist(iso8601)
# testtools is in the extra repository. A main package cannot require it.
Recommends:     python%{pyver}dist(testtools)

%description
Subunit is a streaming protocol for test results.

%prep
%autosetup -p1 -n python_subunit-1.4.6

# Remove bundled egg-info
rm -rf python_%{module}.egg-info

%build
%py_build

%install
%py_install

%files
# 1.4.6 adds gojson2subunit and junitxml2subunit, which do not match subunit*
%{_bindir}/*subunit*
%{python_sitelib}/*
