#
# Conditional build:
%bcond_with	java	# Java interface [some file missing]
%bcond_with	npapi	# NPAPI plugin for Firefox/OpenOffice [nothing really yet]
%bcond_without	qt	# Qt widget (Qt5 or Qt4)
%bcond_with	qt4	# Qt4 instead of Qt5
%bcond_with	tests	# "make test" for Perl module [needs X display]
#
%include	/usr/lib/rpm/macros.perl
Summary:	ZBar Bar Code Reader
Summary(pl.UTF-8):	ZBar - czytnik kodów paskowych
Name:		zbar
Version:	0.20
Release:	4
License:	LGPL v2.1+
Group:		Libraries
# no releases since 2009
#Source0:	http://downloads.sourceforge.net/zbar/%{name}-%{version}.tar.bz2
# non-maintainer release
Source0:	https://linuxtv.org/downloads/zbar/%{name}-%{version}.tar.bz2
# Source0-md5:	116805d44246e288f1f42729950878bf
#Patch0:		zbar_update_to_hg.patch
Patch0:		%{name}-sh.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-npapi.patch
#Patch3:		zbar_use_libv4l.patch
#Patch3:		%{name}-ac.patch
Patch3:		imagemagick7.patch
URL:		http://zbar.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 1:6.2.6
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.13
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2.0
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libv4l-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
%{?with_npapi:BuildRequires:	pkgconfig(mozilla-plugin)}
BuildRequires:	python-devel >= 2.3.5
BuildRequires:	python-pygtk-devel >= 2:2.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
%if %{with qt}
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	qt4-build >= 4
%else
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	Qt5X11Extras-devel >= 5
BuildRequires:	qt5-build >= 5
%endif
%endif
Requires:	ImageMagick-libs >= 1:6.2.6
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
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXv-devel

%description devel
C and C++ header files for ZBar library.

%description devel -l pl.UTF-8
Pliki nagłówkowe C i C++ dla biblioteki ZBar.

%package static
Summary:	Static ZBar library
Summary(pl.UTF-8):	Statyczna biblioteka ZBar
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ZBar library.

%description static -l pl.UTF-8
Statyczna biblioteka ZBar.

%package gtk
Summary:	Bar code scanning and decoding GTK+ widget
Summary(pl.UTF-8):	Widget GTK+ do skanowania i dekodowania kodów paskowych
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
Bar code scanning and decoding GTK+ widget.

%description gtk -l pl.UTF-8
Widget GTK+ do skanowania i dekodowania kodów paskowych.

%package gtk-devel
Summary:	Header file for bar code scanning and decoding GTK+ widget
Summary(pl.UTF-8):	Plik nagłówkowy widgetu GTK+ do skanowania i dekodowania kodów paskowych
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0

%description gtk-devel
Header file for bar code scanning and decoding GTK+ widget.

%description gtk-devel -l pl.UTF-8
Plik nagłówkowy widgetu GTK+ do skanowania i dekodowania kodów
paskowych.

%package gtk-static
Summary:	Bar code scanning and decoding GTK+ widget - static library
Summary(pl.UTF-8):	Widget GTK+ do skanowania i dekodowania kodów paskowych - biblioteka statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Bar code scanning and decoding GTK+ widget - static library.

%description gtk-static -l pl.UTF-8
Widget GTK+ do skanowania i dekodowania kodów paskowych - biblioteka
statyczna.

%package qt
Summary:	Bar code scanning and decoding Qt4 widget
Summary(pl.UTF-8):	Widget Qt4 do skanowania i dekodowania kodów paskowych
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description qt
Bar code scanning and decoding Qt4 widget.

%description qt -l pl.UTF-8
Widget Qt4 do skanowania i dekodowania kodów paskowych.

%package qt-devel
Summary:	Header file for bar code scanning and decoding Qt4 widget
Summary(pl.UTF-8):	Plik nagłówkowy widgetu Qt4 do skanowania i dekodowania kodów paskowych
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
%if %{with qt4}
Requires:	QtCore-devel >= 4
Requires:	QtGui-devel >= 4
%else
Requires:	Qt5Core >= 5
Requires:	Qt5Gui >= 5
Requires:	Qt5Widgets >= 5
Requires:	Qt5X11Extras >= 5
%endif

%description qt-devel
Header file for bar code scanning and decoding Qt4 widget.

%description qt-devel -l pl.UTF-8
Plik nagłówkowy widgetu Qt4 do skanowania i dekodowania kodów
paskowych.

%package qt-static
Summary:	Bar code scanning and decoding Qt4 widget - static library
Summary(pl.UTF-8):	Widget Qt4 do skanowania i dekodowania kodów paskowych - biblioteka statyczna
Group:		X11/Development/Libraries
Requires:	%{name}-qt-devel = %{version}-%{release}

%description qt-static
Bar code scanning and decoding Qt4 widget - static library.

%description qt-static -l pl.UTF-8
Widget Qt4 do skanowania i dekodowania kodów paskowych - biblioteka
statyczna.

%package -n perl-Barcode-ZBar
Summary:	Perl interface to ZBar bar code reader
Summary(pl.UTF-8):	Interfejs Perla do czytnika kodów paskowych ZBar
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Barcode-ZBar
Perl interface to ZBar bar code reader.

%description -n perl-Barcode-ZBar -l pl.UTF-8
Interfejs Perla do czytnika kodów paskowych ZBar.

%package -n python-zbar
Summary:	Python interface to ZBar bar code reader
Summary(pl.UTF-8):	Interfejs Pythona do czytnika kodów paskowych ZBar
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-zbar
Python interface to ZBar bar code reader.

%description -n python-zbar -l pl.UTF-8
Interfejs Pythona do czytnika kodów paskowych ZBar.

%package -n python-zbar-pygtk
Summary:	Bar code scanning and decoding PyGTK widget
Summary(pl.UTF-8):	Widget PyGTK do skanowania i dekodowania kodów paskowych
Group:		Libraries/Python
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.0
%pyrequires_eq	python-libs

%description -n python-zbar-pygtk
Bar code scanning and decoding PyGTK widget.

%description -n python-zbar-pygtk -l pl.UTF-8
Widget PyGTK do skanowania i dekodowania kodów paskowych.

%package -n browser-plugin-zbar
Summary:	ZBar plugin for Web browsers
Summary(pl.UTF-8):	Wtyczka ZBar dla przeglądarek WWW
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins >= 2.0

%description -n browser-plugin-zbar
ZBar plugin for Web browsers.

%description -n browser-plugin-zbar -l pl.UTF-8
Wtyczka ZBar dla przeglądarek WWW.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#patch4 -p1
%if "%(rpm -q ImageMagick-devel --qf '%{VERSION}')" >= "7"
%patch3 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# for ">>" in nested template usage
CXXFLAGS="%{rpmcxxflags} -std=c++11"
%configure \
	%{!?with_java:--without-java} \
	%{!?with_qt:--without-qt} \
	%{?with_qt4:--without-qt5} \
	%{?with_npapi:--with-npapi}
%{__make}

TOPDIR=$(pwd)
cd perl
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INC="-I${TOPDIR}/include" \
	LIBS="-L${TOPDIR}/zbar/.libs -lzbar"

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la

%{__make} -C perl install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Barcode/ZBar/*.pod
# not rm -r to ensure it's empty after .pod removal
rmdir $RPM_BUILD_ROOT%{perl_vendorarch}/Barcode/ZBar
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Barcode/ZBar/.packlist
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%if %{with npapi}
install -d $RPM_BUILD_ROOT%{_browserpluginsdir}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/libzbarplugin.so* $RPM_BUILD_ROOT%{_browserpluginsdir}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libzbarplugin.{la,a}
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
%doc COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/zbarcam
%attr(755,root,root) %{_bindir}/zbarimg
%attr(755,root,root) %{_libdir}/libzbar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzbar.so.0
%dir %{_datadir}/%{name}
%{_mandir}/man1/zbarcam.1*
%{_mandir}/man1/zbarimg.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzbar.so
%{_libdir}/libzbar.la
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
%attr(755,root,root) %{_libdir}/libzbargtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzbargtk.so.0

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzbargtk.so
%{_libdir}/libzbargtk.la
%{_includedir}/zbar/zbargtk.h
%{_pkgconfigdir}/zbar-gtk.pc

%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libzbargtk.a

%if %{with qt}
%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zbarcam-qt
%attr(755,root,root) %{_libdir}/libzbarqt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzbarqt.so.0

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzbarqt.so
%{_libdir}/libzbarqt.la
%{_includedir}/zbar/QZBar.h
%{_includedir}/zbar/QZBarImage.h
%{_pkgconfigdir}/zbar-qt.pc

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libzbarqt.a
%endif

%files -n perl-Barcode-ZBar
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/Barcode
%{perl_vendorarch}/Barcode/ZBar.pm
%dir %{perl_vendorarch}/auto/Barcode
%dir %{perl_vendorarch}/auto/Barcode/ZBar
%attr(755,root,root) %{perl_vendorarch}/auto/Barcode/ZBar/ZBar.so
%{_mandir}/man3/Barcode::ZBar*.3pm*

%files -n python-zbar
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/zbar.so

%files -n python-zbar-pygtk
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/zbarpygtk.so

%if %{with npapi}
%files -n browser-plugin-zbar
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libzbarplugin.so*
%endif
