Name:           yum-stub
Summary:        Overrides depsolving for yum and dnf
Version:        9999
Release:        1%{?dist}
License:        LGPLv2+
URL:            https://github.com/cgwalters/yum-stub
Source0:        yum-stub-%{version}.tar.xz
BuildArch:      noarch

Provides: yum
Provides: dnf

%description
%{summary}

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/yum
%{_bindir}/dnf
