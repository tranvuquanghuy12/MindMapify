import csv
import os

src = r'd:\Project AI\Dự án Tiếng anh\backend\data\dictionary_daily.csv'
temp_src = src + '.tmp'

try:
    with open(src, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print("File empty")
        exit()

    header = lines[0].strip().split(',')
    data = []
    
    for i, line in enumerate(lines[1:], 1):
        line = line.strip()
        if not line: continue
        
        parts = line.split(',')
        if len(parts) >= 5:
            word = parts[0]
            p_type = parts[1]
            pron = parts[2]
            # Meaning can contain commas, it's everything between index 3 and the last index
            meaning = ','.join(parts[3:-1])
            unit = parts[-1]
            data.append([word, p_type, pron, meaning, unit])
        else:
            print(f"Skipping line {i+1}: {line}")

    with open(src, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerows(data)
        
    print(f"Successfully processed {len(data)} lines.")

except Exception as e:
    print(f"Error: {e}")
