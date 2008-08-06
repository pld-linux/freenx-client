Summary:	a Free NoMachine (NX) client
Name:		freenx-client
Version:	0.9
Release:	0.1
License:	GPL v2 or later
Group:		System/X11/Utilities
URL:		http://freenx.berlios.de/
BuildRequires:	doxygen
BuildRequires:	libnxcl-devel
BuildRequires:	QtGui-devel >= 4.4.0
BuildRequires:	QtXml-devel >= 4.4.0
BuildRequires:	QtCore-devel >= 4.4.0
Source0:        http://download.berlios.de/freenx/freenx-client-%{version}.tar.bz2
# Source0-md5:  777b3cda7a245e3870d4870a9460cb73
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a free implementation of a NX session client.

%prep
%setup -q

%build
cd qtnx
qmake-qt4
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install qtnx/qtnx $RPM_BUILD_ROOT%{_bindir} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtnx
