
#
# _without_gnome - without GNOME (build without libgnomecanvaspixbuf)
#

Summary:	Image loading library used with GNOME
Summary(pl):	Biblioteka �aduj�ca obrazki u�ywana w GNOME
Summary(pt_BR):	Biblioteca GdkPixBuf para manipula��o de imagens
Summary(ru):	���������� �������� ����������� � ���������� ��� Gdk
Summary(uk):	��̦����� ������������ ��������� �� ���������� ��� Gdk
Name:		gdk-pixbuf
Version:	0.17.0
Release:	1
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
Biblioteka GdkPixBuf posiada du�e mo�liwo�ci:
 - funkcje wspomagaj�ce �adowanie obrazk�w,
 - oddanie GdkPixBuf w r�nych formatach, do rysowania (okna, pixmapy)
   czy bufory GdkRGB,
 - interfejs pami�ci podr�cznej.

%description -l pt_BR
A biblioteca GdkPixBuf oferece:

- Estrutura GdkPixBuf para representar imagens.
- Facilidades para carga de imagens.
- Maneira simples de carregar imagens animadas.
- V�rios formatos: desenh�veis (windows, pixmaps), buffers GdkRGB.

%description -l ru
���������� GdkPixBuf ������������� ����������� ��������� ����������� �
��������� �� � ������ �������: ����, ��������, ������ GdkRGB.

%description -l uk
��̦����� GdkPixBuf ����� ��������Ԧ ������������� ���������� ��
��������� �� � Ҧ�Φ �������: צ���, Ц������, ������ GdkRGB.

%package devel
Summary:	Include files for the gdk-pixbuf
Summary(pl):	Pliki nag��wkowe dla gdk-pixbuf
Summary(pt_BR):	Bibliotecas e arquivos cabe�alhos para desenvolvimento
Summary(ru):	�������� ���������� ��� �������� � GdkPixBuf
Summary(uk):	������ �������� ��� ������� � GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Include files for the gdk-pixbuf.

%description devel -l pl
Pliki nag��wkowe dla gdk-pixbuf.

%description devel -l pt_BR
Bibliotecas e arquivos cabe�alhos para desenvolvimento de aplicativos
baseados nessa biblioteca.

%description devel -l ru
�����, ����������� ��� ���������� ��������, ������������ GdkPixBuf.

%description devel -l uk
�����, ����Ȧ�Φ ��� �������� �������, �� ������������ GdkPixBuf.

%package static
Summary:	Static gdk-pixbuf libraries
Summary(pl):	Biblioteki statyczne gdk-pixbuf
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gdk-pixbuf
Summary(ru):	����������� ���������� ��� �������� � GdkPixBuf
Summary(uk):	������Φ ¦�̦����� ��� ������� � GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gdk-pixbuf libraries.

%description static -l pl
Statyczne biblioteki gdk-pixbuf.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com gdk-pixbuf.

%description static -l ru
���� ����� �������� ����������� ���������� ��� ������ ��������,
������������ GdkPixBuf.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦����� ��� �������, �˦ ��������������
GdkPixBuf.

%package gnome
Summary:	GNOME part of gdk-pixbuf library
Summary(pl):	Cz�� gdk-pixbuf zwi�zana z GNOME
Summary(ru):	���������� �������� ����������� � ���������� ��� Gdk
Summary(uk):	��̦����� ������������ ��������� �� ���������� ��� Gdk
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description gnome
GNOME part of gdk-pixbuf library.

%description gnome -l pl
Cz�� gdk-pixbuf zwi�zana z GNOME.

%description gnome -l ru
���������� GdkPixBuf ������������� ����������� ��������� ����������� �
��������� �� � ������ �������: ����, ��������, ������ GdkRGB.

%description gnome -l uk
��̦����� GdkPixBuf ����� ��������Ԧ ������������� ���������� ��
��������� �� � Ҧ�Φ �������: צ���, Ц������, ������ GdkRGB.

%package gnome-devel
Summary:	GNOME part of gdk-pixbuf library - development files
Summary(pl):	Cz�� gdk-pixbuf zwi�zana z GNOME - pliki dla programist�w
Group:		X11/Development/Libraries
Requires:	%{name}-gnome = %{version}
Requires:	%{name}-devel = %{version}
Requires:	gnome-libs-devel

%description gnome-devel
GNOME part of gdk-pixbuf library - development files.

%description gnome-devel -l pl
Cz�� gdk-pixbuf zwi�zana z GNOME - pliki dla programist�w.

%package gnome-static
Summary:	GNOME part of gdk-pixbuf library - static version
Summary(pl):	Cz�� gdk-pixbuf zwi�zana z GNOME - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{version}

%description gnome-static
GNOME part of gdk-pixbuf library - static version.

%description gnome-static -l pl
Cz�� gdk-pixbuf zwi�zana z GNOME - wersja statyczna.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake} -a -c
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
