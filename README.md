# RPM meta-spec for Bitwig Studio
This spec file builds an RPM package for Bitwig Studio by unpacking the Debian package, and then properly packaging the binaries, made for you in case you don't like the Flatpak version.


## Building the RPM
Make sure you have the packages necessary to build the RPM:
```
sudo dnf install rpm-build rpmdevtools
```

Then, create the `~/rpmbuild` structure if you haven't already:
```
rpmdev-setuptree
```

And finally, build the RPM:
```
rpmbuild -bb bitwig-studio.spec
```
This will automatically download the original Debian package from the Bitwig website, and then rebuild it.
