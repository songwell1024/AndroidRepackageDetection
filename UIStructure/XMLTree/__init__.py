import XMLTree.ProcessXml as PX
import XMLTree.UIElementFrequency as UIEF
import XMLTree.DecompileAPK as DeAPK
import XMLTree.ElementMappedToCharacter as EMTC
import XMLTree.EditDistance as ED
import os
import XMLTree.SimilarityCompareByUI as SCBU
import XMLTree.GetNotMapElementFrequency as GNMEF

if __name__ == '__main__':

    # print(PX.getStrHash("abcdefg"))
    # print(PX.getStrHash("abccefg"))

    ############全局文件路径的定义##########

    ApkPath = r'C:\Users\Administrator\Desktop\qqq'       #APK文件的路径
    ApkDecompileOutputPath = r'C:\Users\Administrator\Desktop\decompile'   #反编译文件的输出路径
    TxtOutputPath = r'C:\Users\Administrator\Desktop\ApkOutputTxt'    #APK的UI元素对应的TXT的保存目录

    # DeAPK.decompileAPk(ApkPath, ApkDecompileOutputPath, 10)      #反编译APK文件
    # UIEF.getUIElementFrequency(ApkDecompileOutputPath)
    # PX.getMapTreeFromXmlPath(ApkDecompileOutputPath, TxtOutputPath)
    # # SCBU.SimilarityCompare(TxtOutputPath)
    # GNMEF.remainingElementFrequency(TxtOutputPath)
    s1 = 'c1(e2, p2, k2, b2(b3(d4, a4)), e2)'
    s2 = 'c1(e2(p3, k3, b3(b4(d5, a5))), e2)'
    s11 = 'c(e, p, k, b(b(d, a)), e)'
    s22 = 'c(e(p, k, b(b(d, a))), e)'

    print(ED.editDistanceSimilarity(s1,s2))
    print(ED.editDistanceSimilarity(s11,s22))






