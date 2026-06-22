%define		dbname	Country
Summary:	GeoLite2 Country - Country database for GeoIP
Summary(pl.UTF-8):	GeoLite2 Country - baza danych krajów dla GeoIP
Name:		GeoLite2-db-%{dbname}
Version:	20190408
Release:	1
License:	CC-BY-SA v4.0
Group:		Applications/Databases
# Last freely-redistributable (CC-BY-SA 4.0) GeoLite2 build before MaxMind's
# 2019-12-30 license-key wall, recovered from the Internet Archive.
Source0:	https://web.archive.org/web/20190409074343id_/http://geolite.maxmind.com/download/geoip/database/GeoLite2-%{dbname}.mmdb.gz?/GeoLite2-%{dbname}-%{version}.mmdb.gz
# Source0-md5:	7e66ec9d1dbb60bfc15b9898863af597
URL:		http://dev.maxmind.com/geoip/geoip2/geolite2/
BuildRequires:	gzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoLite2 databases are free IP geolocation databases comparable to,
but less accurate than, MaxMind's GeoIP2 databases.

This package ships the last freely-redistributable (CC-BY-SA 4.0) GeoLite2
release, made before MaxMind required a license key in December 2019. It is
a frozen historical snapshot and is no longer updated; for current data use
the geoipupdate package with a (free) MaxMind license key.

%prep
%setup -qcT
cp -p %{SOURCE0} GeoLite2-%{dbname}.mmdb.gz

# -N: take the build date from the gzip header, not the archive download mtime
gunzip -N GeoLite2-%{dbname}.mmdb.gz

ver=$(TZ=GMT stat -c '%y' GeoLite2-%{dbname}.mmdb | awk '{print $1}' | tr -d -)
if [ "$ver" != %{version} ]; then
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP
cp -p GeoLite2-%{dbname}.mmdb $RPM_BUILD_ROOT%{_datadir}/GeoIP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/GeoIP/*.mmdb
