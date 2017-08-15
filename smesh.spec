Summary:	OpenCascade based MESH framework
Name:		smesh
Version:	6.7.4
Release:	1
License:	LGPLv2
Group:		Libraries
URL:		https://github.com/tpaviot/smesh
Source0:	https://github.com/tpaviot/smesh/archive/%{version}.tar.gz
# Source0-md5:	6f7067745c62a8b8183d880963df57f8
BuildRequires:	FreeImage-devel
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	OCE-devel
BuildRequires:	OCE-draw
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	dos2unix
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	f2c
BuildRequires:	freetype-devel
BuildRequires:	gcc-fortran
BuildRequires:	tbb-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel


# Dependencies for optional NETGETPlugin library.
#BuildRequires:  netgen-mesh-devel
#BuildRequires:  netgen-mesh-devel-private


%description
A complete OpenCascade based MESH framework.

%package doc
Summary:	Development documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Development documentation for %{name}.


%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and headers for %{name}.


%prep
%setup -q

dos2unix -k LICENCE.lgpl.txt

%build
install -d build
cd  build
%cmake \
	   -DMONOLITHIC_BUILD=OFF \
	   ../

%{__make} all doc

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %exclude %{_libdir}/libSMESH.so
%attr(755,root,root) %{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%doc build/doc/html/*
%{_includedir}/smesh
%attr(755,root,root) %{_libdir}/libSMESH.so
