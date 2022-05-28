rule WannaCry
{
    strings:
        $s1="ADVAPI32.dll"
        $s2="SHELL32.dll"
        $s3="OLEAUT32.dll"
        $s4="WS2_32.dll"
        $s5="- unzip 0.15 Copyright 1998 Gilles Vollant"
        $s6="WANACRY!"
        $s7="msg/m_chinese (simplified).wnryR9"
        $s8="PPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDING"
        $s9="msg/m_bulgarian.wnry"
    condition:
        all of them
}
