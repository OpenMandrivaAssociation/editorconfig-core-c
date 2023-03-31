#global _smp_build_ncpus 4

%define major 0
%define libname %mklibname editorconfig %{major}
%define develname %mklibname editorconfig -d

Name:		editorconfig-core-c
Version:	0.12.5
Release:	3
Summary:	EditorConfig core library written in C
License:	BSD
Group:		System/Libraries
Url:		http://editorconfig.org/
Source:		https://github.com/editorconfig/editorconfig-core-c/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		editorconfig-core-c-0.12.1-no_timestamp.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pkgconfig(libpcre2-posix)

%description
EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. The EditorConfig
project maintains a file format and plugins for various text editors which allow
this file format to be read and used by those editors. For information on the
file format and supported text editors, see the EditorConfig website.

#------------------------------------------------

%package -n editorconfig
Summary:	Commandline utilities for EditorConfig
Group:		Text tools

%description -n editorconfig
EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. The EditorConfig
project maintains a file format and plugins for various text editors which allow
this file format to be read and used by those editors. For information on the
file format and supported text editors, see the EditorConfig website.

This package contains command line utilities.

#------------------------------------------------

%package -n %{libname}
Summary:	EditorConfig core library written in C
Group:		System/Libraries

%description -n %{libname}
EditorConfig makes it easy to maintain the correct coding style when switching
between different text editors and between different projects. The EditorConfig
project maintains a file format and plugins for various text editors which allow
this file format to be read and used by those editors. For information on the
file format and supported text editors, see the EditorConfig website.

This package contains library files for %{name}.

#------------------------------------------------

%package -n %{develname}
Summary:	Development files for EditorConfig core library written in C
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	editorconfig-devel = %{version}-%{release}
Provides:	libeditorconfig-devel = %{version}-%{release}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

#------------------------------------------------

%prep
%autosetup -p1

%build
mkdir -p build/doc/man
%cmake \
	-DLIB_SUFFIX=%{_lib} \
	-DINSTALL_HTML_DOC=ON

%make_build

%install
%make_install -C build

# we don't want these
find %{buildroot} -name '*.a' -delete

%files -n editorconfig
%license LICENSE
%{_bindir}/editorconfig*
%doc %{_mandir}/man1/editorconfig*
%doc %{_mandir}/man5/editorconfig*

%files -n %{libname}
%license LICENSE
%{_libdir}/libeditorconfig.so.%{major}{,.*}

%files -n %{develname}
%doc CONTRIBUTORS README.md
%license LICENSE
%{_docdir}/editorconfig/
%{_includedir}/editorconfig/
%{_libdir}/libeditorconfig.so
%{_libdir}/cmake/EditorConfig/
%{_libdir}/pkgconfig/editorconfig.pc
%doc %{_mandir}/man3/editorconfig*
