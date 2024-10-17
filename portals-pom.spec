%{?_javapackages_macros:%_javapackages_macros}
Name:          portals-pom
Version:       1.3
Release:       7.0%{?dist}
Summary:       Apache Portals parent pom
License:       ASL 2.0
Url:           https://portals.apache.org/
# svn export http://svn.apache.org/repos/asf/portals/portals-pom/tags/portals-pom-1.3
# tar czf portals-pom-1.3-src-svn.tar.gz portals-pom-1.3
Source0:       %{name}-%{version}-src-svn.tar.gz
BuildRequires: java-devel
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildArch:     noarch

%description
Apache Portals is a collaborative software development project
dedicated to providing robust, full-featured, commercial-quality,
and freely available Portal related software on a wide variety of
platforms and programming languages. This project is managed in
cooperation with various individuals worldwide (both independent and
company-affiliated experts), who use the Internet to communicate, plan,
and develop Portal software and related documentation.

%prep
%setup -q

%pom_remove_plugin :ianal-maven-plugin

for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 29 2013 gil cattaneo <puntogil@libero.it> 1.3-6
- switch to XMvn and pom macros , minor changes to adapt to current guideline

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 gil cattaneo <puntogil@libero.it> 1.3-2
- Remove empty javadoc package

* Sat May 19 2012 gil cattaneo <puntogil@libero.it> 1.3-1
- initial rpm

