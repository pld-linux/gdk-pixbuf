Summary:	Image loading library used with GNOME
Summary(pl):	Bibliotek ³aduj±ca obrazki u¿ywana w GNOME
Name:		gdk-pixbuf
Version:	0.11.0
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gdk-pixbuf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
The GdkPixBuf library provides a number of features:
 - image loading facilities,
 - rendering of a GdkPixBuf into various formats: drawables (windows,
   pixmaps), GdkRGB buffers,
 - a cache interface.

%description -l pl
Biblioteka GdkPixBuf posiada du¿e mo¿liwo¶ci:
 - funkcje wspomagaj±ce ³adowanie obrazków,
 - oddanie GdkPixBuf w ró¿nych formatach, do rysowania (okna, pixmapy)
   czy bufory GdkRGB,
 - interfejs pamiêci podrêcznej.

%package devel
Summary:	Libraries and include files for the gdk-pixbuf
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and include files for the gdk-pixbuf.

%description -l pl devel
Biblioteki i pliki nag³ówkowe dla gdk-pixbuf.

%package static
Summary:	Static gdk-pixbuf libraries
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gdk-pixbuf libraries.

%description -l pl static
Statyczne biblioteki gdk-pixbuf.

%prep
%setup -q
%patch0 -p1

%build
rm missing
libtoolize --copy --force
aclocal
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS ChangeLog NEWS README

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

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gdk-pixbuf-config
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/gdk-pixbuf
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gdk-pixbuf/loaders/lib*.a
