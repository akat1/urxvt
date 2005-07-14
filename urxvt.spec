Summary:	Rxvt terminal with unicode support and some improvements
Summary(pl):	Terminal Rxvt z obs�ug� unicode i kilkoma usprawnieniami
Name:		urxvt
Version:	5.7
Release:	1
Group:		X11/Applications
License:	GPL
Source0:	http://dist.schmorp.de/rxvt-unicode/rxvt-unicode-%{version}.tar.bz2
# Source0-md5:	b6808e467c6328da8baf2d5320cac6c5
Source1:	%{name}.desktop
URL:		http://software.schmorp.de
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	xft-devel
Requires:	terminfo
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
sed -i -e 's|-O3||' autoconf/configure.in
%build
mv -f autoconf/{configure.in,xpm.m4} .
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
%{__make} \
	CPPFLAGS="$CPPFLAGS %{rpmcflags}"

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
%{_desktopdir}/urxvt.desktop
%{_mandir}/man*/*
