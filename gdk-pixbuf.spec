#
# _without_gnome - without GNOME (build without libgnomecanvaspixbuf)
Summary:	Image loading library used with GNOME
Summary(es):	The GdkPixBuf image handling library
Summary(pl):	Biblioteka �aduj�ca obrazki u�ywana w GNOME
Summary(pt_BR):	Biblioteca GdkPixBuf para manipula��o de imagens
Name:		gdk-pixbuf
Version:	0.11.0
Release:	9
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gdk-pixbuf/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gdk-pixbuf-gnome

%define		_prefix		/usr/X11R6

%description
The GdkPixBuf library provides a number of features:
 - image loading facilities,
 - rendering of a GdkPixBuf into various formats: drawables (windows,
   pixmaps), GdkRGB buffers,
 - a cache interface.

%description -l pl
Biblioteka GdkPixBuf posiada du�e mo�liwo�ci:
 - funkcje wspomagaj�ce �adowanie obrazk�w,
 - oddanie GdkPixBuf w r�nych formatach, do rysowania (okna, pixmapy)
   czy bufory GdkRGB,
 - interfejs pami�ci podr�cznej.

%description -l es
The GdkPixBuf library provides a number of features, including :

- GdkPixbuf structure for representing images.
- Image loading facilities.
- Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.
- Fast scaling and compositing of pixbufs.
- Simple animation loading (ie. animated gifs)

%description -l pt_BR
A biblioteca GdkPixBuf oferece:

- Estrutura GdkPixBuf para representar imagens.
- Facilidades para carga de imagens.
- Maneira simples de carregar imagens animadas.
- V�rios formatos: desenh�veis (windows, pixmaps), buffers GdkRGB.

%package devel
Summary:	Libraries and include files for the gdk-pixbuf
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Summary(es):	Libraries and include files for developing GdkPixBuf applications
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Summary(pt_BR):	Bibliotecas e arquivos cabe�alhos para desenvolvimento
Requires:	%{name} = %{version}
Requires:	gnome-libs-devel

%description devel
Libraries and include files for the gdk-pixbuf.

%description -l es devel
Libraries and include files for developing GdkPixBuf applications.

%description -l pl devel
Biblioteki i pliki nag��wkowe dla gdk-pixbuf.

%description -l pt_BR devel
Bibliotecas e arquivos cabe�alhos para desenvolvimento de aplicativos baseados
nessa biblioteca.

%package static
Summary:	Static gdk-pixbuf libraries
Summary(es):	Extra documentation about gdk-pixbuf
Summary(pl):	Biblioteki statyczne gdk-pixbuf
Summary(pt_BR):	Documenta��o adicional sobre o gdk-pixbuf
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gdk-pixbuf libraries.

%description -l es static
Static libraries for gdk-pixbuf development.

%description -l pl static
Statyczne biblioteki gdk-pixbuf.

%description -l pt_BR static
Bibliotecas est�ticas para desenvolvimento com gdk-pixbuf.

%prep
%setup -q
%patch0 -p1

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
rm -f missing
automake -a -c
%configure \
	--enable-canvas-pixbuf \
	--disable-gtk-doc
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
%attr(755,root,root) %{_libdir}/libgdk*.so.*.*
%{!?_without_gnome:%attr(755,root,root) %{_libdir}/libgnome*.so.*.*}
%dir %{_libdir}/gdk-pixbuf
%dir %{_libdir}/gdk-pixbuf/loaders
%attr(755,root,root) %{_libdir}/gdk-pixbuf/loaders/lib*.so*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gdk-pixbuf-config
%attr(755,root,root) %{_libdir}/gdk*.sh
%{!?_without_gnome:%attr(755,root,root) %{_libdir}/gnome*.sh}
%attr(755,root,root) %{_libdir}/libgdk*.so
%{!?_without_gnome:%attr(755,root,root) %{_libdir}/libgnome*.so}
%attr(755,root,root) %{_libdir}/libgdk*.la
%{!?_without_gnome:%attr(755,root,root) %{_libdir}/libgnome*.la}
%{_includedir}/gdk-pixbuf
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdk*.a
%{!?_without_gnome:%{_libdir}/libgnome*.a}
%{_libdir}/gdk-pixbuf/loaders/lib*.a
