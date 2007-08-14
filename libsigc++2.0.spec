%define version 2.1.1
%define release %mkrel 1

%define pkgname libsigc++

%define api_version 2.0
%define major 0
%define libname %mklibname sigc++ %api_version %major
%define libnamedev %mklibname -d sigc++ %api_version

Name:		%{pkgname}%{api_version}
Summary:	The Typesafe Signal Framework for C++
Version:	%{version}
Release:	%{release}
License:	LGPL
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
URL:		http://libsigc.sourceforge.net/
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


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
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

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


%package -n %{libnamedev}
Summary:	Development tools for the Typesafe Signal Framework for C++ 
Group:		Development/C++
Provides:	libsigc++1.2-examples
Obsoletes:	libsigc++1.2-examples
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	sigc++%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes: %mklibname -d %api_version %major

%description -n %{libnamedev}
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING NEWS README
%{_libdir}/libsigc-%{api_version}.so.%{major}*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc AUTHORS ChangeLog TODO
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++-%{api_version}

%files doc
%defattr(-, root, root)
%doc %{_docdir}/libsigc-%{api_version}


