%define major 6
%define libname %{mklibname sonicdecorations3}
%define devname %{mklibname sonicdecorations3 -d}
#define oldlibname %{mklibname kdecorations2_6}
#define olddevname %{mklibname kdecorations2_6 -d}
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Library for handling window decorations
Name:		sonic-decoration
Version:	6.6.5
Release:	%{?git:0.%{git}.}1
License:	LGPL
Group:		System/Libraries
Url:		https://github.com/Sonic-DE/sonic-decoration
# %if 0%{?git:1}
# Source0:	https://invent.kde.org/plasma/kdecoration/-/archive/%{gitbranch}/kdecoration-%{gitbranchd}.tar.bz2#/kdecoration-%{git}.tar.bz2
# %else
Source0:	%url/archive/%version/%name-%version.tar.gz
# %endif
BuildRequires:	cmake(Qt6)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(KF6I18n)

# pending rename
# BuildRequires:	cmake(KF6CoreAddons)
BuildRequires: %{_lib}SonicFrameworksCoreAddons-devel

BuildRequires:	cmake(ECM)

Conflicts:    kdecoration

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
%summary

%package -n %{libname}

Summary:	SonicDE Decorations Library
Group:	System/Libraries
Conflicts: %{_lib}kdecorations3

%description -n %{libname}
%summary

%install -a
rm -rf %{buildroot}/%{_libdir}/cmake

%files -n %{libname} -f %{name}.lang
%{_libdir}/libkdecorations3.so.*
%{_libdir}/libkdecorations3private.so.*

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/SonicDE and Qt
Requires:	%{libname} = %{EVRD}
Conflicts: %{_lib}kdecorations3-devel

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KF6/kdecoration3_version.h
%{_includedir}/KDecoration3
%{_libdir}/libkdecorations3.*
%{_libdir}/libkdecorations3private.*

# pending rename
# %{_libdir}/cmake/KDecoration3
