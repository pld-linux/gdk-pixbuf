#
# Conditional build:
%bcond_without	gnome1	# build without libgnomecanvaspixbuf (which requires GNOME)
#
Summary:	Image loading library used with GNOME
Summary(ko):	그놈에서 사용되는 그림 읽기 라이브러리
Summary(pl):	Biblioteka 쿪duj켧a obrazki u퓓wana w GNOME
Summary(pt_BR):	Biblioteca GdkPixBuf para manipula豫o de imagens
Summary(ru):	隋쫄�鞫탸� 憫할樑漑 �博쫘주턱�� � 瑙匡텀�曠� 켈� Gdk
Summary(uk):	數쫄┩旽個 憫陸塊주턱罫 博쫘주턱� 讀 瑙匡텀�曠� 켈� Gdk
Name:		gdk-pixbuf
Version:	0.22.0
Release:	11
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/0.22/%{name}-%{version}.tar.bz2
# Source0-md5:	05fcb68ceaa338614ab650c775efc2f2
Patch0:		%{name}-am.patch
Patch1:		%{name}-nognome.patch
Patch2:		%{name}-am18.patch
Patch3:		%{name}-bmploop.patch
Patch4:		%{name}-loaders.patch
Patch5:		%{name}-bmp-colormap.patch
Patch6:		%{name}-ico-width.patch
Patch7:		%{name}-link.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giflib-devel
%{?with_gnome1:BuildRequires:	gnome-libs-devel >= 1:1.4.2-15}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GdkPixBuf library provides a number of features:
 - image loading facilities,
 - rendering of a GdkPixBuf into various formats: drawables (windows,
   pixmaps), GdkRGB buffers,
 - a cache interface.

%description -l pl
Biblioteka GdkPixBuf posiada du풽 mo퓄iwo턢i:
 - funkcje wspomagaj켧e 쿪dowanie obrazk�w,
 - oddanie GdkPixBuf w r璨nych formatach, do rysowania (okna, pixmapy)
   czy bufory GdkRGB,
 - interfejs pami�ci podr�cznej.

%description -l pt_BR
A biblioteca GdkPixBuf oferece:

- Estrutura GdkPixBuf para representar imagens.
- Facilidades para carga de imagens.
- Maneira simples de carregar imagens animadas.
- V�rios formatos: desenh�veis (windows, pixmaps), buffers GdkRGB.

%description -l ru
隋쫄�鞫탸� GdkPixBuf 妗탠鞠讀隆錤� 凜謐君卦戇� 憫할倆죤� �博쫘주턱�� �
瑙匡텀�潼 �� � 怒剝芼 팥魯죤�: 駒适, 筋喀皐芩, 쫬팍籠 GdkRGB.

%description -l uk
數쫄┩旽個 GdkPixBuf 适컨� 賈勞�凜戇� 憫陸塊주兩죤� 博쫘주턱罫 讀
瑙匡텀�燉 ㎹ � 娘剝� 팥魯죤�: 屢芥�, 揆喀皐筋, 쫬팍虜 GdkRGB.

%package devel
Summary:	Include files for the gdk-pixbuf
Summary(ko):	gdk-pixbuf 응용프로그램을 개발할때 사용되는 라이브러리와 헤더파일
Summary(pl):	Pliki nag농wkowe dla gdk-pixbuf
Summary(pt_BR):	Bibliotecas e arquivos cabe�alhos para desenvolvimento
Summary(ru):	塹탠戇陸 怒撲좌鞫漑 켈� 妗逑怒袴 � GdkPixBuf
Summary(uk):	鄕遝쪼 碌撲苟漑 켈� 妗逑怒� � GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+-devel >= 1.2.0
Requires:	gtk-doc-common

%description devel
Include files for the gdk-pixbuf.

%description devel -l pl
Pliki nag농wkowe dla gdk-pixbuf.

%description devel -l pt_BR
Bibliotecas e arquivos cabe�alhos para desenvolvimento de aplicativos
baseados nessa biblioteca.

%description devel -l ru
姸奸�, 壙苟훰케梏� 켈� 怒撲좌鞫漑 妗逑怒袴, �唐驅媒藍憤� GdkPixBuf.

%description devel -l uk
姸奸�, 壙苟홀켑� 켈� 碌撲苟漑 妗逑怒�, 粉 蓋虜戇藍潼堂 GdkPixBuf.

%package static
Summary:	Static gdk-pixbuf libraries
Summary(pl):	Biblioteki statyczne gdk-pixbuf
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com gdk-pixbuf
Summary(ru):	慙죤�使沓�� 쪼쫄�鞫탸� 켈� 妗逑怒袴 � GdkPixBuf
Summary(uk):	慙죤�奢� 짝쫄┩旽漑 켈� 妗逑怒� � GdkPixBuf
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static gdk-pixbuf libraries.

%description static -l pl
Statyczne biblioteki gdk-pixbuf.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com gdk-pixbuf.

%description static -l ru
璜鞫 僅愾� 遝컵壟�� 戇죤�使沓�� 쪼쫄�鞫탸� 켈� 澹菊漑 妗逑怒袴,
�唐驅媒藍憤� GdkPixBuf.

%description static -l uk
矢� 僅愾� 稽戇�潼 戇죤�奢� 짝쫄┩旽漑 켈� 妗逑怒�, 麒� 慄蓋虜戇窘藍潼
GdkPixBuf.

%package gnome
Summary:	GNOME part of gdk-pixbuf library
Summary(pl):	Cz沅� gdk-pixbuf zwi콄ana z GNOME
Summary(ru):	隋쫄�鞫탸� 憫할樑漑 �博쫘주턱�� � 瑙匡텀�曠� 켈� Gdk
Summary(uk):	數쫄┩旽個 憫陸塊주턱罫 博쫘주턱� 讀 瑙匡텀�曠� 켈� Gdk
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-libs >= 1:1.4.2-15

%description gnome
GNOME part of gdk-pixbuf library.

%description gnome -l pl
Cz沅� gdk-pixbuf zwi콄ana z GNOME.

%description gnome -l ru
隋쫄�鞫탸� GdkPixBuf 妗탠鞠讀隆錤� 凜謐君卦戇� 憫할倆죤� �博쫘주턱�� �
瑙匡텀�潼 �� � 怒剝芼 팥魯죤�: 駒适, 筋喀皐芩, 쫬팍籠 GdkRGB.

%description gnome -l uk
數쫄┩旽個 GdkPixBuf 适컨� 賈勞�凜戇� 憫陸塊주兩죤� 博쫘주턱罫 讀
瑙匡텀�燉 ㎹ � 娘剝� 팥魯죤�: 屢芥�, 揆喀皐筋, 쫬팍虜 GdkRGB.

%package gnome-devel
Summary:	GNOME part of gdk-pixbuf library - development files
Summary(pl):	Cz沅� gdk-pixbuf zwi콄ana z GNOME - pliki dla programist�w
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-gnome = %{epoch}:%{version}-%{release}
Requires:	gnome-libs-devel >= 1:1.4.2-15

%description gnome-devel
GNOME part of gdk-pixbuf library - development files.

%description gnome-devel -l pl
Cz沅� gdk-pixbuf zwi콄ana z GNOME - pliki dla programist�w.

%package gnome-static
Summary:	GNOME part of gdk-pixbuf library - static version
Summary(pl):	Cz沅� gdk-pixbuf zwi콄ana z GNOME - wersja statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{epoch}:%{version}-%{release}

%description gnome-static
GNOME part of gdk-pixbuf library - static version.

%description gnome-static -l pl
Cz沅� gdk-pixbuf zwi콄ana z GNOME - wersja statyczna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_gnome1:--without-gnome}

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

%if %{with gnome1}
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
