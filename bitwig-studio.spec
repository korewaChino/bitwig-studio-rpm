%undefine _disable_source_fetch
%undefine __brp_mangle_shebangs

%global         debug_package %{nil}
%global         __strip /bin/true
%global         __requires_exclude_from ^/opt/bitwig-studio/.*$
%global         __provides_exclude_from ^/opt/bitwig-studio/.*$

Name:           bitwig-studio
Version:        5.3.13
Release:        1%{?dist}
Summary:        Music production and performance system
Group:          Multimedia

License:        EULA
URL:            https://www.bitwig.com/

Source0:        https://www.bitwig.com/dl/Bitwig%20Studio/5.3.13/installer_linux/#/%{name}-%{version}.deb


# This "meta-spec" will download the Debian version of Bitwig Studio, extract it, then rebuild the binaries as an RPM instead.
BuildRequires:  alien
Requires: ffmpeg

# todo: Maybe override with system JRE,

ExclusiveArch:  x86_64
# make this a nosrc package, becuase it's not free
# NoSource:       0

%description
Bitwig Studio is a multi-platform music-creation system for production, remixing and performance with a focus on flexible editing tools and a super-fast workflow.

%prep
rm -rf %{name}-%{version}
# extract the deb package
export QA_RPATHS=$(( 0x0001|0x0010 ))
alien -s %{SOURCE0}
%setup -TcDn %{name}-%{version}

%install
# rm -rf $RPM_BUILD_ROOT
# cd %{name}-%{version}
mkdir -p %{buildroot}/opt/bitwig-studio
cp -ax opt/ %{buildroot}/
cp -ax usr %{buildroot}/
ln -sfv /usr/bin/ffmpeg %{buildroot}/opt/bitwig-studio/bin/ffmpeg
ln -sfv /usr/bin/ffprobe %{buildroot}/opt/bitwig-studio/bin/ffprobe
export QA_SKIP_RPATHS=1

%files
%license opt/bitwig-studio/EULA.txt
%dir /opt/bitwig-studio
/opt/bitwig-studio/*
%{_bindir}/bitwig-studio
%{_datadir}/icons/hicolor/128x128/apps/com.bitwig.BitwigStudio.png
%{_datadir}/icons/hicolor/48x48/apps/com.bitwig.BitwigStudio.png
%{_datadir}/icons/hicolor/scalable/apps/com.bitwig.BitwigStudio.svg

%{_datadir}/applications/com.bitwig.BitwigStudio.desktop
%{_datadir}/icons/hicolor/scalable/mimetypes/com.bitwig.BitwigStudio*
%{_datadir}/metainfo/com.bitwig.BitwigStudio.appdata.xml
%{_datadir}/mime/packages/com.bitwig.BitwigStudio.xml

%changelog
* Wed Dec 15 2021 Cappy Ishihara <cappy@cappuchino.xyz>
-
