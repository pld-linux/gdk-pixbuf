#
# Conditional build:
%bcond_without	gnome	# build without libgnomecanvaspixbuf (which requires GNOME)
#
Summary:	Image loading library used with GNOME
Summary(pl):	Biblioteka Ёaduj╠ca obrazki u©ywana w GNOME
Summary(pt_BR):	Biblioteca GdkPixBuf para manipulaГЦo de imagens
Summary(ko):	╠вЁП©║╪╜ ╩Г©К╣г╢б ╠в╦╡ юп╠Б ╤Сюл╨Й╥╞╦╝
Summary(ru):	Библиотека загрузки изображений и рендеринга для Gdk
Summary(uk):	Б╕бл╕отека завантаження зображень та рендерингу для Gdk
Name:		gdk-pixbuf
Version:	0.22.0
Release:	8
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/0.22/%{name}-%{version}.tar.bz2
# Source0-md5: 05fcb68ceaa338614ab650c775efc2f2
Patch0:		%{name}-am.patch
Patch1:		%{name}-nognome.patch
Patch2:		%{name}-am18.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
%{?with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
The GdkPixBuf library provides a number of features:
 - image loading facilities,
 - rendering of a GdkPixBuf into various formats: drawables (windows,
   pixmaps), GdkRGB buffers,
 - a cache interface.

%description -l pl
Biblioteka GdkPixBuf posiada du©e mo©liwo╤ci:
 - funkcje wspomagaj╠ce Ёadowanie obrazkСw,
 - oddanie GdkPixBuf w rС©nych formatach, do rysowania (okna, pixmapy)
   czy bufory GdkRGB,
 - interfejs pamiЙci podrЙcznej.

%description -l pt_BR
A biblioteca GdkPixBuf oferece:

- Estrutura GdkPixBuf para representar imagens.
- Facilidades para carga de imagens.
- Maneira simples de carregar imagens animadas.
- VАrios formatos: desenhАveis (windows, pixmaps), buffers GdkRGB.

%description -l ru
Библиотека GdkPixBuf предоставляет возможность загружать изображения и
рендерить их в разные форматы: окна, пиксмапы, буферы GdkRGB.

%description -l uk
Б╕бл╕отека GdkPixBuf нада╓ можливост╕ завантажувати зображення та
рендерити ╖х в р╕зн╕ формати: в╕кна, п╕ксмапи, буфери GdkRGB.

%package devel
Summary:	Include files for the gdk-pixbuf
Summary(pl):	Pliki nagЁСwkowe dla gdk-pixbuf
Summary(pt_BR):	Bibliotecas e arquivos cabeГalhos para desenvolvimento
Summary(ko):	gdk-pixbuf юю©Кга╥н╠в╥╔ю╩ ╟Ё╧ъгр╤╖ ╩Г©К╣г╢б ╤Сюл╨Й╥╞╦╝©м гЛ╢Уфдюо
Summary(ru):	Средства разработки для программ с GdkPixBuf
Summary(uk):	Засоби розробки для програм з GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	gtk+-devel
Requires:	gtk-doc-common

%description devel
Include files for the gdk-pixbuf.

%description devel -l pl
Pliki nagЁСwkowe dla gdk-pixbuf.

%description devel -l pt_BR
Bibliotecas e arquivos cabeГalhos para desenvolvimento de aplicativos
baseados nessa biblioteca.

%description devel -l ru
Файлы, необходимые для разработки программ, использующих GdkPixBuf.

%description devel -l uk
Файли, необх╕дн╕ для розробки програм, що користуються GdkPixBuf.

%package static
Summary:	Static gdk-pixbuf libraries
Summary(pl):	Biblioteki statyczne gdk-pixbuf
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com gdk-pixbuf
Summary(ru):	Статические библиотеки для программ с GdkPixBuf
Summary(uk):	Статичн╕ б╕бл╕отеки для програм з GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static gdk-pixbuf libraries.

%description static -l pl
Statyczne biblioteki gdk-pixbuf.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com gdk-pixbuf.

%description static -l ru
Этот пакет содержит статические библиотеки для сборки программ,
использующих GdkPixBuf.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки для програм, як╕ використовують
GdkPixBuf.

%package gnome
Summary:	GNOME part of gdk-pixbuf library
Summary(pl):	CzЙ╤Ф gdk-pixbuf zwi╠zana z GNOME
Summary(ru):	Библиотека загрузки изображений и рендеринга для Gdk
Summary(uk):	Б╕бл╕отека завантаження зображень та рендерингу для Gdk
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description gnome
GNOME part of gdk-pixbuf library.

%description gnome -l pl
CzЙ╤Ф gdk-pixbuf zwi╠zana z GNOME.

%description gnome -l ru
Библиотека GdkPixBuf предоставляет возможность загружать изображения и
рендерить их в разные форматы: окна, пиксмапы, буферы GdkRGB.

%description gnome -l uk
Б╕бл╕отека GdkPixBuf нада╓ можливост╕ завантажувати зображення та
рендерити ╖х в р╕зн╕ формати: в╕кна, п╕ксмапи, буфери GdkRGB.

%package gnome-devel
Summary:	GNOME part of gdk-pixbuf library - development files
Summary(pl):	CzЙ╤Ф gdk-pixbuf zwi╠zana z GNOME - pliki dla programistСw
Group:		X11/Development/Libraries
Requires:	%{name}-gnome = %{epoch}:%{version}
Requires:	%{name}-devel = %{epoch}:%{version}
Requires:	gnome-libs-devel

%description gnome-devel
GNOME part of gdk-pixbuf library - development files.

%description gnome-devel -l pl
CzЙ╤Ф gdk-pixbuf zwi╠zana z GNOME - pliki dla programistСw.

%package gnome-static
Summary:	GNOME part of gdk-pixbuf library - static version
Summary(pl):	CzЙ╤Ф gdk-pixbuf zwi╠zana z GNOME - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{epoch}:%{version}

%description gnome-static
GNOME part of gdk-pixbuf library - static version.

%description gnome-static -l pl
CzЙ╤Ф gdk-pixbuf zwi╠zana z GNOME - wersja statyczna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_gnome:--without-gnome}

%{__make} \
	AS="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	HTML_DIR=%{_gtkdocdir}

# resolve conflict with gtk+2-devel
mv -f $RPM_BUILD_ROOT%{_gtkdocdir}/gdk-pixbuf{,-1.0}

# no *.{a,la} for plugins - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf/loaders/lib*.{a,la}

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gdk-pixbuf-config
%attr(755,root,root) %{_libdir}/gdk*.sh
%attr(755,root,root) %{_libdir}/libgdk*.so
%{_libdir}/libgdk*.la
%dir %{_includedir}/gdk-pixbuf-1.0
%dir %{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf
%{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf/gdk*.h
%{_aclocaldir}/*
%dir %{_gtkdocdir}/gdk-pixbuf-1.0
%{_gtkdocdir}/gdk-pixbuf-1.0/[!g]*
%{_gtkdocdir}/gdk-pixbuf-1.0/g[!n]*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdk*.a

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome*.so.*.*

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome*.sh
%attr(755,root,root) %{_libdir}/libgnome*.so
%{_libdir}/libgnome*.la
%{_includedir}/gdk-pixbuf-1.0/gdk-pixbuf/gnome*.h
%{_gtkdocdir}/gdk-pixbuf-1.0/gnome*

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libgnome*.a
%endif
