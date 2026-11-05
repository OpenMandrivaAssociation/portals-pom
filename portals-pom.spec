Name:          portals-pom
Version:       1.4
Release:       1
Summary:       Apache Portals parent pom
License:       ASL 2.0
Url:           https://portals.apache.org/
Source0:       https://repo1.maven.org/maven2/org/apache/portals/portals-pom/%{version}/portals-pom-%{version}.pom
Source1:       https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:     noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption:	validate

%description
Apache Portals is a collaborative software development project
dedicated to providing robust, full-featured, commercial-quality,
and freely available Portal related software on a wide variety of
platforms and programming languages. This project is managed in
cooperation with various individuals worldwide (both independent and
company-affiliated experts), who use the Internet to communicate, plan,
and develop Portal software and related documentation.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%files -f .mfiles
%doc LICENSE
