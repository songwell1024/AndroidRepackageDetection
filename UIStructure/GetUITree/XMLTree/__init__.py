import XMLTree.processXml as PX
import XMLTree.UIElementFrequency as UIEF
import XMLTree.decompileAPK as DeAPK


if __name__ == '__main__':

    # print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\qq\Subway Boy Rush Runner 3D_v1.4_apkpure.com'))
    # print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\qq\Bus Rush_v1.15.2_apkpure.com'))
    # apk 的存储路径
    apkPath = r'C:\Users\Administrator\Desktop\qqq'
    outputPath = r'C:\Users\Administrator\Desktop\decompile'
    DeAPK.decompileAPk(apkPath, outputPath, 2)



