#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
Summary:	Nagios XML Engine
Summary(pl.UTF-8):	Silnik XML dla Nagiosa
Name:		nagios-nxe
Version:	1.0
Release:	0.2
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/nxe/NXEv1r0.tar.gz
# Source0-md5:	01b0747367fe96f0f302d90da29b1e3b
Patch0:		%{name}-2.0.patch
Patch1:		%{name}-config.patch
URL:		http://nxe.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps}
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl-CGI
BuildRequires:	perl-Frontier-RPC
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Writer-String
BuildRequires:	perl-XML-XSLT-Wrapper
%endif
Requires(triggerpostun):	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nxe

%description
The Nagios XML Engine (NXE for short) is an Open Source XML processing
layer for the Nagios scheduling & monitoring platform. NXE provides an
XML interface for the most critical aspects of managing and reporting
on your Nagios infrastructure via XML.

%description -l pl.UTF-8
NXE (Nagios XML Engine) to warstwa przetwarzania XML dla platformy
szeregującej i monitorującej Nagios. NXE udostępnia interfejs XML do
najbardziej krytycznych aspektów zarządzania i raportowania z
infrastruktury Nagiosa.

%prep
%setup -qc
# undos the source
find . -type f -print0 | xargs -0 sed -i -e 's,\r$,,'
%patch -P0
%patch -P1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install nxe.pl $RPM_BUILD_ROOT%{_bindir}/nxe
install nxe_client.pl $RPM_BUILD_ROOT%{_bindir}/nxe_client
cp -a nxe.dtd nxe.config $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc USAGE.txt nxe_sample.xsl
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nxe.config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nxe.dtd
%attr(755,root,root) %{_bindir}/nxe
%attr(755,root,root) %{_bindir}/nxe_client
