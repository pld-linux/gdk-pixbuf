Summary:	GdkPixBuf
Name:		gdk-pixbuf
Version:	0.6.0
Release:	1
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/gdk-pixbuf/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	gtk+-devel
BuildRequires:	XFree86-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	esound-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_m4datadir	/usr/share/aclocal

%description
The GdkPixBuf library provides a number of features:
	- image loading facilities,
	- rendering of a GdkPixBuf into various formats:
	  drawables (windows, pixmaps), GdkRGB buffers,
	- a cache interface.

%description -l pl
Biblioteka GdkPixBuf posiada du¿e mo¿liwo¶ci:
    - funkcje wspomagaj±ce ³adowanie obrazków
    - oddanie GdkPixBuf w ró¿nych formatach, do rysowania (okna, pixmapy)
      czy bufory GdkRGB
    - interfejs pamiêci podrêcznej

%package devel
Summary:	Libraries and include files for the gdk-pixbuf
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and include files for the gdk-pixbuf.

%description -l pl devel
Biblioteki i pliki nag³ówkowe dla gdk-pixbuf.

%package static
Summary:	Static gdk-pixbuf libraries
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static bonobo libraries.

%description -l pl static
Statyczne biblioteki bonobo

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_m4datadir}

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
%attr(755,root,root) %{_bindir}/gdk-pixbuf-config
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/gdk-pixbuf
%{_m4datadir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gdk-pixbuf/loaders/lib*.a
