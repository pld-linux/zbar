#
# Conditional build:
%bcond_with	java	# Java interface [TODO: fix packaging]
%bcond_with	npapi	# NPAPI plugin for Firefox/OpenOffice [nothing really yet]
%bcond_with	gtk2	# GTK+ 2.x instead of 3.x
%bcond_without	perl	# Perl module
%bcond_without	python2	# Python 2.x module
%bcond_without	python3	# Python 3.x module
%bcond_without	qt	# Qt widget (Qt5 or Qt6)
%bcond_with	qt6	# Qt6 (experimental [broken as of 0.23.95]) instead of Qt5
%bcond_with	tests	# unit tests for Perl module [needs X display]
#
%if %{with java}
%{?_use_default_jdk}
%endif
Summary:	ZBar Bar Code Reader
Summary(pl.UTF-8):	ZBar - czytnik kodów paskowych
Name:		zbar
Version:	0.23.95
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/mchehab/zbar/releases
Source0:	https://github.com/mchehab/zbar/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4196d644a338733b59f9d27bf5521a34
Patch0:		%{name}-pygtk.patch
Patch2:		%{name}-npapi.patch
URL:		http://zbar.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 1:6.2.6
BuildRequires:	dbus-devel >= 1.0
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gobject-introspection-devel >= 0.6.7
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2.0}
%{!?with_gtk2:BuildRequires:	gtk+3-devel >= 3.0}
%if %{with java}
%{?buildrequires_jdk}
BuildRequires:	jpackage-utils
%endif
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libv4l-devel
BuildRequires:	meson >= 0.61.0
BuildRequires:	ninja >= 1.5
%if %{with perl}
%{?with_tests:BuildRequires:	perl-Test-Simple}
BuildRequires:	perl-devel >= 1:5.8.0
%endif
BuildRequires:	pkgconfig
%{?with_npapi:BuildRequires:	pkgconfig(mozilla-plugin)}
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7.0
BuildRequires:	python-pygtk-devel >= 2:2.0
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.043
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
%if %{with qt}
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6.2
BuildRequires:	Qt6Gui-devel >= 6.2
BuildRequires:	Qt6Widgets-devel >= 6.2
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	qt6-build >= 6.2
%else
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	Qt5X11Extras-devel >= 5
BuildRequires:	qt5-build >= 5
%endif
%endif
Requires:	ImageMagick-libs%{?_isa} >= 1:6.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZBar Bar Code Reader is an open source software suite for reading bar
codes from various sources, such as video streams, image files and raw
intensity sensors. It supports EAN-13/UPC-A, UPC-E, EAN-8, Code 128,
Code 39, Interleaved 2 of 5 and QR Code. Included with the library are
basic applications for decoding captured bar code images and using a
video device (eg, webcam) as a bar code scanner. For application
developers, language bindings are available for C, C++, Python and
Perl as well as GUI widgets for Qt, GTK+ and PyGTK.

%description -l pl.UTF-8
ZBar Bar Code Reader to zestaw oprogramowania do odczytu kodów
paskowych z różnych źródeł, takich jak strumienie wideo, pliki obrazów
oraz czujniki jasności. Obsługuje kody EAN-13/UPC-A, UPC-E, EAN-8,
Code 128, Code 39, Interleaved 2 of 5 oraz QR Code. Do biblioteki
dołączone są podstawowe aplikacje do dekodowania wyłapanych obrazów
kodów paskowych oraz używania urządzeń wejściowych obrazu (np. kamer
internetowych) jako skanera kodów paskowych. Dla programistów są
dostępne też wiązania dla C, C++, Pythona, Perla oraz widgety GUI dla
Qt, GTK+ oraz PyGTK.

%package devel
Summary:	C and C++ header files for ZBar library
Summary(pl.UTF-8):	Pliki nagłówkowe C i C++ dla biblioteki ZBar
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	xorg-lib-libXext-devel%{?_isa}
Requires:	xorg-lib-libXv-devel%{?_isa}

%description devel
C and C++ header files for ZBar library.

%description devel -l pl.UTF-8
Pliki nagłówkowe C i C++ dla biblioteki ZBar.

%package static
Summary:	Static ZBar library
Summary(pl.UTF-8):	Statyczna biblioteka ZBar
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static ZBar library.

%description static -l pl.UTF-8
Statyczna biblioteka ZBar.

%package gtk
Summary:	Bar code scanning and decoding GTK+ widget
Summary(pl.UTF-8):	Widżet GTK+ do skanowania i dekodowania kodów paskowych
Group:		X11/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description gtk
Bar code scanning and decoding GTK+ widget.

%description gtk -l pl.UTF-8
Widżet GTK+ do skanowania i dekodowania kodów paskowych.

%package gtk-devel
Summary:	Header file for bar code scanning and decoding GTK+ widget
Summary(pl.UTF-8):	Plik nagłówkowy widżetu GTK+ do skanowania i dekodowania kodów paskowych
Group:		X11/Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-gtk%{?_isa} = %{version}-%{release}
%{?with_gtk2:Requires:	gtk+2-devel%{?_isa} >= 2.0}
%{!?with_gtk2:Requires:	gtk+3-devel%{?_isa} >= 3.0}

%description gtk-devel
Header file for bar code scanning and decoding GTK+ widget.

%description gtk-devel -l pl.UTF-8
Plik nagłówkowy widżetu GTK+ do skanowania i dekodowania kodów
paskowych.

%package gtk-static
Summary:	Bar code scanning and decoding GTK+ widget - static library
Summary(pl.UTF-8):	Widżet GTK+ do skanowania i dekodowania kodów paskowych - biblioteka statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel%{?_isa} = %{version}-%{release}

%description gtk-static
Bar code scanning and decoding GTK+ widget - static library.

%description gtk-static -l pl.UTF-8
Widżet GTK+ do skanowania i dekodowania kodów paskowych - biblioteka
statyczna.

%package qt
Summary:	Bar code scanning and decoding Qt widget
Summary(pl.UTF-8):	Widżet Qt do skanowania i dekodowania kodów paskowych
Group:		X11/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description qt
Bar code scanning and decoding Qt widget.

%description qt -l pl.UTF-8
Widżet Qt do skanowania i dekodowania kodów paskowych.

%package qt-devel
Summary:	Header file for bar code scanning and decoding Qt widget
Summary(pl.UTF-8):	Plik nagłówkowy widżetu Qt do skanowania i dekodowania kodów paskowych
Group:		X11/Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-qt%{?_isa} = %{version}-%{release}
%if %{with qt6}
Requires:	Qt6Core-devel%{?_isa} >= 6
Requires:	Qt6Gui-devel%{?_isa} >= 6
Requires:	Qt6Widgets-devel%{?_isa} >= 6
%else
Requires:	Qt5Core%{?_isa} >= 5
Requires:	Qt5Gui%{?_isa} >= 5
Requires:	Qt5Widgets%{?_isa} >= 5
Requires:	Qt5X11Extras%{?_isa} >= 5
%endif

%description qt-devel
Header file for bar code scanning and decoding Qt widget.

%description qt-devel -l pl.UTF-8
Plik nagłówkowy widżetu Qt do skanowania i dekodowania kodów
paskowych.

%package qt-static
Summary:	Bar code scanning and decoding Qt widget - static library
Summary(pl.UTF-8):	Widżet Qt do skanowania i dekodowania kodów paskowych - biblioteka statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-qt-devel%{?_isa} = %{version}-%{release}

%description qt-static
Bar code scanning and decoding Qt widget - static library.

%description qt-static -l pl.UTF-8
Widżet Qt do skanowania i dekodowania kodów paskowych - biblioteka
statyczna.

%package -n perl-Barcode-ZBar
Summary:	Perl interface to ZBar bar code reader
Summary(pl.UTF-8):	Interfejs Perla do czytnika kodów paskowych ZBar
Group:		Development/Languages/Perl
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n perl-Barcode-ZBar
Perl interface to ZBar bar code reader.

%description -n perl-Barcode-ZBar -l pl.UTF-8
Interfejs Perla do czytnika kodów paskowych ZBar.

%package -n python-zbar
Summary:	Python 2 interface to ZBar bar code reader
Summary(pl.UTF-8):	Interfejs Pythona 2 do czytnika kodów paskowych ZBar
Group:		Libraries/Python
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python-libs%{?_isa} >= 1:2.7.0

%description -n python-zbar
Python 2 interface to ZBar bar code reader.

%description -n python-zbar -l pl.UTF-8
Interfejs Pythona 2 do czytnika kodów paskowych ZBar.

%package -n python-zbar-pygtk
Summary:	Bar code scanning and decoding PyGTK widget
Summary(pl.UTF-8):	Widget PyGTK do skanowania i dekodowania kodów paskowych
Group:		Libraries/Python
Requires:	%{name}-gtk%{?_isa} = %{version}-%{release}
Requires:	python-libs%{?_isa} >= 1:2.7.0
Requires:	python-pygtk-gtk%{?_isa} >= 2:2.0

%description -n python-zbar-pygtk
Bar code scanning and decoding PyGTK widget.

%description -n python-zbar-pygtk -l pl.UTF-8
Widget PyGTK do skanowania i dekodowania kodów paskowych.

%package -n python3-zbar
Summary:	Python 3 interface to ZBar bar code reader
Summary(pl.UTF-8):	Interfejs Pythona 3 do czytnika kodów paskowych ZBar
Group:		Libraries/Python
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-zbar
Python 3 interface to ZBar bar code reader.

%description -n python3-zbar -l pl.UTF-8
Interfejs Pythona 3 do czytnika kodów paskowych ZBar.

%package -n browser-plugin-zbar
Summary:	ZBar plugin for Web browsers
Summary(pl.UTF-8):	Wtyczka ZBar dla przeglądarek WWW
Group:		X11/Applications/Graphics
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	browser-plugins >= 2.0

%description -n browser-plugin-zbar
ZBar plugin for Web browsers.

%description -n browser-plugin-zbar -l pl.UTF-8
Wtyczka ZBar dla przeglądarek WWW.

%prep
%setup -q
%patch -P0 -p1
%patch -P2 -p1

%{__mv} pygtk python/pygtk

%build
%define _vpath_builddir "$builddir"
for pythonbuild in %{?with_python2:python2} %{?with_python3:python3} %{!?with_python2:%{!?with_python3:no}} ; do
builddir="build-$pythonbuild"
%meson \
	-Ddbus=enabled \
	-Dgraphicsmagick=disabled \
	-Dgtk=%{?with_gtk2:gtk2}%{!?with_gtk2:gtk3} \
	-Dimagemagick=enabled \
	-Djava=%{__enabled_disabled java} \
	-Djpeg=enabled \
	-Dnls=enabled \
	%{?with_npapi:-Dnpapi=enabled} \
	-Dpython=$pythonbuild \
	%{!?with_qt:-Dqt=false} \
	%{?with_qt6:-Dqt6=true} \
	-Dx11=enabled \
	-Dxshm=enabled \
	-Dxv=enabled

%meson_build
done

%if %{with perl}
TOPDIR=$(pwd)
cd perl
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INC="-I${TOPDIR}/include" \
	LIBS="-L${TOPDIR}/$builddir/zbar -lzbar"

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

for pythonbuild in %{?with_python2:python2} %{?with_python3:python3} %{!?with_python2:%{!?with_python3:no}} ; do
builddir="build-${pythonbuild}"

%meson_install
done

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/zbar

%if %{with perl}
%{__make} -C perl install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Barcode/ZBar/*.pod
# not rm -r to ensure it's empty after .pod removal
rmdir $RPM_BUILD_ROOT%{perl_vendorarch}/Barcode/ZBar
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Barcode/ZBar/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%endif

%if %{with npapi}
install -d $RPM_BUILD_ROOT%{_browserpluginsdir}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/libzbarplugin.so* $RPM_BUILD_ROOT%{_browserpluginsdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%post	-n browser-plugin-zbar
%update_browser_plugins

%postun	-n browser-plugin-zbar
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
# COPYING contains license summary, not LGPL text
%doc COPYING ChangeLog NEWS.md README.md SECURITY.md TODO.md
%attr(755,root,root) %{_bindir}/zbarcam
%attr(755,root,root) %{_bindir}/zbarimg
%{_libdir}/libzbar.so.*.*.*
%ghost %{_libdir}/libzbar.so.0
%{_libdir}/girepository-1.0/ZBar-1.0.typelib
# for zbarcam
/etc/dbus-1/system.d/org.linuxtv.Zbar.conf
%dir %{_datadir}/%{name}
%{_mandir}/man1/zbarcam.1*
%{_mandir}/man1/zbarimg.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libzbar.so
%{_datadir}/gir-1.0/ZBar-1.0.gir
# C
%{_includedir}/zbar.h
%dir %{_includedir}/zbar
# C++
%{_includedir}/zbar/Decoder.h
%{_includedir}/zbar/Exception.h
%{_includedir}/zbar/Image.h
%{_includedir}/zbar/ImageScanner.h
%{_includedir}/zbar/Processor.h
%{_includedir}/zbar/Scanner.h
%{_includedir}/zbar/Symbol.h
%{_includedir}/zbar/Video.h
%{_includedir}/zbar/Window.h
%{_pkgconfigdir}/zbar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libzbar.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zbarcam-gtk
%{_libdir}/libzbargtk.so.*.*.*
%ghost %{_libdir}/libzbargtk.so.0
%{_mandir}/man1/zbarcam-gtk.1*

%files gtk-devel
%defattr(644,root,root,755)
%{_libdir}/libzbargtk.so
%{_includedir}/zbar/zbargtk.h
%{_pkgconfigdir}/zbar-gtk.pc

%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libzbargtk.a

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zbarcam-qt
%{_libdir}/libzbarqt.so.*.*.*
%ghost %{_libdir}/libzbarqt.so.0
%{_mandir}/man1/zbarcam-qt.1*

%files qt-devel
%defattr(644,root,root,755)
%{_libdir}/libzbarqt.so
%{_includedir}/zbar/QZBar.h
%{_includedir}/zbar/QZBarImage.h
%{_pkgconfigdir}/zbar-qt.pc

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libzbarqt.a
%endif

# TODO: fix locations
#files -n java-zbar
#   /usr/share/zbar/lib/libzbarjni.so
#   /usr/share/zbar/lib/zbar.jar

%if %{with perl}
%files -n perl-Barcode-ZBar
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/Barcode
%{perl_vendorarch}/Barcode/ZBar.pm
%dir %{perl_vendorarch}/auto/Barcode
%dir %{perl_vendorarch}/auto/Barcode/ZBar
%{perl_vendorarch}/auto/Barcode/ZBar/ZBar.so
%{_mandir}/man3/Barcode::ZBar*.3pm*
%endif

%if %{with python2}
%files -n python-zbar
%defattr(644,root,root,755)
%{py_sitedir}/zbar.so

%files -n python-zbar-pygtk
%defattr(644,root,root,755)
%{py_sitedir}/zbarpygtk.so
%endif

%if %{with python3}
%files -n python3-zbar
%defattr(644,root,root,755)
%{py3_sitedir}/zbar.cpython-*.so
%endif

%if %{with npapi}
%files -n browser-plugin-zbar
%defattr(644,root,root,755)
%{_browserpluginsdir}/libzbarplugin.so*
%endif
