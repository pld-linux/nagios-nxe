%include	/usr/lib/rpm/macros.perl
Summary:	Nagios XML Engine
Name:		nagios-nxe
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/nxe/NXEv1r0.tar.gz
# Source0-md5:	01b0747367fe96f0f302d90da29b1e3b
URL:		http://nxe.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires(triggerpostun):	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Nagios XML Engine (NXE for short) is an Open Source XML processing
layer for the Nagios scheduling & monitoring platform. NXE provides an
XML interface for the most critical aspects of managing and reporting
on your Nagios infrastructure via XML.

%prep
%setup -qc
# undos the source
find . -type f -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install nxe.pl nxe_client.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc USAGE.txt
%attr(755,root,root) %{_bindir}/nxe.pl
%attr(755,root,root) %{_bindir}/nxe_client.pl
