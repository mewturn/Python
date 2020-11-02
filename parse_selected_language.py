#
# Main idea: to extract only a particular "language" from text content containing words / characters from different language.
# Using regex, we search for characters within particular unicode ranges and exclude the rest.
#

import re

def parse_only_text(string, setting):
    '''
    Available settings:
    * "alphabets": A-Z ASCII alphabets
    * "chinese" Chinese characters
    '''
    
    regex_setting = {
        "alphabets": r"[A-Za-z '\"]+",
        "chinese": r"[\u4e00-\u9fff]+"
    }
    
    if setting in regex_setting:
        comp = regex_setting[setting]
        result = re.findall(comp, string)

        if setting == "alphabets":
            joiner = " "
        else:
            joiner = ""
        
        return (joiner.join(result))

if __name__ == "__main__":
    filepath = "C:\\Users\\user\\Desktop\\8501_\\"
    files = [
        "AST_Ep4_SRT.srt",
        "AST_Ep1_.SRT",
        "AST_Ep2_.SRT",
        "AST_Ep3_SRT.srt"
    ]


    for file in files:
        path = f"{filepath}{file}"
        text_en = ""
        text_zh = ""

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                result_en = parse_only_text(line, "alphabets")
                result_zh = parse_only_text(line, "chinese")

                if result_en and not result_en.isspace():
                    text_en += f"{result_en}\n"

                if result_zh and not result_zh.isspace():
                    text_zh += f"{result_zh}\n"

        out_filename = file.replace(".srt", "")
        out_en = f"{filepath}{out_filename}_en.srt"
        out_zh = f"{filepath}{out_filename}_zh.srt"

        with open(out_en, "w", encoding="utf-8") as f_en:
            f_en.write(text_en)

        with open(out_zh, "w", encoding="utf-8") as f_zh:
            f_zh.write(text_zh)
