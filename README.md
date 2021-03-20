# pymorse

a Python3 Morse library

# TODO:

- [x] Handle text to morse conversion
- [x] Handle morse to text conversion
- [x] Handle custom dots and dahses
- [x] Create audible dots and dashes
- [ ] Support multiple standards
- [ ] Decode text from audio file
- [ ] Decode text from audio stream (pipe support)
- [ ] ???
- [ ] ~PROFIT~

# Linux

On Pop OS! 20.10 everything works out of the box.

# OS X

On Mac OS X `playsound` package might give you issues about AppKit mising and when you try to run `pip install -U AppKit` it might give you a clang error about `MACOSX_DEPLOYMENT_TARGE` such as `clang: error: invalid version number in 'MACOSX_DEPLOYMENT_TARGET=11'`. This can be solved by installing `PyObjC` with `pip install -U PyObjC`.

# Windows

???
