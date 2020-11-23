import platform
import WifiExtractorWindow
import WifiExtractorLinux

#OS Detect
OperatingSystem = platform.system()
print("platform : "+ OperatingSystem )
print("************************************")
if OperatingSystem == "Windows" :
    print("   I am  Windows")
    WifiExtractorWindow.WifiExtratorWindow()
elif OperatingSystem == "Linux" :
    print("   I am  Linux")
    WifiExtractorLinux.WifiExtrsctorLinux()
else:
   print("Can't Detect Platform ")

print("************************************")
print("Coder By : h4n24wnyin3")
