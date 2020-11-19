class OfflineCase:
    def __init__(self, filename):
        self.filename = filename
        self.output_filename = filename.split(".")[0]
        self.parseSegments()
        
    def parseSegments(self):
        import openpyxl
        self.segments = []
        wb = openpyxl.load_workbook(self.filename)
        
        for sheetname in wb.sheetnames:
            sheet = wb[sheetname]     
            i = 4
            
            while True:
                id = sheet[f"A{i}"].value
                source = sheet[f"B{i}"].value
                if id is not None and source is not None:
                    target = sheet[f"C{i}"].value
                    if target is None:
                        target = ""
                    self.segments.append(Segment(id, source, target))
                    i += 1

                else:
                    break            
        
    def convert(self, ext):
        ext_map = {
            "tmx": self.convertTMX(),
            "xliff": self.convertXLIFF()
        }
        
        output_filename = f"{self.output_filename}.{ext}"
        header, body, footer = ext_map[ext]

        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(header)
            f.write(body)
            f.write(footer)
    
    def convertTMX(self):
        header = "<?xml version='1.0' encoding='UTF-8'?>\n"
        header += "<tmx version='1.4'>\n"
        header += "<header adminlang='en' creationtool='WritePath Translation Editor' creationtoolversion='1.0' datatype='tbx' o-tmf='unknown' segtype='block'/>\n"
        header += "<body>\n\n"

        body = ""
        if self.segments:
            for segment in self.segments:
                body += f"<tu origin='tbx' tuid='{segment.id}'>\n"
                body += "<tuv xml:lang='zh-TW'>\n"
                body += f"<seg>{segment.source}</seg>\n"
                body += "</tuv>\n"
                body += "<tuv xml:lang='en'>\n"
                body += f"<seg>{segment.target}</seg>\n"
                body += "</tuv>\n"
                body += "</tu>\n\n"
                
        footer = "</body>\n"
        footer += "</tmx>\n"
        
        return header, body, footer
        
    def convertXLIFF(self):
        header = "<?xml version='1.0' encoding='UTF-8'?>\n"
        header += "<xliff version='1.2' xmlns='urn:oasis:names:tc:xliff:document:1.2'>\n"
        header += "<file original='writepath-case112066' datatype='plaintext' source-language='zh-TW' target-language='en'>\n"
        header += "<body>\n\n"

        body = ""
        if self.segments:
            for segment in self.segments:
                body += f"<trans-unit id='{segment.id}'>\n"
                body += f"<source id='{segment.id}'>{segment.source}</source>\n"
                body += f"<target id='{segment.id}' state='translated'>{segment.target}</target>\n"
                body += "</trans-unit>\n\n"
        
        footer = "</body>\n"
        footer += "</file>\n"
        footer += "</xliff>\n"

        return header, body, footer

class Segment:
    def __init__(self, id, source, target):
        self.id = id
        self.source = source
        self.target = target
        
if __name__ == "__main__":
    import os
    import time
    
    ext_num = input("Select output format - [1]: TMX, [2]: XLIFF\nEnter number: ")
    ext_map = {
        "1": "tmx",
        "2": "xliff"
    }
    try:
        for i in os.listdir():
            if ".xlsx" in i:
                start_time = time.time()
                print(f"Processing file {i}")
                offline_case = OfflineCase(i)
                offline_case.convert(ext_map[ext_num])
                elapsed_time = round(time.time() - start_time, 2)
                print(f"Success! Completed in {elapsed_time} seconds.")
        input("Task completed. Press <Enter> to close this window.")
    except Exception as e:
        input(f"An error occurred. {repr(e)}. Press <Enter> to close this window.")
