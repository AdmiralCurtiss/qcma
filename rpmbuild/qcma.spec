# 
# qcma spec file
# 

%define _version 0.3.12

%if "%{_version}" == "testing" || "%{_version}" == "master"
%define _verprefix %{_version}
%else
%define _verprefix v%{_version}
%endif

%if 0%{?fedora}
%define _qt5base qt5-qtbase
%define _qt5imageformats qt5-qtimageformats
%define _pkgconfig pkgconfig
%define _qt5linguist qt5-linguist
%define _qt5basedevel qt5-qtbase-devel
%else
%define qmake_qt5 qmake-qt5
%define _qt5base libqt5-qtbase
%define _qt5imageformats libqt5-qtimageformats
%define _pkgconfig pkg-config
%define _qt5linguist  libqt5-linguist
%define _qt5basedevel libqt5-qtbase-devel
%endif

Name:           qcma
Summary:        PSVita Content Manager Assistant
License:        GPL-3.0
Release:        1
Version:        %{_version}
URL:            https://github.com/codestation/qcma
Source:         https://github.com/codestation/qcma/archive/%{_verprefix}/qcma-%{_version}.tar.gz
Group:          Productivity/File utilities
Requires:       libnotify
Requires:       ffmpeg
Requires:       %{_qt5base}
Requires:       %{_qt5imageformats}
Requires:       libvitamtp5 >= 2.5.9
BuildRequires:  gcc-c++ 
BuildRequires:  %{_pkgconfig}
BuildRequires:  libnotify-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libvitamtp-devel
BuildRequires:  %{_qt5linguist}
BuildRequires:  %{_qt5basedevel}

%description
QCMA is an cross-platform application to provide a Open Source implementation
of the original Content Manager Assistant that comes with the PS Vita. QCMA
is meant to be compatible with Linux, Windows and MAC OS X.

%prep
%setup -n %{name}-%{version}

%build
lrelease-qt5 common/resources/translations/*.ts
%{qmake_qt5} PREFIX=/usr qcma.pro CONFIG+="QT5_SUFFIX"
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/qcma
%{_prefix}/share/applications/qcma.desktop
%{_prefix}/share/icons/hicolor/64x64/apps/qcma.png
%{_prefix}/share/man/man1/qcma.1.gz

%changelog

%package cli
Summary: Content Manager Assistant for the PS Vita (headless version)
%description cli
Headless version of Qcma
%files cli
%{_bindir}/qcma_cli
%{_prefix}/share/man/man1/qcma_cli.1.gz
