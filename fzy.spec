%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%define git_sha 1e19357b933c918d59777a2ac8f20e9788b02cc5

Name:       fzy
Version:    0.9
Release:    1%{?dist}

Summary:    A better fuzzy finder.
Group:      Utilities/Misc
License:    MIT
URL:        https://github.com/jhawthorn/fzy
Packager:   Frankie Dintino <fdintino@theatlantic.com>

Source0:    https://github.com/jhawthorn/%{name}/archive/%{git_sha}.tar.gz#/%{name}-%{git_sha}.tar.gz

BuildRequires:   gcc

%description
A better fuzzy finder.

%prep
%setup -q -n %{name}-%{git_sha}

%build
make %{?_smp_mflags}

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} BINDIR=%{_bindir} MANDIR=%{_mandir} make install
install -p -d -m 0755 %{buildroot}%{_pkgdocdir}
install -p -m 0644 -t %{buildroot}%{_pkgdocdir} CHANGELOG.md ALGORITHM.md README.md

%files
%{_bindir}/fzy
%{_mandir}/man1/fzy.1*
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/CHANGELOG.md
%doc %{_pkgdocdir}/ALGORITHM.md
%doc %{_pkgdocdir}/README.md
%license LICENSE

%changelog
* Fri Mar 17 2017 Frankie Dintino <fdintino@theatlantic.com>
- first rpm version
