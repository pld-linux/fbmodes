Summary:	XFree86/SVGAlib/FrameBuffer mode lines generator
Summary(pl):	Generator trybów graficznych dla XFree86/SVGAlib/FrameBuffer
Name:		fbmodes
Version:	1.2.1
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://oktober.stc.cx/get/src/%{name}-%{version}.tar.bz2
URL:		http://oktober.stc.cx/source/fbmodes.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modeline is a small utility to make XFree86/SVGAlib/FrameBuffer
modelines.

%description -l pl
Modeline jest ma³ym narzêdziem do generowania trybów graficznych dla
XFree86, SVGAlib oraz FrameBuffera.

%package -n argh
Summary:	argh library for fbmodes
Summary(pl):	biblioteka argh dla fbmodes
Group:		Libraries

%description -n argh
Library argh.

%description -n argh -l pl
Biblioteka argh.

%package -n argh-devel
Summary:	argh library devel files
Group:		Development/Libraries
Requires:	argh

%description -n argh-devel
Developement files for argh.

%description -n argh-devel -l pl
Pliki potrzebne do pisania programów przy u¿yciu argh.

%package -n argh-static
Summary:	Static argh library
Summary(pl):	Statyczna biblioteka argh
Group:		Development/Libraries

%description -n argh-static
Static argh library.

%description -n argh-static -l pl
Statyczna biblioteka argh

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/argh,%{_libdir}}

%{__make} install BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INCDIR=$RPM_BUILD_ROOT%{_includedir}/argh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.php
%attr(755,root,root) %{_bindir}/*

%files -n argh
%defattr(644,root,root,755)
%doc argh/*.php
%attr(755,root,root) %{_libdir}/*.so

%files -n argh-devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/argh/*.h

%files -n argh-static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
