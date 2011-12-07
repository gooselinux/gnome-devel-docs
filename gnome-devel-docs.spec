Summary: GNOME developer documentation
Name: gnome-devel-docs
Version: 2.28.0
Release: 1%{?dist}
License: GFDL
Group: System Environment/Libraries
URL: http://library.gnome.org
Source: http://download.gnome.org/sources/gnome-devel-docs/2.28/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: gnome-doc-utils
BuildRequires: rarian-compat
BuildRequires: docbook-utils
BuildRequires: gettext

%description
This package contains documents which are targeted for GNOME developers.
It contains, e.g., the Human Interface Guidelines, the Integration Guide
and the Platform Overview.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS NEWS COPYING
%{_datadir}/gnome/help/gdp-handbook
%{_datadir}/gnome/help/gdp-style-guide
%{_datadir}/gnome/help/hig-book
%{_datadir}/gnome/help/integration-guide
%{_datadir}/gnome/help/platform-overview
%{_datadir}/omf/gdp-handbook
%{_datadir}/omf/gdp-style-guide
%{_datadir}/omf/hig-book
%{_datadir}/omf/integration-guide
%{_datadir}/omf/platform-overview

%changelog
* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.1-1
- Update to 2.27.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Thu Sep  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Wed Feb 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.1-1
- Update to 2.21.1

* Wed Oct 24 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-2
- Incorporate package review feedback

* Tue Oct 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Initial packaging
