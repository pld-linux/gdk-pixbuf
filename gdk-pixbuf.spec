Summary:	GdkPixBuf
Name:		gdk-pixbuf
Version:	0.8.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gdk-pixbuf/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_m4datadir	/usr/share/aclocal

%description
The GdkPixBuf library provides a number of features:
 - image loading facilities,
 - rendering of a GdkPixBuf into various formats: drawables (windows,
   pixmaps), GdkRGB buffers,
 - a cache interface.

%description -l pl
Biblioteka GdkPixBuf posiada du�e mo�liwo�ci:
    - funkcje wspomagaj�ce �adowanie obrazk�w
    - oddanie GdkPixBuf w r�nych formatach, do rysowania (okna, pixmapy)
      czy bufory GdkRGB
    - interfejs pami�ci podr�cznej

%package devel
Summary:	Libraries and include files for the gdk-pixbuf
Group:		X11/Development/Libraries
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and include files for the gdk-pixbuf.

%description -l pl devel
Biblioteki i pliki nag��wkowe dla gdk-pixbuf.

%package static
Summary:	Static gdk-pixbuf libraries
Group:		X11/Development/Libraries
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gdk-pixbuf libraries.

%description -l pl static
Statyczne biblioteki gdk-pixbuf.

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
%attr(755,root,root) %{_libdir}/gdk-pixbuf/loaders/lib*.so*
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
