%define url_ver %(echo %{version}|cut -d. -f1,2)

%define pkgname	libsigc++
%define api	2.0
%define major	0
%define libname	%mklibname sigc++ %{api} %{major}
%define devname	%mklibname -d sigc++ %{api}
%define _disable_rebuild_configure 1

Summary:	The Typesafe Signal Framework for C++
Name:		%{pkgname}%{api}
Version:	2.10.4
Release:	1
License:	LGPLv2
Group:		System/Libraries
Url:		http://libsigc.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsigc++/%{url_ver}/%{pkgname}-%{version}.tar.xz
BuildRequires:	mm-common
BuildRequires:  meson

%description
Callback system for use in widget libraries, abstract interfaces, and
general programming.

This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally part
of the Gtk-- widget set, %{pkgname} is now a separate library to provide for
more general use. It is the most complete library of its kind with the
ablity to connect an abstract callback to a class method, function, or
function object. It contains adaptor classes for connection of dissimilar
callbacks and has an ease of use unmatched by other C++ callback
libraries.

Package gtkmm, which is a c++ binding to the famous gtk+ library, uses
%{pkgname}.

%package -n %{libname}
Summary:	The Typesafe Signal Framework for C++
Group:		System/Libraries
Provides:	%{pkgname}%{api} = %{version}-%{release}

%description -n %{libname}
Callback system for use in widget libraries, abstract interfaces, and
general programming.

This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally part
of the Gtk-- widget set, %{pkgname} is now a separate library to provide for
more general use. It is the most complete library of its kind with the
ablity to connect an abstract callback to a class method, function, or
function object. It contains adaptor classes for connection of dissimilar
callbacks and has an ease of use unmatched by other C++ callback
libraries.

Package gtkmm, which is a c++ binding to the famous gtk+ library, uses
%{pkgname}.


%package -n %{devname}
Summary:	Development tools for the Typesafe Signal Framework for C++ 
Group:		Development/C++
Provides:	%{pkgname}%{api}-devel = %{version}-%{release}
Provides:	sigc++%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the headers and static libraries of %{pkgname},
which are needed when developing or compiling applications which use
%{pkgname}.

#package doc
#Summary:	Documentation for %{pkgname} library
#Group:		Books/Other

#description doc
#This package provides API documentation of %{pkgname} library.

%prep
%setup -qn %{pkgname}-%{version}

%build
%meson
%meson_build

%install
%meson_install
rm -f %{buildroot}/%{_docdir}/ChangeLog

%files -n %{libname}
%{_libdir}/libsigc-%{api}.so.%{major}*

%files -n %{devname}
%doc COPYING NEWS README AUTHORS
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++-%{api}

#files doc
#doc %{_docdir}/libsigc++-%{api}
#_datadir/devhelp/books/libsigc++-%{api}
