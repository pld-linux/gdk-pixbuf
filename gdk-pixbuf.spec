Summary:	GdkPixBuf
Name:		gdk-pixbuf
Version: 	0.4
Release: 	1
Copyright: 	GPL
Group:		Libraries
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/%{name}-%{version}.tar.gz
URL: 		http://www.gnome.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
The GdkPixBuf library provides a number of features:

        - Image loading facilities.
        - Rendering of a GdkPixBuf into various formats:
          drawables (windows, pixmaps), GdkRGB buffers.
        - A cache interface

%package devel
Summary:	Libraries and include files for the gdk-pixbuf
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries and include files for the gdk-pixbuf.

%package static
Summary:	Static gdk-pixbuf libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static bonobo libraries.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf/loaders/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gdk-pixbuf
%dir %{_libdir}/gdk-pixbuf/loaders
%attr(755,root,root) %{_libdir}/gdk-pixbuf/loaders/lib*.so
%attr(755,root,root) %{_libdir}/gdk-pixbuf/loaders/lib*.la

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/gdk-pixbuf

%files static
%defattr(644,root,root)
%{_libdir}/lib*.a
%{_libdir}/gdk-pixbuf/loaders/lib*.a
