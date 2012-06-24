Summary:	Rxvt terminal with unicode support and some improvements
Summary(pl):	Terminal Rxvt z obs�ug� unicode i kilkoma usprawnieniami
Name:		urxvt
Version:	4.0
Release:	2
Group:		X11/Applications
License:	GPL
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
# Source0-md5:	d2a9505ab50f79e7f65bbdfe675cdd58
Source1:	%{name}.desktop
Patch0:		%{name}-libname.patch
URL:		http://software.schmorp.de
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URxvt is a Rxvt modification which includes:
- unicode support
- xft font support (antialiasing)
- background pixmaps
- background tinting

%description -l pl
URxvt jest modyfikacj� Rxvt uwzgl�dniaj�c�:
- obs�ug� unicode
- obs�ug� czcionek xft (antialiasing)
- mo�liwo�� ustawienia grafiki jako t�a
- cieniowanie t�a

%prep
%setup -q -n rxvt-unicode-%{version}
%patch0 -p1

%build
mv -f autoconf/{configure.in,xpm.m4} .
#CFLAGS="%{rpmcflags} -DLINUX_KEYS"
%{__libtoolize}
%{__aclocal} -I .
%{__autoheader}
%{__autoconf}
%{__automake} || :
%configure \
	--enable-shared \
	--disable-static \
	--enable-everything \
	--enable-xgetdefault \
	--enable-mousewheel \
	--disable-menubar \
	--enable-next-scroll \
	--enable-ttygid \
	--with-term=rxvt \
	--enable-half-shadow \
	--enable-smart-resize \
	--enable-256-color \
	--enable-24bit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,7}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
echo '.so urxvtc.1' >$RPM_BUILD_ROOT%{_mandir}/man1/urxvtd.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/menu/* Changes doc/README.*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/liburxvt.so*
%{_desktopdir}/urxvt.desktop
%{_mandir}/man*/*
