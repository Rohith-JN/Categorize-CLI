
extensions = {
    "text": [".txt", ".rtf"],
    "image": [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"],
    "audio" : [".wav", ".mp3", ".ogg", ".gsm", ".dct", ".flac", ".au", ".aiff", ".vox", "raw", ".wma", ".aac", ".atrac",
              ".ra", ".oma", ".omg", ".atp", ".waptt", ".i3pack", ".3ga", ".opus", ".cda", ".wpl", ".rec", ".vdjsample",
              ".mus", ".aax", ".amr", ".ds2", ".sng", ".dss", ".nvf", ".midi", ".m4a", ".pcm", ".mscz", ".ses", ".dvf",
              ".gp5", ".gp4", ".bnk", ".aup", ".acd", ".sf2", ".thd", ".sty", ".mxl", ".band", ".cdfs", ".ram", ".aa",
              ".eac3", ".mogg", ".au", ".seq", ".uax", ".mid", ".kar", ".dlp", ".vce", ".spx", ".m4r", ".wax"],
    "video": [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt",
              ".flv", ".swf", ".avchd", ".vob", ".rm", ".avi", ".3gp", ".3g2", ".mkv", ".MOV"],
    "word": [".doc", ".docx", ".asd", ".dotx",
             ".svd", ".dot", ".wbk", ".docm", ".dotm", ".wll"],
    "powerpoint": [".pptx", ".pptm", ".ppt", ".pps", ".ppsx", ".ppsm",
                   ".pptm", ".sldx", ".pot", ".potx", ".ppam", ".ppa", ".sldm", ".pa", ".potm"],
    "excel": [".xls", ".xlsx", ".xltx", ".xltm", ".xlsb", ".xlsm", ".xlam",
              ".xlb", ".xla", ".xlt", ".xar", ".xlm", ".xl", ".xlw", ".xltx", ".xll", ".xlc"],
    "access": [".accdb"],
    "executables": [".exe", ".msi", ".apk", ".bat", ".com"],
    "pdf": [".pdf"],
    "font": [".fnt", ".fon", ".otf", ".ttf", ".woff",
             ".woff2", ".ofm", ".bmap", ".frf", ".afs"],
    "archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],       
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],     
    "media": [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp", ".wav", ".mp3", ".ogg", ".gsm", ".dct", ".flac", ".au", ".aiff", ".vox", "raw", ".wma", ".aac", ".atrac",
              ".ra", ".oma", ".omg", ".atp", ".waptt", ".i3pack", ".3ga", ".opus", ".cda", ".wpl", ".rec", ".vdjsample",
              ".mus", ".aax", ".amr", ".ds2", ".sng", ".dss", ".nvf", ".midi", ".m4a", ".pcm", ".mscz", ".ses", ".dvf",
              ".gp5", ".gp4", ".bnk", ".aup", ".acd", ".sf2", ".thd", ".sty", ".mxl", ".band", ".cdfs", ".ram", ".aa",
              ".eac3", ".mogg", ".au", ".seq", ".uax", ".mid", ".kar", ".dlp", ".vce", ".spx", ".m4r", ".wax", ".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt",
              ".flv", ".swf", ".avchd", ".vob", ".rm", ".avi", ".3gp", ".3g2", ".mkv", ".MOV"]            
}

text = extensions.get("text") 
image = extensions.get("image")
audio = extensions.get("audio")
video = extensions.get("Video")
gif = extensions.get("gif")
photoshop = extensions.get("photoshop")
word = extensions.get("word")
powerpoint = extensions.get("powerpoint")
excel = extensions.get("excel")
access = extensions.get("access")
executables = extensions.get("executables")
pdf = extensions.get("pdf")
font = extensions.get("font")
archives = extensions.get("archives")
documents = extensions.get("documents")
media = extensions.get("media")

'''
Todo:
1) add adobe extensions
2) add code extensions
3) add more extensions in documents
'''