#
# _without_gnome - without GNOME (build without libgnomecanvaspixbuf)
Summary:	Image loading library used with GNOME
Summary(pl):	Biblioteka ³aduj±ca obrazki u¿ywana w GNOME
Summary(pt_BR):	Biblioteca GdkPixBuf para manipulação de imagens
Name:		gdk-pixbuf
Version:	0.16.0
Release:	3.1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gdk-pixbuf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+-devel
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libungif-devel
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

%description -l pt_BR
A biblioteca GdkPixBuf oferece:

- Estrutura GdkPixBuf para representar imagens.
- Facilidades para carga de imagens.
- Maneira simples de carregar imagens animadas.
- Vários formatos: desenháveis (windows, pixmaps), buffers GdkRGB.

%package devel
Summary:	Include files for the gdk-pixbuf
Summary(pl):	Pliki nag³ówkowe dla gdk-pixbuf
Summary(pt_BR):	Bibliotecas e arquivos cabeçalhos para desenvolvimento
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Include files for the gdk-pixbuf.

%description devel -l pl
Pliki nag³ówkowe dla gdk-pixbuf.

%description devel -l pt_BR
Bibliotecas e arquivos cabeçalhos para desenvolvimento de aplicativos
baseados nessa biblioteca.

%package static
Summary:	Static gdk-pixbuf libraries
Summary(pl):	Biblioteki statyczne gdk-pixbuf
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com gdk-pixbuf
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gdk-pixbuf libraries.

%description static -l pl
Statyczne biblioteki gdk-pixbuf.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com gdk-pixbuf.

%package gnome
Summary:	GNOME part of gdk-pixbuf library
Summary(pl):	Czê¶æ gdk-pixbuf zwi±zana z GNOME
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description gnome
GNOME part of gdk-pixbuf library.

%description gnome -l pl
Czê¶æ gdk-pixbuf zwi±zana z GNOME.

%package gnome-devel
Summary:	GNOME part of gdk-pixbuf library - development files
Summary(pl):	Czê¶æ gdk-pixbuf zwi±zana z GNOME - pliki dla programistów
Group:		X11/Development/Libraries
Requires:	%{name}-gnome = %{version}
Requires:	%{name}-devel = %{version}
Requires:	gnome-libs-devel

%description gnome-devel
GNOME part of gdk-pixbuf library - development files.

%description gnome-devel -l pl
Czê¶æ gdk-pixbuf zwi±zana z GNOME - pliki dla programistów.

%package gnome-static
Summary:	GNOME part of gdk-pixbuf library - static version
Summary(pl):	Czê¶æ gdk-pixbuf zwi±zana z GNOME - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{version}

%description gnome-static
GNOME part of gdk-pixbuf library - static version.

%description gnome-static -l pl
Czê¶æ gdk-pixbuf zwi±zana z GNOME - wersja statyczna.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure \
	--disable-gtk-doc \
	CPPFLAGS="$CPPFLAGS"
%{__make} AS="%{__cc}"

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

%post	gnome -p /sbin/ldconfig
%postun	gnome -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdk*.so.*.*
%dir %{_libdir}/gdk-pixbuf
%dir %{_libdir}/gdk-pixbuf/loaders
%attr(755,root,root) %{_libdir}/gdk-pixbuf/loaders/lib*.so*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gdk-pixbuf-config
%attr(755,root,root) %{_libdir}/gdk*.sh
%attr(755,root,root) %{_libdir}/libgdk*.so
%attr(755,root,root) %{_libdir}/libgdk*.la
%dir %{_includedir}/gdk-pixbuf-1.0
%dir %{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf
%{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf/gdk*.h
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdk*.a
%{_libdir}/gdk-pixbuf/loaders/lib*.a

%if %{?_without_gnome:0}%{!?_without_gnome:1}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome*.so.*.*

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome*.sh
%attr(755,root,root) %{_libdir}/libgnome*.so
%attr(755,root,root) %{_libdir}/libgnome*.la
%{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf/gnome*.h

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgnome*.a
%endif
