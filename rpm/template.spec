Name:           ros-indigo-pal-msgs
Version:        0.11.3
Release:        0%{?dist}
Summary:        ROS pal_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-pal-behaviour-msgs
Requires:       ros-indigo-pal-control-msgs
Requires:       ros-indigo-pal-detection-msgs
Requires:       ros-indigo-pal-device-msgs
Requires:       ros-indigo-pal-interaction-msgs
Requires:       ros-indigo-pal-motion-model-msgs
Requires:       ros-indigo-pal-multirobot-msgs
Requires:       ros-indigo-pal-navigation-msgs
Requires:       ros-indigo-pal-tablet-msgs
Requires:       ros-indigo-pal-vision-msgs
Requires:       ros-indigo-pal-walking-msgs
Requires:       ros-indigo-pal-wifi-localization-msgs
BuildRequires:  ros-indigo-catkin

%description
PAL-specific messages and services

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 21 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.3-0
- Autogenerated by Bloom

