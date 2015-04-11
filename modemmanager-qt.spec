%define fw_version 5.9

Summary:	KDE Frameworks 5 Qt wrapper for ModemManager API
Name:		modemmanager-qt
Version:	5.9.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/frameworks/%{fw_version}/%{name}-%{version}.tar.xz
BuildRequires:	extra-cmake-modules
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(ModemManager)

%description
KDE Frameworks 5 Qt wrapper for ModemManager API.

#----------------------------------------------------------------------------

%define kf5modemmanagerqt_major 6
%define libkf5modemmanagerqt %mklibname kf5modemmanagerqt %{kf5modemmanagerqt_major}

%package -n %{libkf5modemmanagerqt}
Summary:	KDE Frameworks 5 Qt wrapper for ModemManager API shared library
Group:		System/Libraries

%description -n %{libkf5modemmanagerqt}
KDE Frameworks 5 Qt wrapper for ModemManager API shared library.

%files -n %{libkf5modemmanagerqt}
%{_kde5_libdir}/libKF5ModemManagerQt.so.%{kf5modemmanagerqt_major}
%{_kde5_libdir}/libKF5ModemManagerQt.so.%{version}

#----------------------------------------------------------------------------

%define devkf5modemmanagerqt %mklibname kf5modemmanagerqt -d

%package -n %{devkf5modemmanagerqt}
Summary:	Development files for KDE Frameworks 5 Qt wrapper for ModemManager API
Group:		Development/KDE and Qt
Requires:	%{libkf5modemmanagerqt} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	kf5modemmanagerqt-devel = %{version}

%description -n %{devkf5modemmanagerqt}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkf5modemmanagerqt}
%{_kde5_includedir}/KF5/ModemManagerQt
%{_kde5_includedir}/KF5/modemmanagerqt_version.h
%{_kde5_libdir}/cmake/KF5ModemManagerQt
%{_kde5_libdir}/libKF5ModemManagerQt.so
%{_kde5_mkspecsdir}/*.pri

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build
