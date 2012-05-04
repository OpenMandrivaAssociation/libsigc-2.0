%define pkgname libsigc++

%define api 2.0
%define major 0
%define libname %mklibname sigc++ %{api} %{major}
%define develname %mklibname -d sigc++ %{api}

Name:		%{pkgname}%{api}
Summary:	The Typesafe Signal Framework for C++
Version:	2.2.10
Release:	3
License:	LGPL
Group:		System/Libraries
URL:		http://libsigc.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz

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


%package -n %{develname}
Summary:	Development tools for the Typesafe Signal Framework for C++ 
Group:		Development/C++
Provides:	libsigc++1.2-examples
Obsoletes:	libsigc++1.2-examples
Provides:	%{pkgname}%{api}-devel = %{version}-%{release}
Provides:	sigc++%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{develname}
This package contains the headers and static libraries of %{pkgname},
which are needed when developing or compiling applications which use
%{pkgname}.

%package doc
Summary:	Documentation for %{pkgname} library
Group:		Books/Other

%description doc
This package provides API documentation of %{pkgname} library.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x
%make

%check
make check

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING NEWS README
%{_libdir}/libsigc-%{api}.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog TODO
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++-%{api}

%files doc
%doc %{_docdir}/libsigc++-%{api}
%_datadir/devhelp/books/libsigc++-%{api}

