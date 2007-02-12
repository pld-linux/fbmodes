Summary:	XFree86/SVGAlib/FrameBuffer mode lines generator
Summary(pl.UTF-8):	Generator trybów graficznych dla XFree86/SVGAlib/FrameBuffer
Name:		fbmodes
Version:	1.2.2
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://oktober.stc.cx/get/src/%{name}-%{version}.tar.bz2
# Source0-md5:	0a066b01e88d076b95565f2d6e18cdea
URL:		http://bisqwit.iki.fi/source/fbmodes.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
Requires:	argh = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modeline is a small utility to make XFree86/SVGAlib/FrameBuffer
modelines.

%description -l pl.UTF-8
Modeline jest małym narzędziem do generowania trybów graficznych dla
XFree86, SVGAlib oraz FrameBuffera.

%package -n argh
Summary:	argh library for fbmodes
Summary(pl.UTF-8):	Biblioteka argh dla fbmodes
Group:		Libraries

%description -n argh
argh library.

%description -n argh -l pl.UTF-8
Biblioteka argh.

%package -n argh-devel
Summary:	argh library devel files
Summary(pl.UTF-8):	Pliki nagłówkowe argh
Group:		Development/Libraries
Requires:	argh = %{version}-%{release}

%description -n argh-devel
Developement files for argh library.

%description -n argh-devel -l pl.UTF-8
Pliki potrzebne do pisania programów korzystających z argh.

%package -n argh-static
Summary:	Static argh library
Summary(pl.UTF-8):	Statyczna biblioteka argh
Group:		Development/Libraries
Requires:	argh-devel = %{version}-%{release}

%description -n argh-static
Static argh library.

%description -n argh-static -l pl.UTF-8
Statyczna biblioteka argh.

%prep
%setup -q

%build
%{__make} \
	OPTIM="%{rpmcflags} -ffast-math"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/argh,%{_libdir}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
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
%dir %{_includedir}/argh
%{_includedir}/argh/*.h*

%files -n argh-static
%defattr(644,root,root,755)
%{_libdir}/*.a
