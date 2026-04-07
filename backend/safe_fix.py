import csv
import os

src = r'data\dictionary_daily.csv'
tmp = r'data\dictionary_daily_fixed_final.csv'

try:
    with open(src, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print("File is empty.")
        exit()

    header = lines[0].strip().split(',')
    data = []
    
    for i, line in enumerate(lines[1:], 1):
        line = line.strip()
        if not line or line.startswith('word,'): continue
        
        parts = line.split(',')
        if len(parts) >= 5:
            word = parts[0]
            p_type = parts[1]
            pron = parts[2]
            # Meaning is everything between fields 0,1,2 and the last one
            meaning = ','.join(parts[3:-1])
            unit = parts[-1]
            data.append([word, p_type, pron, meaning, unit])

    with open(tmp, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        writer.writerows(data)
        
    # Overwrite the original file
    if os.path.exists(src):
        os.remove(src)
    os.rename(tmp, src)
    
    print(f"Successfully fixed {len(data)} lines and overwrote the original file.")

except Exception as e:
    print(f"Error occurred: {e}")
