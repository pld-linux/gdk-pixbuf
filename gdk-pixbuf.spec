#
# Conditional build:
%bcond_with	gnome1		# build with libgnomecanvaspixbuf (which requires GNOME)
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Image loading library used with GNOME
Summary(ko.UTF-8):	그놈에서 사용되는 그림 읽기 라이브러리
Summary(pl.UTF-8):	Biblioteka ładująca obrazki używana w GNOME
Summary(pt_BR.UTF-8):	Biblioteca GdkPixBuf para manipulação de imagens
Summary(ru.UTF-8):	Библиотека загрузки изображений и рендеринга для Gdk
Summary(uk.UTF-8):	Бібліотека завантаження зображень та рендерингу для Gdk
Name:		gdk-pixbuf
Version:	0.22.0
Release:	25
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/0.22/%{name}-%{version}.tar.bz2
# Source0-md5:	05fcb68ceaa338614ab650c775efc2f2
Patch0:		%{name}-am.patch
Patch1:		%{name}-nognome.patch
Patch2:		%{name}-am18.patch
Patch3:		%{name}-bmploop.patch
Patch4:		%{name}-loaders.patch
Patch5:		%{name}-bmp-colormap.patch
Patch6:		%{name}-ico-width.patch
Patch7:		%{name}-link.patch
Patch8:		%{name}-ac.patch
Patch9:		%{name}-libpng15.patch
URL:		http://developer.gnome.org/arch/imaging/gdkpixbuf.html
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gnome1:BuildRequires:	gnome-libs-devel >= 1:1.4.2-15}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GdkPixBuf library provides a number of features:
 - image loading facilities,
 - rendering of a GdkPixBuf into various formats: drawables (windows,
   pixmaps), GdkRGB buffers,
 - a cache interface.

%description -l pl.UTF-8
Biblioteka GdkPixBuf posiada duże możliwości:
 - funkcje wspomagające ładowanie obrazków,
 - oddanie GdkPixBuf w różnych formatach, do rysowania (okna, pixmapy)
   czy bufory GdkRGB,
 - interfejs pamięci podręcznej.

%description -l pt_BR.UTF-8
A biblioteca GdkPixBuf oferece:

- Estrutura GdkPixBuf para representar imagens.
- Facilidades para carga de imagens.
- Maneira simples de carregar imagens animadas.
- Vários formatos: desenháveis (windows, pixmaps), buffers GdkRGB.

%description -l ru.UTF-8
Библиотека GdkPixBuf предоставляет возможность загружать изображения и
рендерить их в разные форматы: окна, пиксмапы, буферы GdkRGB.

%description -l uk.UTF-8
Бібліотека GdkPixBuf надає можливості завантажувати зображення та
рендерити їх в різні формати: вікна, піксмапи, буфери GdkRGB.

%package devel
Summary:	Include files for the gdk-pixbuf
Summary(ko.UTF-8):	gdk-pixbuf 응용프로그램을 개발할때 사용되는 라이브러리와 헤더파일
Summary(pl.UTF-8):	Pliki nagłówkowe dla gdk-pixbuf
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos cabeçalhos para desenvolvimento
Summary(ru.UTF-8):	Средства разработки для программ с GdkPixBuf
Summary(uk.UTF-8):	Засоби розробки для програм з GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+-devel >= 1.2.0
Requires:	gtk-doc-common

%description devel
Include files for the gdk-pixbuf.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gdk-pixbuf.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos cabeçalhos para desenvolvimento de aplicativos
baseados nessa biblioteca.

%description devel -l ru.UTF-8
Файлы, необходимые для разработки программ, использующих GdkPixBuf.

%description devel -l uk.UTF-8
Файли, необхідні для розробки програм, що користуються GdkPixBuf.

%package static
Summary:	Static gdk-pixbuf libraries
Summary(pl.UTF-8):	Biblioteki statyczne gdk-pixbuf
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com gdk-pixbuf
Summary(ru.UTF-8):	Статические библиотеки для программ с GdkPixBuf
Summary(uk.UTF-8):	Статичні бібліотеки для програм з GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static gdk-pixbuf libraries.

%description static -l pl.UTF-8
Statyczne biblioteki gdk-pixbuf.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com gdk-pixbuf.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для сборки программ,
использующих GdkPixBuf.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки для програм, які використовують
GdkPixBuf.

%package gnome
Summary:	GNOME part of gdk-pixbuf library
Summary(pl.UTF-8):	Część gdk-pixbuf związana z GNOME
Summary(ru.UTF-8):	Библиотека загрузки изображений и рендеринга для Gdk
Summary(uk.UTF-8):	Бібліотека завантаження зображень та рендерингу для Gdk
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-libs >= 1:1.4.2-15

%description gnome
GNOME part of gdk-pixbuf library.

%description gnome -l pl.UTF-8
Część gdk-pixbuf związana z GNOME.

%description gnome -l ru.UTF-8
Библиотека GdkPixBuf предоставляет возможность загружать изображения и
рендерить их в разные форматы: окна, пиксмапы, буферы GdkRGB.

%description gnome -l uk.UTF-8
Бібліотека GdkPixBuf надає можливості завантажувати зображення та
рендерити їх в різні формати: вікна, піксмапи, буфери GdkRGB.

%package gnome-devel
Summary:	GNOME part of gdk-pixbuf library - development files
Summary(pl.UTF-8):	Część gdk-pixbuf związana z GNOME - pliki dla programistów
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-gnome = %{epoch}:%{version}-%{release}
Requires:	gnome-libs-devel >= 1:1.4.2-15

%description gnome-devel
GNOME part of gdk-pixbuf library - development files.

%description gnome-devel -l pl.UTF-8
Część gdk-pixbuf związana z GNOME - pliki dla programistów.

%package gnome-static
Summary:	GNOME part of gdk-pixbuf library - static version
Summary(pl.UTF-8):	Część gdk-pixbuf związana z GNOME - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{epoch}:%{version}-%{release}

%description gnome-static
GNOME part of gdk-pixbuf library - static version.

%description gnome-static -l pl.UTF-8
Część gdk-pixbuf związana z GNOME - wersja statyczna.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p0
%patch -P9 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc \
	%{!?with_static_libs:--disable-static} \
	%{!?with_gnome1:--without-gnome} \
	--with-html-dir=%{_gtkdocdir}

%{__make} \
	AS="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	HTML_DIR=%{_gtkdocdir}

# resolve conflict with gtk+2-devel
%{__mv} $RPM_BUILD_ROOT%{_gtkdocdir}/gdk-pixbuf{,-1.0}

# no *.{a,la} for plugins
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf/loaders/lib*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf/loaders/lib*.a
%endif

# cleanup non-gnome build
%if %{without gnome}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnomecanvaspixbufConf.sh
%{__rm} $RPM_BUILD_ROOT%{_gtkdocdir}/gdk-pixbuf-1.0/gnomecanvaspixbuf.html
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	gnome -p /sbin/ldconfig
%postun	gnome -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgdk_pixbuf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdk_pixbuf.so.2
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdk_pixbuf_xlib.so.2
%dir %{_libdir}/gdk-pixbuf
%dir %{_libdir}/gdk-pixbuf/loaders
%attr(755,root,root) %{_libdir}/gdk-pixbuf/loaders/libpixbufloader-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdk-pixbuf-config
%attr(755,root,root) %{_libdir}/gdk_pixbufConf.sh
%attr(755,root,root) %{_libdir}/gdk_pixbuf_xlibConf.sh
%attr(755,root,root) %{_libdir}/libgdk_pixbuf.so
%attr(755,root,root) %{_libdir}/libgdk_pixbuf_xlib.so
%{_libdir}/libgdk_pixbuf.la
%{_libdir}/libgdk_pixbuf_xlib.la
%dir %{_includedir}/gdk-pixbuf-1.0
%dir %{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf
%{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf/gdk-pixbuf*.h
%{_aclocaldir}/gdk-pixbuf.m4
%dir %{_gtkdocdir}/gdk-pixbuf-1.0
%{_gtkdocdir}/gdk-pixbuf-1.0/a*.html
%{_gtkdocdir}/gdk-pixbuf-1.0/compiling.html
%{_gtkdocdir}/gdk-pixbuf-1.0/extra-configuration-options.html
%{_gtkdocdir}/gdk-pixbuf-1.0/gdk-pixbuf-*.html
%{_gtkdocdir}/gdk-pixbuf-1.0/gdkpixbufloader.html
%{_gtkdocdir}/gdk-pixbuf-1.0/index.html
%{_gtkdocdir}/gdk-pixbuf-1.0/license.html
%{_gtkdocdir}/gdk-pixbuf-1.0/r*.html
%{_gtkdocdir}/gdk-pixbuf-1.0/x*.html

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdk_pixbuf.a
%{_libdir}/libgdk_pixbuf_xlib.a
%endif

%if %{with gnome1}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecanvaspixbuf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomecanvaspixbuf.so.1

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnomecanvaspixbufConf.sh
%attr(755,root,root) %{_libdir}/libgnomecanvaspixbuf.so
%{_libdir}/libgnomecanvaspixbuf.la
%{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf/gnome-canvas-pixbuf.h
%{_gtkdocdir}/gdk-pixbuf-1.0/gnomecanvaspixbuf.html

%if %{with static_libs}
%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgnomecanvaspixbuf.a
%endif
%endif
