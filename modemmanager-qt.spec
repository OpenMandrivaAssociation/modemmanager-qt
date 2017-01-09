# (tpg) looks like libmm-qt5 is providing same libraries but with lower major

%define major 6
%define libname %mklibname KF5ModemManagerQt %{major}
%define devname %mklibname KF5ModemManagerQt -d

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Frameworks 5 Qt wrapper for ModemManager API
Name:		modemmanager-qt
Version:	5.30.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(ModemManager)

%description
KDE Frameworks 5 Qt wrapper for ModemManager API.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	KDE Frameworks 5 Qt wrapper for ModemManager API shared library
Group:		System/Libraries

%description -n %{libname}
KDE Frameworks 5 Qt wrapper for ModemManager API shared library.

%files -n %{libname}
%{_libdir}/libKF5ModemManagerQt.so.%{major}
%{_libdir}/libKF5ModemManagerQt.so.%{version}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for KDE Frameworks 5 Qt wrapper for ModemManager API
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(ModemManager)

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KF5/ModemManagerQt
%{_includedir}/KF5/modemmanagerqt_version.h
%{_libdir}/cmake/KF5ModemManagerQt
%{_libdir}/libKF5ModemManagerQt.so
%{_libdir}/qt5/mkspecs/modules/*.pri

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
