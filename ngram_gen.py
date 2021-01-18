def stringToNGrams(s, n=3):
    d = dict()
    for i in range(len(s)):
        for j in range(n):
            sub_str = s[i:i+j+1]
            
            if sub_str in d:
                d[sub_str] += 1
            else:
                d[sub_str] = 1
    return d
    
def findChineseText(line):
    import re
    return "".join(re.findall('[\u4e00-\u9fff]+', line))
    
def processText(file, min_freq=25):
    d = dict()
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            text = findChineseText(line)
            string_d = stringToNGrams(text, 7)
            for k, v in string_d.items():
                if k in d:
                    d[k] += v
                else:
                    d[k] = v
    
    output = file.split(".")[0] + "_out.txt"
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    with open(output, "w", encoding="utf-8") as f:
        for k, v in d.items():
            if v < min_freq:
                break
            f.write(f"{k}\t{v}\n")
