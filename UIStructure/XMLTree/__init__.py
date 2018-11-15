import XMLTree.ProcessXml as PX
import XMLTree.UIElementFrequency as UIEF
import XMLTree.DecompileAPK as DeAPK
import XMLTree.ElementMappedToCharacter as EMTC
import XMLTree.EditDistance as ED
import os
import XMLTree.SimilarityCompareByUI as SCBU

if __name__ == '__main__':

    # print(PX.getStrHash("abcdefg"))
    # print(PX.getStrHash("abccefg"))

    # print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\decompile\talk'
    #                                  r'\True Love – Find a date Chat and Flirt for free_v2.3_apkpure.com\res\layout'))
    # print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\decompile\talk\whispar_v3.1.1_apkpure.com\res\layout'))
    # print(UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk'
    #                                  r'\True Love – Find a date Chat and Flirt for free_v2.3_apkpure.com\res\layout'))
    # EleTup1 = UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk'
    #                                  r'\True Love – Find a date Chat and Flirt for free_v2.3_apkpure.com\res\layout')
    # print(UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk\whispar_v3.1.1_apkpure.com\res\layout'))
    # EleTup2 = UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk\whispar_v3.1.1_apkpure.com\res\layout')
    #
    # EleDict = EMTC.getElementDictionary(EleTup1, EleTup2)
    # print(EleDict)
    # PX.getTreeFromXmlPath(r'C:\Users\Administrator\Desktop\demoxml')
    # PX.getMapTreeFromXmlPath(r'C:\Users\Administrator\Desktop\demoxml', r'C:\Users\Administrator\Desktop\ApkOutputTxt', EleDict)

    ############全局文件路径的定义##########

    ApkPath = r'C:\Users\Administrator\Desktop\qqq'       #APK文件的路径
    ApkDecompileOutputPath = r'C:\Users\Administrator\Desktop\decompile'   #反编译文件的输出路径
    TxtOutputPath = r'C:\Users\Administrator\Desktop\ApkOutputTxt'    #APK的UI元素对应的TXT的保存目录

    # DeAPK.decompileAPk(ApkPath, ApkDecompileOutputPath, 10)      #反编译APK文件
    # UIEF.getUIElementFrequency(ApkDecompileOutputPath)
    PX.getMapTreeFromXmlPath(ApkDecompileOutputPath, TxtOutputPath)
    SCBU.SimilarityCompare(TxtOutputPath)






