import XMLTree.ProcessXml as PX
import XMLTree.UIElementFrequency as UIEF
import XMLTree.DecompileAPK as DeAPK
import ElementMappedToCharacter as EMTC
import EditDistance as ED

if __name__ == '__main__':

    # print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\qq\Subway Boy Rush Runner 3D_v1.4_apkpure.com'))
    #print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\qq\Bus Rush_v1.15.2_apkpure.com'))
    # print(PX.getStrHash("abcdefg"))
    # print(PX.getStrHash("abccefg"))

    # apk 的存储路径

    # apkPath = r'C:\Users\Administrator\Desktop\qqq'
    # outputPath = r'C:\Users\Administrator\Desktop\decompile'
    # DeAPK.decompileAPk(apkPath, outputPath, 1)
    # print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\decompile\talk'
    #                                  r'\True Love – Find a date Chat and Flirt for free_v2.3_apkpure.com\res\layout'))
    # print(UIEF.getUIElementFrequency(r'C:\Users\Administrator\Desktop\decompile\talk\whispar_v3.1.1_apkpure.com\res\layout'))
    # print(UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk'
    #                                  r'\True Love – Find a date Chat and Flirt for free_v2.3_apkpure.com\res\layout'))
    EleTup1 = UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk'
                                     r'\True Love – Find a date Chat and Flirt for free_v2.3_apkpure.com\res\layout')
    # print(UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk\whispar_v3.1.1_apkpure.com\res\layout'))
    EleTup2 = UIEF.getElementPer(r'C:\Users\Administrator\Desktop\decompile\talk\whispar_v3.1.1_apkpure.com\res\layout')

    EleDict = EMTC.getElementDictionary(EleTup1, EleTup2)
    print(EleDict)
    print(PX.getTreeFromXmlPath(r'C:\Users\Administrator\Desktop\demoxml'))
    print(PX.getMapTreeFromXmlPath(r'C:\Users\Administrator\Desktop\demoxml', EleDict))
    print(ED.editDistance("abcde","abcds"))
    print(ED.editDistanceSimilarity("abcsdde", "abcdsfr"))
    # [chr(x) for x in range(ord('a'), ord('z') + 1)]



